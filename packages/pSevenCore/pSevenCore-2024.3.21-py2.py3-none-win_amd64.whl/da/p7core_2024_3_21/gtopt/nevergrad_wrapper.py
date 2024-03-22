#
# coding: utf-8
# Copyright (C) pSeven SAS, 2010-present
#
import contextlib as _contextlib
import json
import logging
import time
import warnings
import weakref as _weakref
from collections import OrderedDict, deque
from functools import partial

import nevergrad as ng
import numpy as np
from nevergrad import callbacks, optimizers
from nevergrad.common import errors
from nevergrad.common import tools as ngtools
from nevergrad.optimization import utils
from nevergrad.parametrization import parameter as p

from .. import __version__, _distutils_loose_version, exceptions, shared
from ..gtdoe.generator import _append_field_spec, _SolutionSnapshotFactory
from ..loggers import LogLevel
from ..result import Result
from ..shared import _NONE
from ..status import IN_PROGRESS, SUCCESS, UNSUPPORTED_PROBLEM, USER_TERMINATED
from ..utils import buildinfo
from ..utils.designs import (_DetachableSingleCallableRef,
                             _postprocess_designs, _SolutionSnapshot)
from . import api, diagnostic
from .problem import _get_gtopt_negative_infinity, _get_gtopt_positive_infinity
from .solver import ValidationResult

GTOPT_POSITIVE_INFINITY = _get_gtopt_positive_infinity()
GTOPT_NEGATIVE_INFINITY = _get_gtopt_negative_infinity()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False


class BatchOptimizer(optimizers.NGOpt):

  def __init__(self, *args, **kwargs):
    super(BatchOptimizer, self).__init__(*args, **kwargs)
    self._asked_batch_cache = set()

  def _tell(self, *args, **kwargs):
    super(BatchOptimizer, self).tell(*args, **kwargs)
    # The whole batch was calculated, so just clear the cache.
    self._asked_batch_cache.clear()

  def _ask(self, objective_function, constraint_violation, n_attempts):
    candidate = super(BatchOptimizer, self).ask()
    if self.num_workers == 1 or n_attempts == 0:
      return candidate

    def _not_in_archives(candidate):
      # Check both the global Nevergrad archive and cache of the current batch points,
      # that have not been sent to the blackbox yet
      key = candidate.get_standardized_data(reference=self.parametrization)
      # Note that we can not use the key for batch cache since it may be different for the same value within a batch
      return key not in self.archive and candidate.args not in self._asked_batch_cache

    def _has_unknown_responses(candidate):
      # If any of objectives or constraints is not calculated then the point is not considered as duplicate.
      # Actually, both objectives and constraints are evaluated for each point.
      cached_objectives = objective_function.calc_from_cache(*candidate.args, **candidate.kwargs)
      if cached_objectives is None:
        return True
      for c_func in constraint_violation or []:
        if c_func.calc_from_cache(candidate.value) is None:
          return True
      return False

    # Fast check in Nevergrad archive, then slow check for calculated responses.
    # If the point was found in the global archive, it should have all the responses calculated.
    if _not_in_archives(candidate) and _has_unknown_responses(candidate):
      self._asked_batch_cache.add(candidate.args)
      return candidate

    logger.debug("Trying to find a unique candidate instead of the known one %s" % str(candidate.args))
    for i in range(n_attempts):
      # We can not use the `ask` method since it consumes the budget, so just sample from the design space.
      new_candidate = self.parametrization.sample()
      if _not_in_archives(new_candidate) and _has_unknown_responses(new_candidate):
        logger.debug("Unique candidate was found after %d attempts: %s" % (i + 1, str(new_candidate.args)))
        # Note that if the candidate is included to the current batch, it wont have any calculated responses
        if not _has_unknown_responses(candidate):
          cached_objectives = objective_function.calc_from_cache(*candidate.args, **candidate.kwargs)
          if constraint_violation is not None:
            cached_constraints = [c_func.calc_from_cache(candidate.value) for c_func in constraint_violation]
            self.tell(candidate, cached_objectives, cached_constraints)
          else:
            self.tell(candidate, cached_objectives)
        self._asked_batch_cache.add(new_candidate.args)
        return new_candidate
    else:
      # Failed to find a unique candidate
      logger.debug("Failed to find a unique candidate, using the proposed one %s" % str(candidate.args))
      self._asked_batch_cache.add(candidate.args)
      return candidate

  def minimize(
      self,
      objective_function,
      executor = None,
      batch_mode = False,
      verbosity = 0,
      constraint_violation = None,
      n_unique_sampling_attempts=10,
  ):
    """Optimization (minimization) procedure

    !!! This override is needed for the following reasons:  !!!
     - no support for parallel execution of constraints
     - no guarantee that asked points are unique, hence the batch size can not be guaranteed

    Parameters
    ----------
    objective_function: callable
        A callable to optimize (minimize)
    executor: Executor
        An executor object, with method :code:`submit(callable, *args, **kwargs)` and returning a Future-like object
        with methods :code:`done() -> bool` and :code:`result() -> float`. The executor role is to dispatch the execution of
        the jobs locally/on a cluster/with multithreading depending on the implementation.
        Eg: :code:`concurrent.futures.ProcessPoolExecutor`
    batch_mode: bool
        when :code:`num_workers = n > 1`, whether jobs are executed by batch (:code:`n` function evaluations are launched,
        we wait for all results and relaunch n evals) or not (whenever an evaluation is finished, we launch
        another one)
    verbosity: int
        print information about the optimization (0: None, 1: fitness values, 2: fitness values and recommendation)
    constraint_violation: list of functions or None
        each function in the list returns >0 for a violated constraint.

    Returns
    -------
    ng.p.Parameter
        The candidate with minimal value. :code:`ng.p.Parameters` have field :code:`args` and :code:`kwargs` which can
        be directly used on the function (:code:`objective_function(*candidate.args, **candidate.kwargs)`).

    Note
    ----
    for evaluation purpose and with the current implementation, it is better to use batch_mode=True
    """
    # pylint: disable=too-many-branches
    if self.budget is None:
      raise ValueError("Budget must be specified")
    if executor is None:
      executor = utils.SequentialExecutor()  # defaults to run everything locally and sequentially
      if self.num_workers > 1:
        self._warn(
          "num_workers = %d > 1 is suboptimal when run sequentially" % self.num_workers,
          errors.InefficientSettingsWarning,
        )
    assert executor is not None
    tmp_runnings = []
    tmp_finished = deque()
    # go
    sleeper = ngtools.Sleeper()  # manages waiting time depending on execution time of the jobs
    remaining_budget = self.budget - self.num_ask
    first_iteration = True
    #
    while remaining_budget or self._running_jobs or self._finished_jobs:
      # # # # # Update optimizer with finished jobs # # # # #
      # this is the first thing to do when resuming an existing optimization run
      # process finished
      if self._finished_jobs:
        if (remaining_budget or sleeper._start is not None) and not first_iteration:
          # ignore stop if no more suggestion is sent
          # this is an ugly hack to avoid warnings at the end of steady mode
          sleeper.stop_timer()

        violation_results = None
        if constraint_violation is not None:
          violation_results = []
          for constraint_function in constraint_violation:
            constraint_jobs = []
            for candidate, job in self._finished_jobs:
              constraint_jobs.append(
                (candidate, executor.submit(constraint_function, candidate.value))
              )
            while any(not job[1].done() for job in constraint_jobs):
              sleeper.sleep()
            violation_results.append([job[1].result() for job in constraint_jobs])
          # Transpose so that the rows correspond to evaluated points
          violation_results = list(zip(*violation_results))

        while self._finished_jobs:
          x, job = self._finished_jobs[0]
          result = job.result()
          if constraint_violation is not None:
            violation = violation_results.pop(0)
            self._tell(x, result, violation)
          else:
            self._tell(x, result)
          self._finished_jobs.popleft()  # remove it after the tell to make sure it was indeed "told" (in case of interruption)
          if verbosity:
            logger.info("Updating fitness with value %s" % str(result))
        if verbosity:
          logger.info("%d remaining budget and %d running jobs" % (remaining_budget, len(self._running_jobs)))
          if verbosity > 1:
            logger.info("Current pessimistic best is: %s" % str(self.current_bests["pessimistic"]))
      elif not first_iteration:
        sleeper.sleep()
      # # # # # Start new jobs # # # # #
      if not batch_mode or not self._running_jobs:
        n_points_to_ask = max(0, min(remaining_budget, self.num_workers - len(self._running_jobs)))
        if verbosity and n_points_to_ask:
          logger.info("Launching %d jobs with new suggestions" % n_points_to_ask)
        for _ in range(n_points_to_ask):
          try:
            # Try to ensure the proper batch size by removing the duplicate points
            candidate = self._ask(objective_function, constraint_violation, n_unique_sampling_attempts)
          except errors.NevergradEarlyStopping:
            remaining_budget = 0
            break
          self._running_jobs.append(
            (candidate, executor.submit(objective_function, *candidate.args, **candidate.kwargs))
          )
        if n_points_to_ask:
          sleeper.start_timer()
      if remaining_budget > 0:  # early stopping sets it to 0
        remaining_budget = self.budget - self.num_ask
      # split (repopulate finished and runnings in only one loop to avoid
      # weird effects if job finishes in between two list comprehensions)
      tmp_runnings, tmp_finished = [], deque()
      for x_job in self._running_jobs:
        (tmp_finished if x_job[1].done() else tmp_runnings).append(x_job)
      self._running_jobs, self._finished_jobs = tmp_runnings, tmp_finished
      first_iteration = False
    return self.provide_recommendation() if self.num_objectives == 1 else p.Constant(None)


class _BatchFuture:
  def __init__(self, args, kwargs, callback_on_check=None):
    self._args = args
    self._kwargs = kwargs
    self._done = False
    self._result = None
    self._callback_on_check = callback_on_check or (lambda: None)

  def done(self):
    self._callback_on_check()
    return self._done

  def result(self):
    self._callback_on_check()
    return self._result

  def set_result(self, result):
    self._done = True
    self._result = result


class BatchExecutor:
  def __init__(self, fn_to_batch_fn, num_workers, batch_timeout_sec=10):
    self._num_workers = num_workers
    self._fn_to_batch_fn = fn_to_batch_fn
    self._fn_futures = dict((fn, []) for fn in self._fn_to_batch_fn)
    self._batch_wait_in_sec = batch_timeout_sec
    self._last_submit = {}

  def _check_results(self, fn):
    if fn in self._last_submit and len(self._fn_futures[fn]):
      if time.time() - self._last_submit[fn] > self._batch_wait_in_sec:
        warnings.warn("Flushing incomplete batch of size %d instead of full batch of size %d due to timeout. Consider reducing the batch size." % (len(self._fn_futures[fn]), self._num_workers))
        self._flush(fn)
        self._last_submit[fn] = time.time()

  def _flush(self, fn):
    futures = self._fn_futures[fn][:self._num_workers]
    if len(futures):
      args = list(zip(*[_._args for _ in futures]))
      kwargs = {key: [_._kwargs[key] for _ in futures] for key in futures[0]._kwargs}
      results = self._fn_to_batch_fn[fn](*args, **kwargs)
      if len(results) != len(futures):
        raise ValueError("Wrong number of batch results. Expected %d, got %d" % (len(futures), len(results)))
      for future, result in zip(futures, results):
        future.set_result(result)
      self._fn_futures[fn] = self._fn_futures[fn][self._num_workers:]

  def submit(self, fn, *args, **kwargs):
    if fn not in self._fn_to_batch_fn:
      raise ValueError("There is no known batch version of the function provided")
    batch_future = _BatchFuture(args, kwargs, partial(self._check_results, fn))
    self._fn_futures[fn].append(batch_future)
    if len(self._fn_futures[fn]) >= self._num_workers:
      self._flush(fn)
    self._last_submit[fn] = time.time()
    return batch_future


def _isfinite(number, neg_inf=GTOPT_NEGATIVE_INFINITY, pos_inf=GTOPT_POSITIVE_INFINITY):
  if np.ndim(number) > 0:
    return np.array([_isfinite(_, neg_inf, pos_inf) for _ in number])
  if number is not None and np.isfinite(number):
    return number > neg_inf and number < pos_inf
  else:
    return False


class _Archive(object):
  # CommonConst::NUMERICS_PRECISION from pSeven Core
  PRECISION = np.finfo(np.float64).eps * 1e4

  def __init__(self, input_names, objective_names, constraint_names, lookup_size=0, cache_size=100):
    self.input_names = input_names
    self.objective_names = objective_names
    self.constraint_names = constraint_names
    self.output_names = objective_names + constraint_names
    self.names = self.input_names + self.output_names
    self._lookup_size = lookup_size
    self._cache_size = cache_size
    # Internal state of archive
    self._data = dict((_, []) for _ in self.names)  # name -> List[value]
    self._n_values = {}  # (name, index) -> idx
    self._cache = OrderedDict()  # binary(x) -> idx
    self._size = 0
    self._initial_sample_size = 0
    self.n_history_hits = 0
    self.n_cache_hits = 0

  @property
  def size(self):
    return self._size

  @property
  def init_size(self):
    return self._initial_sample_size

  def register_initial_sample(self, input_sample, output_sample=None):
    # TODO merge duplicates in initial sample?
    input_sample = np.atleast_2d(input_sample).astype(float)
    if self._size > 0:
      raise ValueError("Can not add initial sample since the evaluation history is not empty. Initial sample should be added first.")
    if input_sample.shape[1] != len(self.input_names):
      raise ValueError("Wrong number of columns in input part of initial sample. Expected %d, got %d." % (len(self.input_names), input_sample.shape[1]))
    if output_sample is not None:
      output_sample = np.atleast_2d(output_sample).astype(float)
      if output_sample.shape != (input_sample.shape[0], len(self.output_names)):
        raise ValueError("Wrong shape of output part of initial sample. Expected (%d, %d), got %s." % (input_sample.shape[0], len(self.input_names), str(output_sample.shape)))
    for i in np.arange(input_sample.shape[0]):
      index = self.find(input_sample[i])
      if output_sample is None:
        self.register(index, input_sample[i])
      else:
        self.register(index, input_sample[i], output_sample[i])
    self._initial_sample_size = self._size

  def _is_equal(self, index, input):
    # GTOpt treats points x0 and x1 as equal if abs(x0 - x1) <= PRECISION * (1 + min(abs(x0), abs(x1))), so do we
    for i, name in enumerate(self.input_names):
      value1 = input[i]
      value2 = self._data[name][index]
      precision = _Archive.PRECISION * (1 + np.minimum(np.abs(value1), np.abs(value2)))
      if np.abs(value1 - value2) > precision:
        return False
    return True

  def _append(self, input, output=None, mask=None):
    if output is None:
      output = [_NONE for _ in self.output_names]
    if mask is None:
      mask = np.ones_like(self.output_names, dtype=bool)

    if len(input) != len(self.input_names):
      raise ValueError("Wrong size of inputs vector. Expected %d, got %d." % (len(self.input_names), len(input)))
    if len(output) != len(self.output_names):
      raise ValueError("Wrong size of outputs vector. Expected %d, got %d." % (len(self.output_names), len(output)))
    if len(mask) != len(self.output_names):
      raise ValueError("Wrong size of outputs mask. Expected %d, got %d." % (len(self.output_names), len(mask)))
    if not np.all(_isfinite(input)):
      raise ValueError("Only finite values are allowed in inputs vector, got %s." % str(input))

    hash = np.array(input, copy=False).tobytes()
    self._cache[hash] = self._size
    if len(self._cache) > self._cache_size:
      self._cache.popitem(False)
    for i, name in enumerate(self.input_names):
      self._data[name].append(input[i])
    for name, value, calculated in zip(self.output_names, output, mask):
      self._data[name].append(value if calculated else _NONE)
    self._size += 1

  def _update(self, index, output, mask=None, sparse=False):
    if output is None:
      return
    if mask is None:
      mask = np.ones_like(self.output_names, dtype=bool)

    if index < 0 or index >= self._size:
      raise ValueError("Wrong index of evaluation history item for update. Expected index in range [0, %d), got %d." % (self._size, index))
    if sparse:
      if len(output) != len(mask):
        raise ValueError("Wrong size of sparse outputs mask. Expected %d, got %d." % (len(output), len(mask)))
      if any(output_i < 0 or output_i >= len(self.output_names) for output_i in mask):
        raise ValueError("Wrong index in sparse outputs mask. Expected index in range [0, %d), got %d." % (len(self.output_names), index))
      values = [(self.output_names[m], output[_]) for _, m in enumerate(mask)]
    else:
      if len(output) != len(self.output_names):
        raise ValueError("Wrong size of outputs vector. Expected %d, got %d." % (len(self.output_names), len(output)))
      if len(mask) != len(self.output_names):
        raise ValueError("Wrong size of outputs mask. Expected %d, got %d." % (len(self.output_names), len(mask)))
      values = [(self.output_names[_], output[_]) for _, m in enumerate(mask) if m]

    for name, value in values:
      if _isfinite(self._data[name][index]) and _isfinite(value):
        # Cumulative average
        n = self._n_values.setdefault((name, index), 1)
        value = float(n * self._data[name][index] + value) / (n + 1)
        self._n_values[(name, index)] += 1
      self._data[name][index] = value

  def register(self, index, input, output=None, mask=None):
    if index is None:
      # No such input in history
      self._append(input, output, mask)
      return self._size - 1
    else:
      # Update existing record with newly calculated values
      self._update(index, output, mask)
      return index

  def get_output(self, index, mask=None):
    if mask is None:
      mask = np.ones_like(self.output_names, dtype=bool)
    elif len(mask) != len(self.output_names):
      raise ValueError("Wrong size of outputs mask. Expected %d, got %d." % (len(self.output_names), len(mask)))
    if index is None:
      return np.array([_NONE for _ in np.arange(sum(mask))])
    else:
      if index < 0 or index >= self._size:
        raise ValueError("Wrong index of evaluation history item for outputs request. Expected index in range [0, %d), got %d." % (self._size, index))
      return np.array([self._data[name][index] for name, m in zip(self.output_names, mask) if m])

  def find(self, input):
    if len(input) != len(self.input_names):
      raise ValueError("Wrong size of inputs vector. Expected %d, got %d." % (len(self.input_names), len(input)))
    if not np.all(_isfinite(input)):
      raise ValueError("Only finite values are allowed in inputs vector, got %s." % str(input))
    index = None
    hash = np.array(input, copy=False).tobytes()
    if hash in self._cache:
      self.n_cache_hits += 1
      index = self._cache[hash]
    elif self._size > 0:
      lookup = self._size if self._lookup_size == 0 else min(self._lookup_size, self._size)
      lookup_mask = np.ones(lookup, dtype=bool)
      # Precision is taken in such way that all points outside are certainly not equal to the given point (w.r.t precision).
      precision = _Archive.PRECISION * (1 + np.amax(np.abs(input)))
      for i, name in enumerate(self.input_names):
        lookup_inputs = np.array(self._data[name][-lookup:])
        submask = np.abs(lookup_inputs[lookup_mask] - input[i]) <= precision
        lookup_mask[lookup_mask] *= submask
        if np.sum(submask) < 2:
          break
      for candidate_index in np.where(lookup_mask)[0]:
        candidate_index = self._size - lookup + candidate_index
        if self._is_equal(candidate_index, input):
          index = candidate_index
          self._cache[hash] = index
          if len(self._cache) > self._cache_size:
            self._cache.popitem(False)
          self.n_history_hits += 1
          break
    return index

  def merge(self, names=None):
    if names is None:
      names = self.names
    else:
      names = np.atleast_1d(names).astype(str)
      for name in names:
        if name not in self.names:
          raise ValueError("Unknown name %s, expected one of %s." % (name, str(self.names)))
    return np.vstack([self._data[_] for _ in names]).T if len(names) else np.array([])


class CachedResponses(object):

  def __init__(self, archive, problem, mask, **kwargs):
    self.archive = archive
    self.problem = problem
    if len(mask) != problem.size_full():
      raise ValueError("Wrong size of responses mask. Expected %d, got %d." % (problem.size_full(), len(mask)))
    self.mask = np.array(mask, dtype=bool)
    self.catvars = kwargs.get('catvars', {})
    self.linear_responses = set()
    self.linear_responses_weights = {}  # category -> response index -> weights
    self.n_category_hits = {}
    self._n_blackbox_calls = 0
    self._budget = None

  def set_budget(self, budget):
    self._budget = budget

  def set_linear_builder(self, linear_builder):
    self.linear_builder = linear_builder
    for i in np.arange(self.problem.size_full()):
      elem_i = self.problem.size_x() + i
      linearity = self.problem.elements_hint(elem_i, "@GTOpt/LinearityType") or "Generic"
      if linearity.lower() == "linear":
        self.linear_responses.add(i)
        if self.mask[i]:  # Only responses that to be calculated
          self.linear_responses_weights.setdefault(None, {})[i] = []
          weights = self.problem.elements_hint(elem_i, "@GTOpt/LinearParameterVector")
          if weights is not None and len(weights):
            self.linear_responses_weights[None][i] = weights

  def _exclude_linear_mask(self, inputs):
    calc_mask = np.repeat([self.mask], len(inputs), axis=0)

    categories = [None]
    cat_idx = sorted(self.catvars)
    if cat_idx:
      cat_inputs = np.unique(inputs[:, cat_idx], axis=0)
      categories = [tuple(_) for _ in cat_inputs]

    categories_to_restore = []
    category_mask = np.ones(len(inputs), dtype=bool)
    for category in categories:
      if category is not None:
        self.n_category_hits.setdefault(category, 0)
        self.n_category_hits[category] += 1
        if self.n_category_hits[category] <= 1:
          continue
      if category not in self.linear_responses_weights:
        categories_to_restore.append(category)
        continue
      responses_weights = self.linear_responses_weights[category]
      if any(not len(_) for _ in responses_weights.values()):
        # Weights of some linear outputs are not known yet in this category
        categories_to_restore.append(category)
      elif responses_weights:
        # The dict may be empty e.g. if approximation failed for all the linear responses
        known_outputs = list(self.linear_responses_weights[category])
        if category is not None:
          category_mask = np.all(inputs[:, cat_idx] == category, axis=1)
        # Disable calculation of linear outputs with known weights
        calc_mask[np.ix_(category_mask, known_outputs)] = False

    if categories_to_restore:
      categories = categories_to_restore
    else:
      return calc_mask

    size_x, size_f, size_c = self.problem.size_x(), self.problem.size_f(), self.problem.size_c()

    for category in categories:
      responses_weights = self.linear_responses_weights.setdefault(category, self.linear_responses_weights[None].copy())

      vars_hints = [{} for _ in range(size_x)]  # [{}]*size_x references to the same dict
      objs_hints = [{} for _ in range(size_f)]
      cons_hints = [{} for _ in range(size_c)]

      if category is not None:
        for var_i, var_value in zip(cat_idx, category):
          vars_hints[var_i]["@GT/FixedValue"] = var_value

      for resp_i in self.linear_responses:
        category_hints = objs_hints[resp_i] if resp_i < size_f else cons_hints[resp_i - size_f]
        if resp_i in responses_weights:
          # Never use whole individual budget since if approximation is failed we are out of budget for that response
          category_hints["@GT/EvaluationLimit"] = "Auto"
          category_hints["@GTOpt/LinearParameterVector"] = responses_weights[resp_i]
        else:
          # Disable linear reconstruction of responses that are not requested (or failed before and deleted from the dictionary)
          category_hints["@GTOpt/LinearityType"] = "Generic"

      with self.problem._solve_as_subproblem(vars_hints, objs_hints, cons_hints, doe_mode=False):
        sample_x = self.archive.merge(self.problem.variables_names())
        sample_f, sample_c = None, None
        if np.any(self.mask[:self.problem.size_f()]):
          sample_f = self.archive.merge(self.problem.objectives_names())
        if np.any(self.mask[self.problem.size_f():]):
          sample_c = self.archive.merge(self.problem.constraints_names())
        if category is not None:
          category_mask = np.all(sample_x[:, cat_idx] == category, axis=1)
          sample_x = sample_x[category_mask]
          if sample_f is not None:
            sample_f = sample_f[category_mask]
          if sample_c is not None:
            sample_c = sample_c[category_mask]
        hints, evaluations = self.linear_builder(problem=self.problem, sample_x=sample_x, sample_f=sample_f, sample_c=sample_c)
        # We can not suggest the new points to the optimizer, since if there are many categorical variables,
        # only those suggested points are going to be calculated (suggested points have higher priority).
        for input, output, mask in zip(*evaluations):
          index = self.archive.find(input)
          self.archive.register(index, input, output, mask)
        category_mask = slice(0, len(inputs))
        if category is not None:
          category_mask = np.all(inputs[:, cat_idx] == category, axis=1)
        for resp_i in list(responses_weights):
          weights = hints[resp_i].get("@GTOpt/LinearParameterVector")
          if weights is not None and len(weights):
            responses_weights[resp_i] = weights
          # Note that weights might be set by user
          if len(responses_weights[resp_i]):
            # Disable calculation of linear outputs with known weights
            calc_mask[category_mask, resp_i] = False
          else:
            # Was not set by user and failed to approximate so dont try again
            del responses_weights[resp_i]

    return calc_mask

  def _evaluate_linear(self, inputs, outputs, archive_idx):
    outputs_idx = np.where(self.mask)[0].tolist()
    is_calculated = np.zeros(len(inputs), dtype=bool)
    category = None
    category_mask = ~is_calculated
    for i, input in enumerate(inputs):
      if np.all(is_calculated[i:]):
        break
      elif is_calculated[i]:
        continue
      if self.catvars:
        cat_idx = sorted(self.catvars)
        category = tuple(input[cat_idx])
        category_mask = np.all(inputs[:, cat_idx] == category, axis=1)
      if category is not None and self.n_category_hits[category] <= 1:
        is_calculated[category_mask] = True
        continue
      for resp_i, weights in self.linear_responses_weights[category].items():
        output_i = outputs_idx.index(resp_i)
        calc_mask = category_mask * (_NONE == outputs[:, output_i])
        if np.any(calc_mask):
          outputs[calc_mask, output_i] = np.sum(inputs[calc_mask] * weights[:-1], axis=1) + weights[-1]
          for _ in np.where(calc_mask)[0]:
            self.archive._update(archive_idx[_], outputs[_, [output_i]], [resp_i], sparse=True)
      is_calculated[category_mask] = True
    return outputs

  def _evaluate(self, input):
    return self._evaluate_batch([input])[0]

  def _evaluate_batch(self, inputs):
    if self._budget is not None and self._n_blackbox_calls >= self._budget:
      raise errors.NevergradEarlyStopping("Budget limit reached")
    inputs = np.array(inputs)
    if inputs.ndim != 2 or inputs.shape[1] != self.problem.size_x():
      raise ValueError("Wrong shape of batch inputs. Expected matrix of shape (n x %d), got %s." % (self.problem.size_x(), str(inputs.shape)))
    batch_size = inputs.shape[0]
    calc_mask = np.repeat([self.mask], batch_size, axis=0)
    archive_idx = np.empty(batch_size, dtype=object)
    for i in range(batch_size):
      archive_idx[i] = self.archive.find(inputs[i])
      # Add point to archive so that it is available when restoring linear responses
      archive_idx[i] = self.archive.register(archive_idx[i], inputs[i])
      # Request only unknown values
      output = self.archive.get_output(archive_idx[i])
      calc_mask[i] *= (_NONE == output)
    if self.linear_responses_weights:
      # Do not request linear responses that were approximated
      calc_mask *= self._exclude_linear_mask(inputs)

    # Do not request inputs that have already been calculated
    new_inputs_mask = np.any(calc_mask, axis=1)
    # Do not request the same inputs multiple times (remove duplicates from the batch)
    unique_archive_idx = set()
    for i in np.argwhere(new_inputs_mask).flatten():
      if archive_idx[i] in unique_archive_idx:
        new_inputs_mask[i] = False
      else:
        unique_archive_idx.add(archive_idx[i])

    batch_size = sum(new_inputs_mask)
    self._n_blackbox_calls += batch_size
    calc_inputs = inputs[new_inputs_mask]
    calc_mask = calc_mask[new_inputs_mask]
    calc_archive_idx = archive_idx[new_inputs_mask]
    if calc_inputs.size:
      # Use private `_evaluate` method to track the optimization history for History.csv.
      new_outputs, new_masks = self.problem._evaluate(calc_inputs, calc_mask, timecheck=None)
      new_outputs = np.array(new_outputs, dtype=float)
      new_masks = np.array(new_masks, dtype=bool)
      if new_outputs.shape != (batch_size, self.problem.size_full()):
        raise ValueError("Wrong shape of evaluated outputs vector. Expected %s, got %s." % (str((batch_size, self.problem.size_full())), str(new_outputs.shape)))
      if new_masks.shape != (batch_size, self.problem.size_full()):
        raise ValueError("Wrong shape of masks of evaluated outputs vector. Expected %s, got %s." % (str((batch_size, self.problem.size_full())), str(new_masks.shape)))
      for i, archive_index in enumerate(calc_archive_idx):
        self.archive._update(archive_index, new_outputs[i], new_masks[i])
    outputs = np.array([self.archive.get_output(_, self.mask) for _ in archive_idx])
    if self.linear_responses_weights:
      outputs = self._evaluate_linear(inputs, outputs, archive_idx)
    return outputs

  def _evaluate_from_cache(self, input):
    # Either get the whole output from cache or do nothing
    input = np.array(input)
    if input.ndim != 1 or input.shape[0] != self.problem.size_x():
      raise ValueError("Wrong shape of input vector. Expected vector of size %d, got shape %s." % (self.problem.size_x(), str(input.shape)))
    archive_index = self.archive.find(input)
    if archive_index is None:
      return None
    output = self.archive.get_output(archive_index, self.mask)
    # Return the value only if all the required values are known hence
    # the blackbox should not be called for that point
    if np.any(_NONE == output):
      return None
    return output

class Objectives(CachedResponses):

  def __init__(self, archive, problem, **kwargs):
    self.coeffs = []
    self.min_evaluation_limit = np.inf
    mask = np.zeros(problem.size_full(), dtype=bool)
    for i in range(problem.size_f()):
      objective_type = problem.elements_hint(problem.size_x() + i, "@GT/ObjectiveType")
      objective_type = 'minimize' if objective_type is None else objective_type.lower()
      evaluation_limit = problem.elements_hint(problem.size_x() + i, "@GT/EvaluationLimit")
      evaluation_limit = problem._parse_evaluations_limit(evaluation_limit)
      if objective_type in ('minimize', 'maximize'):
        self.coeffs.append(1 if objective_type == "minimize" else -1)
        mask[i] = True
        if evaluation_limit == 0:
          raise ValueError("One of optimization objectives has zero evaluation limit")
        elif evaluation_limit > 0:
          self.min_evaluation_limit = min(self.min_evaluation_limit, evaluation_limit)
    super(Objectives, self).__init__(archive, problem, mask, **kwargs)

  def __call__(self, *args):
    values = self._evaluate(input=args)
    return np.multiply(values, self.coeffs).tolist()

  def calc_from_cache(self, *args):
    values = self._evaluate_from_cache(input=args)
    if values is None:
      return None
    return np.multiply(values, self.coeffs).tolist()

  def calc_batch(self, *args):
    batch_values = self._evaluate_batch(inputs=np.vstack(args).T)
    return np.multiply(batch_values, self.coeffs).tolist()

  @property
  def n_objectives(self):
    return np.sum(self.mask)


class Constraints(CachedResponses):

  NG_MAX_VALUE = 4.9e20  # finite value according to NG is < 5e20

  def __init__(self, archive, problem, tolerance=1.e-5, cache_size=100, **kwargs):
    self.bounds = problem.constraints_bounds()
    self.tolerance = tolerance
    self._cache = OrderedDict()  # binary(x) -> violation
    self._cache_size = cache_size
    self.n_cache_hits = 0
    self.min_evaluation_limit = np.inf
    mask = np.zeros(problem.size_full(), dtype=bool)
    for i in range(problem.size_c()):
      if not _isfinite(self.bounds[0][i]) and not _isfinite(self.bounds[1][i]):
        raise ValueError("Unbounded constraints are not supported")
      output_index = problem.size_f() + i
      evaluation_limit = problem.elements_hint(problem.size_x() + output_index, "@GT/EvaluationLimit")
      evaluation_limit = problem._parse_evaluations_limit(evaluation_limit)
      mask[output_index] = evaluation_limit != 0
      if evaluation_limit > 0:
        self.min_evaluation_limit = min(self.min_evaluation_limit, evaluation_limit)
    super(Constraints, self).__init__(archive, problem, mask, **kwargs)

  def _calc_batch_violations(self, batch_values):
    unknown_idx = []
    unknown_hashes = []
    batch_violations = np.empty(len(batch_values), dtype=float)
    for i, values in enumerate(batch_values):
      hash = np.array(values, copy=False).tobytes()
      if hash in self._cache:
        self.n_cache_hits += 1
        batch_violations[i] = self._cache[hash]
      else:
        unknown_idx.append(i)
        unknown_hashes.append(hash)
    if unknown_idx:
      mask_c = self.mask[self.problem.size_f():]
      # Fill N/A values if one of constraints has no evaluation limit.
      # No that initial sample points may include values of such constraints.
      if not all(mask_c) and batch_values.shape[1] < self.problem.size_c():
        batch_values_fill_na = np.empty((len(batch_values), self.problem.size_c()), dtype=float)
        batch_values_fill_na[:, mask_c] = batch_values
        batch_values_fill_na[:, ~mask_c] = _NONE
        batch_values = batch_values_fill_na
      violations, _ = self.problem._evaluate_psi(batch_values[unknown_idx], self.tolerance)
      violations[np.isnan(violations)] = Constraints.NG_MAX_VALUE
      violations[violations > Constraints.NG_MAX_VALUE] = Constraints.NG_MAX_VALUE
      violations[violations < -Constraints.NG_MAX_VALUE] = -Constraints.NG_MAX_VALUE
      # Last values is the max violation (might be nan as well)
      violations = violations[:, -1]
      for i, hash, violation in zip(unknown_idx, unknown_hashes, violations):
        self._cache[hash] = batch_violations[i] = violation
        if len(self._cache) > self._cache_size:
          self._cache.popitem(False)
    return batch_violations

  def __call__(self, args_kwargs):
    input = args_kwargs[0]  # we do not use named parameters, just args
    value = self._evaluate(input=input)
    violation = self._calc_batch_violations(np.atleast_2d(value))[0]
    return violation

  def calc_from_cache(self, args_kwargs):
    input = args_kwargs[0]  # we do not use named parameters, just args
    value = self._evaluate_from_cache(input=input)
    if value is None:
      return None
    violation = self._calc_batch_violations(np.atleast_2d(value))[0]
    return violation

  def calc_batch(self, args_kwargs):
    inputs = [_[0] for _ in args_kwargs]  # we do not use named parameters, just args
    batch_values = self._evaluate_batch(inputs=inputs)
    batch_violations = self._calc_batch_violations(batch_values)
    return batch_violations


class ObjectivesCSP(Constraints):

  def __init__(self, archive, problem, tolerance=1.e-5, csp_objective_type=None, csp_stop_on_feasible=True, cache_size=100, **kwargs):
    super(ObjectivesCSP, self).__init__(archive, problem, tolerance, cache_size, **kwargs)
    lb, ub = np.array(problem.variables_bounds())
    self._init = problem.initial_guess()
    if self._init is None:
      if csp_objective_type is None:
        csp_objective_type = "Psi"
      if csp_objective_type != "Psi":
        raise ValueError("CSP objective type `%s` requires initial guess" % csp_objective_type)
    elif np.isfinite(lb).all() and np.isfinite(ub).all():
      if csp_objective_type is None:
        csp_objective_type = "PsiDistanceNormed"
    else:
      if csp_objective_type is None:
        csp_objective_type = "PsiDistanceInverse"
      if csp_objective_type != "PsiDistanceInverse":
        raise ValueError("CSP objective type `%s` requires bounds of variables" % csp_objective_type)

    if csp_objective_type == "Psi":
      self._calc_objective = lambda inputs: self._max_psi(inputs)
      self._n_objectives = 1
    elif csp_objective_type == "PsiDistanceNormed":
      max_vector = np.maximum(self._init - lb, ub - self._init)
      max_dist = max(1, np.hypot.reduce(max_vector))
      self._calc_objective = lambda inputs: self._max_psi_distance_normed(inputs, max_dist)
      self._n_objectives = 1
    elif csp_objective_type == "PsiDistanceInverse":
      self._calc_objective = lambda inputs: self._max_psi_distance_inverse(inputs)
      self._n_objectives = 1
    else:
      known_types = ", ".join(["Psi", "PsiDistanceNormed", "PsiDistanceInverse"])
      raise ValueError("Unknown CSP objective type `%s`, expencted one of: %s" % (csp_objective_type, known_types))
    self.csp_objective_type = csp_objective_type
    self.csp_stop_on_feasible = csp_stop_on_feasible
    self.feasible_found = False

  def _distance(self, inputs):
    return np.hypot.reduce(self._init - inputs, axis=1)

  def _max_psi(self, inputs):
    batch_values = self._evaluate_batch(inputs=inputs)
    return self._calc_batch_violations(batch_values=batch_values)

  def _max_psi_distance_normed(self, inputs, max_dist):
    if self.csp_stop_on_feasible and self.feasible_found:
      raise errors.NevergradEarlyStopping("Feasible point found")
    # Set constraint violation to 0 in feasible area
    batch_violations = self._max_psi(inputs=inputs)
    feasible_idx = batch_violations <= 0
    if np.any(feasible_idx):
      self.feasible_found = True
      # Replace 0 values in feasible area with normed to [0, 1] distance to initial guess
      batch_violations[feasible_idx] = -1.0 + self._distance(inputs[feasible_idx]) / max_dist
    return batch_violations

  def _max_psi_distance_inverse(self, inputs):
    if self.csp_stop_on_feasible and self.feasible_found:
      raise errors.NevergradEarlyStopping("Feasible point found")
    # Set constraint violation to 0 in feasible area
    batch_violations = self._max_psi(inputs=inputs)
    feasible_idx = batch_violations <= 0
    if np.any(feasible_idx):
      self.feasible_found = True
      # Replace 0 values in feasible area with inverse distance to initial guess
      batch_violations[feasible_idx] = max(-self.NG_MAX_VALUE, -1.0 / self._distance(inputs[feasible_idx]))
    return batch_violations

  def __call__(self, *args):
    return self._calc_objective(inputs=np.atleast_2d(args))[0]

  def calc_batch(self, *args):
    return self._calc_objective(inputs=np.vstack(args).T)

  @property
  def n_objectives(self):
    return self._n_objectives


class _SnapshotFactory(_SolutionSnapshotFactory):

  def __init__(self, archive, *args, **kwargs):
    super(_SnapshotFactory, self).__init__(*args, **kwargs)
    self._archive = archive
    self._archive_size = 0

  def snapshot(self, final_result):
    if self._last_snapshot is not None and self._archive_size == self._archive.size:
      return self._last_snapshot

    self._archive_size = self._archive.size

    try:
      designs_table = self._archive.merge()
      status_initial = np.zeros(designs_table.shape[0], dtype=int)
      if not designs_table.size:
        # This must be the first call
        return self._make_snapshot(designs=designs_table,
                                   status_initial=status_initial,
                                   status_feasibility=status_initial,
                                   status_optimality=status_initial)

      status_initial.fill(_SolutionSnapshot._UNDEFINED)
      status_initial[:self._archive.init_size] = _SolutionSnapshot._INITIAL
      status_feasibility = self._status_feasibility(design=designs_table, final_result=final_result)
      status_optimality = self._status_optimality(design=designs_table, status_feasibility=status_feasibility, final_result=final_result)
      return self._make_snapshot(designs=designs_table,
                                 status_initial=status_initial,
                                 status_feasibility=status_feasibility,
                                 status_optimality=status_optimality)
    except:
      pass

    return None


class _ResultFactory(object):
  def __init__(self, solver, problem, archive):
    self._solver = solver
    self._problem = problem
    self._archive = archive
    self._last_result = None
    self._last_state = ()

  def result(self, status, intermediate_result):
    current_state = (self._archive.size, status.id, intermediate_result)
    if self._last_result is not None and current_state == self._last_state:
      return self._last_result
    self._last_state = current_state

    size_x = self._problem.size_x()
    size_f = self._problem.size_f()
    size_c = self._problem.size_c()

    current_options = self._solver.options.values
    constraints_tol = float(self._solver.options.get('GTOpt/ConstraintsTolerance'))
    info = {
      "Solver": {
          "Buildstamp": buildinfo.buildinfo().get("Build", {}).get("Stamp", 'version=' + str(__version__) + ';'),
          "Number of variables": size_x,
          "Number of stochastic variables": 0,
          "Number of objectives": size_f,
          "Number of constraints": size_c,
          "Objectives gradients": False,
          "Constraints gradients": False,
          "Objectives gradients analytical": False,
          "Constraints gradients analytical": False,
          "Options" : dict((k, current_options[k]) for k in current_options if not k.startswith("//")),
      }
    }

    sample = self._archive.merge()
    n_init = self._archive.init_size
    n_total = self._archive.size

    fields, base_offset = [("x", slice(0, size_x))], size_x
    base_offset = _append_field_spec(fields, base_offset, "f", size_f)
    base_offset = _append_field_spec(fields, base_offset, "c", size_c)
    solutions_subsets = {"new": slice(n_init, n_total),
                         "auto": slice(0, n_total),
                         "initial": slice(0, n_init)}

    designs = _postprocess_designs(problem=self._problem,
                                   all_designs=sample,
                                   n_initial=n_init,
                                   constraints_tol=constraints_tol)

    result = Result(status=status,
                    info=info,
                    solutions=sample,
                    fields=dict(fields),
                    problem=_weakref.ref(self._problem),
                    designs=designs,
                    solutions_subsets=solutions_subsets,
                    finalize=False)

    result._finalize(problem=self._problem,
                     auto_objective_type="Minimize",
                     options=current_options,
                     logger=self._solver._get_logger(),
                     intermediate_result=intermediate_result)

    self._last_result = result
    self._last_archive_size = self._archive.size
    return result


class Watcher:
  def __init__(self, solver, problem, archive, call_interval=3):
    self._archive = archive
    self._previous_best = None
    self._call_interval = call_interval
    self._next_call_time = time.time() + self._call_interval
    self._user_watcher = solver._get_watcher()
    self._log = solver._log
    self._result_factory = _ResultFactory(
      solver=solver,
      problem=problem,
      archive=archive,
    )
    self._snapshot_factory = _SnapshotFactory(
      archive=archive,
      generator=solver,
      problem=problem,
      watcher=lambda msg=None: True,
      auto_objective_type="minimize",
    )
    if len(self._archive.names) != self._snapshot_factory._designs_width - 1:
      self._log(LogLevel.DEBUG, "WARN: Wrong shape of history matrix for intermediate result %d!=%d" % (len(self._archive.names), self._snapshot_factory._designs_width - 1))

    self.keep_going = True

  def __call__(self, ng_optimizer, *args, **kwargs):
    if time.time() > self._next_call_time and self.keep_going:

      best_value = None
      if ng_optimizer.num_objectives == 1:
        loss = ng_optimizer.provide_recommendation().loss
        best_value = np.array([loss]) if loss is not None else None
      elif ng_optimizer.num_objectives > 1:
        best_value = np.array([_.loss for _ in ng_optimizer.pareto_front()])

      self.keep_going = self._call_user_watcher(best_value)
      self._next_call_time = time.time() + self._call_interval

    if not self.keep_going:
      # We can only stop normally on `ask` callback when no args set.
      # Values of parameters and loss are only set on `tell` callback.
      if not args and not kwargs:
        self._log(LogLevel.DEBUG, "Optimization process stopped by watcher")
        raise errors.NevergradEarlyStopping("Stopped by watcher")

  def _call_user_watcher(self, best_value, status=IN_PROGRESS, final_result=False):
    if self._user_watcher is None:
      return True

    result_updated = False
    if best_value is not None:
      if self._previous_best is None or len(self._previous_best) != len(best_value):
        self._previous_best = best_value
        result_updated = True
      else:
        diff = np.abs(np.subtract(self._previous_best, best_value))
        if np.any(diff > 1e-10):
          self._previous_best = best_value
          result_updated = True

    lazy_result = _DetachableSingleCallableRef(
      callable=self._result_factory.result,
      status=status,
      intermediate_result=True,  # Never evaluate responses from watcher call
    )
    lazy_snapshot = _DetachableSingleCallableRef(
      callable=self._snapshot_factory.snapshot,
      final_result=final_result
    )
    return self._user_watcher({
      "ResultUpdated": result_updated if not final_result else True,
      "RequestIntermediateResult": lazy_result,
      "RequestIntermediateSnapshot": lazy_snapshot,
    })


def show_warning(message, category, filename, lineno, file=None, line=None, solver=None):
  if solver is not None:
    solver._log(LogLevel.WARN, warnings.formatwarning(message, category, filename, lineno))


class LogHandler(logging.Handler):
  def __init__(self, solver):
    super(LogHandler, self).__init__()
    self.solver = solver

  def emit(self, record):
    msg = self.format(record)
    if record.levelno <= logging.DEBUG:
      self.solver._log(LogLevel.DEBUG, msg)
    elif record.levelno == logging.INFO:
      self.solver._log(LogLevel.INFO, msg)
    elif record.levelno == logging.WARN:
      self.solver._log(LogLevel.WARN, msg)
    elif record.levelno >= logging.ERROR:
      self.solver._log(LogLevel.ERROR, msg)


def collect_parameters(problem):
  catvars = {}
  parameters = []
  effective_dim = 0
  initial_guess = problem.initial_guess()
  for i in range(problem.size_x()):
    bound = problem.variables_bounds(i)
    variable_type = problem.elements_hint(i, "@GT/VariableType")
    fixed_value = problem.elements_hint(i, "@GT/FixedValue")
    variable_type = "continuous" if variable_type is None else variable_type.lower()
    if fixed_value is not None:
      parameter = float(fixed_value)
    elif len(bound) == 1 or np.all(bound[0] == bound[1:]):
      parameter = float(bound[0])
    elif variable_type == "continuous" or variable_type == "integer":
      effective_dim += 1
      bound = bound.astype(object)
      bound[~_isfinite(bound)] = None
      # Initial guess is already in bounds and rounded for integer variables
      init = None if initial_guess is None else initial_guess[i]
      parameter = ng.p.Scalar(init=init, lower=bound[0], upper=bound[1])
      if variable_type == "integer":
        parameter = parameter.set_integer_casting()
    elif variable_type == "stepped" or variable_type == "discrete":
      effective_dim += 1
      parameter = ng.p.TransitionChoice(choices=bound)
    elif variable_type == "categorical":
      catvars[i] = bound
      effective_dim += 1
      parameter = ng.p.Choice(choices=bound)
    parameters.append(parameter)
  return parameters, catvars, effective_dim


def estimate_budget(solver, problem, effective_dim, catvars):
  budget = int(solver.options.get("GTOpt/MaximumIterations")) or None
  batch_size = max(int(solver.options.get("GTOpt/BatchSize")), 1)
  responses_scalability = int(solver.options.get("GTOpt/ResponsesScalability"))
  csp_objective_type = solver.options.values.get("/GTOpt/Nevergrad/CSPObjectiveType")
  csp_stop_on_feasible = solver.options.values.get("/GTOpt/Nevergrad/CSPStopOnFeasible")
  n_categories, n_categories_guess = count_categorical_values(catvars)

  objectives = Objectives(archive=None, problem=problem, catvars=catvars)
  constraints = Constraints(archive=None, problem=problem, catvars=catvars)
  has_bb_objectives = np.any(objectives.mask)
  has_bb_constraints = np.any(constraints.mask)
  if not has_bb_objectives:
    if has_bb_constraints:
      # Switch to constraint satisfaction problem
      objectives = ObjectivesCSP(archive=None, problem=problem, csp_objective_type=csp_objective_type, csp_stop_on_feasible=csp_stop_on_feasible, catvars=catvars)
    else:
      raise ValueError("At least one objective or constraint with non-zero evaluation limit should be set")

  budget_message = ""

  if budget is None:
    budget = max(100, min(10000, n_categories_guess * 10 * effective_dim ** 2))
    budget = int(np.ceil(budget / 100) * 100)
    budget_message += "Setting automatic budget for objectives to %d \n" % budget
  if budget > objectives.min_evaluation_limit:
    budget = objectives.min_evaluation_limit
    budget_message += "Reducing budget up to minimal evaluation limit of objectives %d \n" % budget
  if problem.size_c() and budget > constraints.min_evaluation_limit:
    budget = constraints.min_evaluation_limit
    budget_message += "Reducing budget up to minimal evaluation limit of constraints %d \n" % budget

  if responses_scalability > 1:
    # Validation assures that batch_size >= responses_scalability
    batch_size = batch_size // responses_scalability * responses_scalability

  budget_msg = "%d blackbox calls" % budget
  if responses_scalability > 1:
    budget *= responses_scalability
    budget_msg += " with %d parallel executors or %d evaluations in total" % (responses_scalability, budget)
  if batch_size > 1:
    budget = (budget // batch_size) * batch_size
    budget_msg += " (%d batches of size %d)" % (budget // batch_size, batch_size)
  budget_message += "Final exploration budget: %s\n" % budget_msg

  return budget, budget_message


def count_categorical_values(catvars):
  n_categories = 1
  for levels in catvars.values():
    n_categories *= len(levels)
    # if n_categories is too big then n_categories and n_categories_guess are infinite
    if n_categories > np.iinfo(int).max:
      return np.inf, np.inf
  # We assume that some fraction of categories will not be checked even once.
  n_categories_guess = n_categories / max(1, np.log10(n_categories))
  return n_categories, n_categories_guess


def allow_linear_reconstruction(response_budget, effective_dim, catvars):
  n_categories, n_categories_guess = count_categorical_values(catvars)
  # The more categories there are, the less is the probability to check a category at least twice so that we restore linears for it.
  return (response_budget / n_categories_guess) >= (effective_dim - len(catvars) + 2)


def validate(solver, problem, sample_x=None, sample_f=None, sample_c=None):
  diagnostics = []

  def error(msg):
    diagnostics.append(diagnostic.DiagnosticRecord(diagnostic.DIAGNOSTIC_ERROR, msg))

  def warn(msg):
    diagnostics.append(diagnostic.DiagnosticRecord(diagnostic.DIAGNOSTIC_WARNING, msg))

  def hint(msg):
    diagnostics.append(diagnostic.DiagnosticRecord(diagnostic.DIAGNOSTIC_HINT, msg))

  def misc(msg):
    diagnostics.append(diagnostic.DiagnosticRecord(diagnostic.DIAGNOSTIC_MISC, msg))

  def _loose_version_string(code):
    return ".".join(str(_) for _ in code) if code else "<no version>"

  current_version = _distutils_loose_version(ng.__version__)
  supported_versions = sorted([_distutils_loose_version("0.13.0"), _distutils_loose_version("1.0.1")])
  if current_version < supported_versions[0]:
    error('Nevergrad version %s is not supported! Required version >= %s' % (_loose_version_string(current_version), _loose_version_string(supported_versions[0])))
  elif current_version > supported_versions[-1]:
    warn('Using version of Nevergrad %s that is not officially supported!' % _loose_version_string(current_version))

  if problem.objectives_gradient()[0] or problem.constraints_gradient()[0]:
    error("Nevergrad does not support gradients of objectives and constraints in problem definition")
  if problem.size_nf() or problem.size_nc() or problem.size_s():
    error("Nevergrad does not support stochastic variables in problem definition")

  parameters, catvars, effective_dim = collect_parameters(problem)
  if effective_dim == 0:
    error("At least one (free) design variable should be specified.")

  batch_size = max(int(solver.options.get("GTOpt/BatchSize")), 1)
  responses_scalability = int(solver.options.get("GTOpt/ResponsesScalability"))
  if responses_scalability > batch_size:
    error("Target scalability %d can not be reached with batch size %d." % (responses_scalability, batch_size))

  if problem.size_f() > 5:
    # Nevergrad minimizes hypervolume, which is recalculated with the complexity of O(n^(d-2)*log(n)) each time the Pareto-front is changed.
    # An Improved Dimension-Sweep Algorithm for the Hypervolume Indicator
    # https://ieeexplore.ieee.org/document/1688440
    warn("Too many objectives, low performance expected. The current technique is known to show weak performance in multi-objective problems")

  try:
    budget, budget_message = estimate_budget(solver, problem, effective_dim, catvars)
    hint(budget_message)

    restore_linear = shared.parse_auto_bool(solver.options._get("GTOpt/RestoreAnalyticResponses"), True)
    has_linear_responses = False
    for i in np.arange(problem.size_full()):
      linearity = problem.elements_hint(problem.size_x() + i, "@GTOpt/LinearityType") or "Generic"
      if linearity.lower() == "linear":
        has_linear_responses = True
        break

    if restore_linear and has_linear_responses:
      n_categories, n_categories_guess = count_categorical_values(catvars)
      if not allow_linear_reconstruction(budget, effective_dim, catvars):
        message = "The specified budget %d may be exceeded for linear responses" % budget
        if n_categories > 1 and n_categories < np.inf:
          message += " due to high cardinality %d of categorical space" % n_categories
        warn(message)

  except Exception as ex:
    # Catch errors from objectives and constraints constructors during the budget estimation
    budget = 0
    error(str(ex))

  try:
    sample_x, sample_f, sample_c, output_sample = prepare_samples(problem, sample_x, sample_f, sample_c)
    if sample_x is None:
      if sample_f is not None or sample_c is not None:
        warn("Initial sample is ignored since the input part of the sample is missing")
  except Exception as ex:
    error(str(ex))

  misc(json.dumps({
    "_details": {
      "General": {},
      "Optimization": {
        "N_eval": budget
      }
    }
  }))

  if any(_.severity == diagnostic.DIAGNOSTIC_ERROR for _ in diagnostics):
    status = UNSUPPORTED_PROBLEM
  else:
    status = SUCCESS

  return ValidationResult(status, diagnostics)


def prepare_samples(problem, sample_x, sample_f, sample_c):
  output_sample = None
  if sample_x is not None:
    sample_x = np.atleast_2d(sample_x).astype(float) if np.ndim(sample_x) > 1 else np.array(sample_x, dtype=float).reshape(-1, 1)
    if sample_x.shape[1] != problem.size_x():
      raise ValueError("Wrong number of columns in input part of initial sample. Expected %d, got %d." % (problem.size_x(), sample_x.shape[1]))

    if sample_f is not None or sample_c is not None:
      output_sample = np.empty((sample_x.shape[0], problem.size_full()))

      if sample_f is None:
        output_sample[:, :problem.size_f()] = _NONE
      else:
        sample_f = np.atleast_2d(sample_f).astype(float) if np.ndim(sample_x) > 1 else np.array(sample_x, dtype=float).reshape(-1, 1)
        if sample_f.shape != (sample_x.shape[0], problem.size_f()):
          raise ValueError("Wrong shape of objectives part of initial sample. Expected (%d, %d), got %s." % (sample_x.shape[0], problem.size_f(), str(sample_f.shape)))
        output_sample[:, :problem.size_f()] = sample_f

      if sample_c is None:
        output_sample[:, problem.size_f():] = _NONE
      else:
        sample_c = np.atleast_2d(sample_c).astype(float) if np.ndim(sample_x) > 1 else np.array(sample_x, dtype=float).reshape(-1, 1)
        if sample_c.shape != (sample_x.shape[0], problem.size_c()):
          raise ValueError("Wrong shape of constraints part of initial sample. Expected (%d, %d), got %s." % (sample_x.shape[0], problem.size_c(), str(sample_c.shape)))
        output_sample[:, problem.size_f():] = sample_c

  return sample_x, sample_f, sample_c, output_sample


@_contextlib.contextmanager
def _archived_blackbox(archive, problem):
  original_evaluate = None

  try:
    original_evaluate = problem.evaluate

    def archived_evaluate(queryx, querymask, *args, **kwargs):
      batch_size = len(queryx)
      archive_idx = np.empty(batch_size, dtype=object)
      # TODO exclude linearly interpolated points (use evaluate_from_cache methods)
      for i in range(batch_size):
        archive_idx[i] = archive.find(queryx[i])
        # Add point to archive so that it is available when restoring linear responses
        archive_idx[i] = archive.register(archive_idx[i], queryx[i])
      new_outputs, new_masks = original_evaluate(queryx, querymask, *args, **kwargs)
      new_outputs = np.array(new_outputs, dtype=float)
      new_masks = np.array(new_masks, dtype=bool)
      if new_outputs.shape != (batch_size, problem.size_full()):
        raise ValueError("Wrong shape of evaluated outputs vector. Expected %s, got %s." % (str((batch_size, problem.size_full())), str(new_outputs.shape)))
      if new_masks.shape != (batch_size, problem.size_full()):
        raise ValueError("Wrong shape of masks of evaluated outputs vector. Expected %s, got %s." % (str((batch_size, problem.size_full())), str(new_masks.shape)))
      for i, archive_index in enumerate(archive_idx):
        archive._update(archive_index, new_outputs[i], new_masks[i])
      return new_outputs, new_masks
    problem.evaluate = archived_evaluate
  except:
    pass

  try:
    yield problem
  finally:
    if original_evaluate is not None and problem.evaluate is not original_evaluate:
      problem.evaluate = original_evaluate


def solve(solver, problem, sample_x=None, sample_f=None, sample_c=None):
  solver._log(LogLevel.INFO, "Solving by Nevergrad %s the following %s" % (ng.__version__, str(problem)))

  budget = int(solver.options.get("GTOpt/MaximumIterations")) or None
  seed = int(solver.options.get("GTOpt/Seed")) if shared.parse_auto_bool(solver.options.get("GTOpt/Deterministic"), True) else np.random.randint(1, 65535)
  verbosity = int(shared.parse_auto_bool(solver.options.get("GTOpt/VerboseOutput"), False))
  time_limit = int(solver.options.get("GTOpt/TimeLimit"))
  batch_size = max(int(solver.options.get("GTOpt/BatchSize")), 1)
  responses_scalability = int(solver.options.get("GTOpt/ResponsesScalability"))
  constraints_tolerance = float(solver.options.get('GTOpt/ConstraintsTolerance'))
  restore_linear = shared.parse_auto_bool(solver.options._get("GTOpt/RestoreAnalyticResponses"), True)

  lookup_size = int(solver.options.values.get("/GTOpt/Nevergrad/HistoryLookupSize", 1000))
  cache_size = int(solver.options.values.get("/GTOpt/Nevergrad/HistoryCacheSize", 100))
  verbosity = int(solver.options.values.get("/GTOpt/Nevergrad/Verbosity", verbosity))
  watcher_call_interval = float(solver.options.values.get("/GTOpt/Nevergrad/WatcherCallInterval", 3))
  enable_hypervolume = shared.parse_bool(solver.options.values.get("/GTOpt/Nevergrad/EnableHyperVolume", True))
  set_objectives_number = shared.parse_bool(solver.options.values.get("/GTOpt/Nevergrad/SetNumberOfObjectives", False))  # Changes algorithm selection path, usually selects DE when set
  multiobjective_reference = shared.parse_json(solver.options.values.get("/GTOpt/Nevergrad/MultiobjectiveReference"))
  csp_objective_type = solver.options.values.get("/GTOpt/Nevergrad/CSPObjectiveType")
  csp_stop_on_feasible = shared.parse_bool(solver.options.values.get("/GTOpt/Nevergrad/CSPStopOnFeasible", True))
  n_unique_sampling_attempts = int(solver.options.values.get("/GTOpt/Nevergrad/UniqueSamplingAttempts", 10))

  for msg in validate(solver, problem, sample_x, sample_f, sample_c).details:
    if msg.severity == diagnostic.DIAGNOSTIC_ERROR:
      raise exceptions.InvalidProblemError(msg.message)
    elif msg.severity == diagnostic.DIAGNOSTIC_WARNING:
      solver._log(LogLevel.WARN, msg.message)
    elif msg.severity == diagnostic.DIAGNOSTIC_HINT:
      solver._log(LogLevel.INFO, msg.message)

  parameters, catvars, effective_dim = collect_parameters(problem)

  archive = _Archive(input_names=problem.variables_names(),
                     objective_names=problem.objectives_names(),
                     constraint_names=problem.constraints_names(),
                     lookup_size=lookup_size,
                     cache_size=cache_size)

  objectives = Objectives(archive, problem, catvars=catvars)
  constraints = Constraints(archive, problem, constraints_tolerance, catvars=catvars)
  has_bb_objectives = np.any(objectives.mask)
  has_bb_constraints = np.any(constraints.mask)
  if not has_bb_objectives and has_bb_constraints:
    # Switch to constraint satisfaction problem
    objectives = ObjectivesCSP(archive, problem, constraints_tolerance, csp_objective_type=csp_objective_type, csp_stop_on_feasible=csp_stop_on_feasible, catvars=catvars)
    solver._log(LogLevel.DEBUG, "No objectives set, switching to CSP problem with %s objective" % objectives.csp_objective_type)
  budget, budget_message = estimate_budget(solver, problem, effective_dim, catvars)
  objectives.set_budget(budget)
  constraints.set_budget(budget)

  if restore_linear:
    linear_builder = partial(solver._preprocess_linear_response, mode=api.GTOPT_SOLVE, return_evaluations=True)
    objectives.set_linear_builder(linear_builder)
    constraints.set_linear_builder(linear_builder)

  parametrization = ng.p.Instrumentation(*parameters)
  parametrization.random_state.seed(seed)
  optimizer = BatchOptimizer(parametrization=parametrization,
                             budget=budget,
                             num_workers=batch_size)

  if set_objectives_number:
    optimizer.num_objectives = objectives.n_objectives
  if not enable_hypervolume:
    optimizer._no_hypervolume = True
  if multiobjective_reference:
    optimizer.tell(ng.p.MultiobjectiveReference(), multiobjective_reference)

  sample_x, sample_f, sample_c, output_sample = prepare_samples(problem, sample_x, sample_f, sample_c)
  if sample_x is not None:
    # Round values and mark those that are out of bounds/levels
    sample_x, is_valid = problem._valid_input_points(sample_x, precision=8)
    # Save raw unrounded values to history, otherwise we need to fix archive lookup
    archive.register_initial_sample(input_sample=sample_x, output_sample=output_sample)
    for x_vector in sample_x[is_valid]:
      optimizer.suggest(*x_vector)
      optimizer.budget += 1
  if problem.initial_guess() is not None:
    # In some cases initial guess set by Nevergrad parameters may be ignored
    # (i.g. continuous variable with no bounds) so we explicitly pass it to optimizer
    optimizer.suggest(*problem.initial_guess())
    optimizer.budget += 1

  warnings.showwarning = partial(show_warning, solver=solver)
  redirected_logger = LogHandler(solver)
  logger.addHandler(redirected_logger)
  optimizers.logger.addHandler(redirected_logger)
  progress_callback = None
  try:
    from tqdm import tqdm

    class Log:
      def write(self, msg):
        solver._log(LogLevel.INFO, msg)
      def flush(self):
        pass

    progress_callback = callbacks.ProgressBar()
    progress_callback._progress_bar = tqdm(file=Log(), ascii=True)
    progress_callback._progress_bar.total = optimizer.budget
    optimizer.register_callback("tell", progress_callback)
  except ImportError:
    pass

  batch_functions = {objectives: objectives.calc_batch, constraints: constraints.calc_batch}
  executor = BatchExecutor(batch_functions, num_workers=optimizer.num_workers, batch_timeout_sec=10)

  result_status = SUCCESS
  with shared.sigint_watcher(solver):
    watcher = Watcher(solver=solver, archive=archive, problem=problem, call_interval=watcher_call_interval)
    optimizer.register_callback("ask", watcher)
    optimizer.register_callback("tell", watcher)
    if time_limit:
      optimizer.register_callback("ask", callbacks.EarlyStopping.timer(time_limit))

    try:
      # Batch mode is always enabled since in terms of Nevergrad it means
      # to wait for the whole batch to be calculated before generating new points
      optimizer.minimize(objectives,
                         executor=executor,
                         batch_mode=True,
                         verbosity=verbosity,
                         constraint_violation=[constraints] if has_bb_objectives and has_bb_constraints else None,
                         n_unique_sampling_attempts=n_unique_sampling_attempts)
    except errors.NevergradEarlyStopping as ex:
      # Catch early stopping exceptions threw at "tell" stage from response calculation functions,
      # since Nevergrad handles such exceptions only from watcher, i.e. threw at "ask" stage
      solver._log(LogLevel.DEBUG, "Optimization was stopped: %s" % str(ex))

    if progress_callback is not None:
      progress_callback._progress_bar.close()
    if not watcher.keep_going:
      result_status = USER_TERMINATED

    # Since the blackbox is called directly, the values of evaluated responses need
    # to be saved to the archive so that the final result contains the whole sample.
    with _archived_blackbox(archive=archive, problem=problem) as archived_problem:
      result_factory = _ResultFactory(solver=solver, problem=archived_problem, archive=archive)
      result = result_factory.result(status=result_status, intermediate_result=False)

    # In the case of 'user terminated' status it is not allowed to call watcher anymore,
    # so the sigint wrapper will suppress this call and the last snapshot will be
    # inconsistent with the result, which is OK (same as for other p7core techniques).
    watcher._call_user_watcher(best_value=None, status=result_status, final_result=True)
  return result
