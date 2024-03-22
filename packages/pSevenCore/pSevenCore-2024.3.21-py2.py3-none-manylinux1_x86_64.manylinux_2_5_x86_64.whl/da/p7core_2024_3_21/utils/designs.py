#
# coding: utf-8
# Copyright (C) pSeven SAS, 2010-present
#
#

import sys as _sys
import numpy as _numpy

from .. import shared as _shared
from .. import six as _six

def _fill_gaps_and_keep_dups(dataset, key_slice):
  if len(dataset) < 2:
    # degenerated case: single record - there is nothing to merge, return list of rows always
    return dataset

  holes_masks = _shared._find_holes(dataset)
  holes_masks[:, key_slice] = False # ignore holes at keys, we cannot proceed it anyway

  if _numpy.logical_or(holes_masks.all(axis=0), ~holes_masks.any(axis=0)).all():
    # all data columns are either completely known or completely undefined: no chess, no game
    return dataset

  keys = _shared._make_dataset_keys(dataset[:, key_slice])
  order = _shared._lexsort(keys)

  keys = keys[order]
  duplicates = _numpy.equal(keys[:-1], keys[1:]).all(axis=1)
  del keys

  if not duplicates.any():
    # degenerated case: no dup in keys, we cannot fill anything
    return dataset

  original_dataset = dataset
  completely_known = ~holes_masks.any(axis=1)

  def _enumerate_equal_keys_groups():
    first = 0 # note this is index in the order vector
    for i, same_record in enumerate(duplicates):
      # note i is index in the duplicates vector which corresponds to order[1:]
      if not same_record:
        if first < i:
          yield first, (i + 1)
        first = i + 1
    if first < len(order):
      yield first, len(order)

  def _fill_vector_gaps(dataset, source_index, destination_index):
    if completely_known[destination_index]:
      # there is nothing to copy
      return dataset
    elif completely_known[source_index]:
      # simple case
      if dataset is original_dataset:
        dataset = dataset.copy() # copy-on-write
      update_mask = holes_masks[destination_index]
      dataset[destination_index, update_mask] = dataset[source_index, update_mask]
      holes_masks[destination_index].fill(False)
      completely_known[destination_index] = True
      return dataset

    update_mask = _numpy.logical_and(holes_masks[destination_index], ~holes_masks[source_index])
    if update_mask.any():
      if dataset is original_dataset:
        dataset = dataset.copy() # copy-on-write
      dataset[destination_index, update_mask] = dataset[source_index, update_mask]
      holes_masks[destination_index, update_mask] = False
      completely_known[destination_index] = not holes_masks[destination_index].any()
    return dataset

  for first, last in _enumerate_equal_keys_groups():
    baseline_index = order[first]
    if not completely_known[baseline_index]:
      # forward pass: copy from other rows to the first one
      for other_index in order[(first + 1):last]:
        dataset = _fill_vector_gaps(dataset, other_index, baseline_index)
    # backward pass: copy from the first row to others
    for other_index in order[(first + 1):last]:
      dataset = _fill_vector_gaps(dataset, baseline_index, other_index)

  return dataset

def _fill_sliced_sample_gaps(dst_keys, dst_data, src_keys, src_data):
  for dst_index, src_index in _shared._enumerate_equal_keys(dst_keys, src_keys):
    dst_value = dst_data[dst_index]
    # source may contain dups which fills destination, so we must update mask every time
    d_mask = _shared._find_holes(dst_value)
    dst_value[d_mask] = src_data[src_index][d_mask] # copy values from src to the holes in dst

  return dst_data

def _select_unique_nan_mark(keys):
  finfo = _numpy.finfo(float)

  nan_mark = _numpy.nanmax(keys)
  if nan_mark < finfo.max:
    return nan_mark * (1. + finfo.eps)

  nan_mark = _numpy.nanmin(keys)
  if nan_mark > -finfo.max:
    return nan_mark * (1. - finfo.eps)

  nan_mark = _numpy.random.random()
  while (nan_mark == keys).any():
    nan_mark = _numpy.random.random()

  return nan_mark

def _unique_rows_indices(keys):
  # Note lexsort works noticeably faster on the C-ordered data
  nan_mask = _numpy.isnan(keys)
  if nan_mask.any():
    keys = keys.copy()
    keys[nan_mask] = _select_unique_nan_mark(keys)
  keys_order = _shared._lexsort(keys)
  keys = keys[keys_order]

  keys_order = _numpy.hstack(([keys_order[0]], keys_order[1:][_numpy.not_equal(keys[1:], keys[:-1]).any(axis=-1)]))
  keys_order.sort()
  return keys_order

def _select_unique_rows(dataset, keep_n_first):
  if dataset.shape[0] < 2:
    # degenerated case: single record - there is nothing to merge
    return dataset

  keys = _shared._make_dataset_keys(dataset)
  unique_elements = _unique_rows_indices(keys)

  if len(unique_elements) == len(keys):
    return dataset

  if keep_n_first:
    return _numpy.vstack((dataset[:keep_n_first], dataset[unique_elements[unique_elements >= keep_n_first]]))

  return dataset[unique_elements]

def _solutions_to_designs(problem, solutions_table, fields, sample_x, sample_f, sample_c, c_tol):
  input_size = problem.size_x()+problem.size_s()

  initial_sample = _preprocess_initial_sample(problem, sample_x, sample_f, sample_c, None, None)
  n_initial, designs_table = (initial_sample.shape[0], [initial_sample]) if initial_sample is not None else (0, [])

  fields = dict(fields) if fields is not None else {}
  if "x" in fields:
    solutions_sample = _preprocess_initial_sample(problem, solutions_table[:, fields["x"]],
                                                  (solutions_table[:, fields["f"]] if "f" in fields else None),
                                                  (solutions_table[:, fields["c"]] if "c" in fields else None),
                                                  None, None)
    if solutions_sample is not None and solutions_sample.size:
      designs_table.append(solutions_sample)
  designs_table.extend(problem._history_cache)

  if not designs_table:
    return None

  designs_table = _fill_gaps_and_keep_dups(_numpy.vstack(designs_table), slice(0, input_size))
  designs_table = _select_unique_rows(designs_table, n_initial)

  return _postprocess_designs(problem, designs_table, n_initial, c_tol)

def _preprocess_optional_sample(data, n_rows, n_cols, name):
  if data is not None:
    data = _shared.as_matrix(data, shape=(None, n_cols), name=name)
    if not data.size:
      return None # empty matrix (n_cols may be zero)
    elif n_rows and data.shape[0] != n_rows:
      raise ValueError("%s must be either empty or has %d rows (%d rows encountered)!" % (name, n_rows, data.shape[0]))
  return data

def _preprocess_initial_sample(problem, sample_x, sample_f, sample_c, sample_nf, sample_nc, return_slices=False):
  """
  Collect initial sample to a single matrix a la `problem.designs` with `problem._history_fields[1]` columns.

  :param problem: original problem
  :param sample_x: input part (x) of initial sample
  :param sample_f: objective values of initial sample, requires :arg:`sample_x`
  :param sample_c: constraint values of initial sample, requires :arg:`sample_x`
  :param sample_nf: objective value uncertainties of initial sample, requires :arg:`sample_x` and :arg:`sample_f`
  :param sample_nc: constraint value uncertainties of initial sample, requires :arg:`sample_x` and :arg:`sample_c`

  Note designs matrix for :arg:`postprocess_designs` has ``problem.size_x()+problem.size_s()+problem.size_full()`` columns.
  """

  size_x, size_f, size_c, size_nf, size_nc = problem.size_x(), problem.size_f(), problem.size_c(), problem.size_nf(), problem.size_nc()

  input_size = size_x + problem.size_s()
  total_fields = input_size + problem.size_full()

  sample_x = _preprocess_optional_sample(sample_x, None, size_x, name="Input part of initial sample")
  if sample_x is None:
    return (None, []) if return_slices else None

  n_points = sample_x.shape[0]
  sample_f = _preprocess_optional_sample(sample_f, n_points, size_f, name="Responses part of initial sample")
  sample_c = _preprocess_optional_sample(sample_c, n_points, size_c, name="Constraints part of initial sample")
  sample_nf = _preprocess_optional_sample(sample_nf, n_points, size_nf, name="Responses value uncertainties part of initial sample") if sample_f is not None else None
  sample_nc = _preprocess_optional_sample(sample_nc, n_points, size_nc, name="Constraints value uncertainties part of initial sample") if sample_c is not None else None

  slice_x = slice(0, size_x)
  slice_f = slice(input_size, input_size + size_f)
  slice_c = slice(input_size + size_f, input_size + size_f + size_c)
  slice_nf = slice(total_fields - size_nf - size_nc, total_fields - size_nc)
  slice_nc = slice(total_fields - size_nc, total_fields)

  # reshape initial guesses just like problem.history do, except keep it as matrix of floats with _shared.NONE for the holes
  initial_sample = _shared._filled_array((sample_x.shape[0], total_fields), _shared._NONE) # by default the whole initial sample is unknown
  initial_sample[:, slice_x] = sample_x # note stochastic problem is the only case, for which part of input is undefined

  if sample_f is not None:
    initial_sample[:, slice_f] = sample_f
  if sample_c is not None:
    initial_sample[:, slice_c] = sample_c
  if sample_nf is not None:
    initial_sample[:, slice_nf] = sample_nf
  if sample_nc is not None:
    initial_sample[:, slice_nc] = sample_nc

  initial_slices = ("x", slice_x), ("f", slice_f), ("c", slice_c), ("nf", slice_nf), ("nc", slice_nc),
  initial_slices = [(k, v) for k, v in initial_slices if v.stop > v.start]

  problem._refill_from_history(initial_sample, initial_slices) # fill gaps using evaluation history
  problem._refill_analytical_history(history_records=initial_sample, history_fields=initial_slices) # fill known linear dependencies

  # fill gaps and remove possible duplicates from initial sample
  initial_sample = _fill_gaps_and_keep_dups(initial_sample, slice(input_size))
  initial_sample = _select_unique_rows(initial_sample, 0)

  return (initial_sample, initial_slices) if return_slices else initial_sample

def _combine_designs(input_size, designs_a, designs_b):
  if designs_a is None or not designs_a[0].size:
    return designs_b
  elif designs_b is None or not designs_b[0].size:
    return designs_a

  data_a, fields_a, samples_a = designs_a
  data_b, fields_b, samples_b = designs_b

  assert all(fields_a[2][k] == fields_b[2][k] for k in fields_a[2])
  assert all(fields_a[2][k] == fields_b[2][k] for k in fields_b[2])

  initial_a, new_a = data_a[samples_a[1].get("initial", slice(0, 0))], data_a[samples_a[1].get("new", slice(0, 0))]
  initial_b, new_b = data_b[samples_b[1].get("initial", slice(0, 0))], data_b[samples_b[1].get("new", slice(0, 0))]
  input_key = slice(input_size)

  if not initial_a.size:
    new_initial = initial_b
  elif not initial_b.size:
    new_initial = initial_a
  else:
    new_initial = _fill_gaps_and_keep_dups(_numpy.vstack((initial_a, initial_b)), input_key)
    new_initial = _select_unique_rows(new_initial, 0)

  new_designs_table = _fill_gaps_and_keep_dups(_numpy.vstack((new_initial, new_a, new_b)), input_key)
  new_designs_table = _select_unique_rows(new_designs_table, len(new_initial))

  if fields_a[0] != fields_b[0] or fields_a[1] != fields_b[1]:
    # some fields may be disabled due to empty data so we reconstruct basic and extra fields
    n_columns, fields_spec = new_designs_table.shape[1], fields_a[2]
    basic_fields = tuple(sorted([_ for _ in set(tuple(fields_a[0]) + tuple(fields_b[0]))], key=lambda x: fields_spec[x].indices(n_columns)[0]))
    extra_fields = tuple(sorted([_ for _ in set(tuple(fields_a[1]) + tuple(fields_b[1]))], key=lambda x: fields_spec[x].indices(n_columns)[0]))
    new_designs_fields = _filter_designs_fields(new_designs_table, basic_fields, extra_fields, fields_spec)
  else:
    new_designs_fields = fields_a

  new_designs_samples = _configure_designs_samples(len(new_initial), len(new_designs_table))

  return new_designs_table, new_designs_fields, new_designs_samples

def _configure_designs_samples(n_initial, n_total):
  samples = [("all", 0, n_total), ("new", n_initial, n_total), ("initial", 0, n_initial),]
  return (tuple(name for name, start, stop in samples if stop > start),
          dict((name, slice(start, stop)) for name, start, stop in samples),) # note dict contains ALL valid subsamples, including empty

def _filter_designs_fields(designs_table, basic_fields, extra_fields, fields_spec):
  # field filtering is intentionally disabled in version 6.43 (issue #351)
  return basic_fields, extra_fields, fields_spec

def _postprocess_designs(problem, all_designs, n_initial, constraints_tol):
  size_x = problem.size_x()
  input_size = size_x + problem.size_s()
  total_fields = input_size + problem.size_full()
  all_designs = _shared.as_matrix(all_designs, shape=(None, total_fields), detect_none=True)
  n_total = all_designs.shape[0]

  if not n_total:
    return None

  basic_fields, extra_fields = problem._history_fields

  basic_fields = [_ for _ in basic_fields]
  extra_fields = [(_, i) for i, _ in enumerate(extra_fields)] # convert names list to list of (name, index) tuples

  assert len(extra_fields) == total_fields

  for name, start, stop in basic_fields:
    for i in range(start, stop):
      extra_fields[i] = (name + "." + extra_fields[i][0]), extra_fields[i][1]

  size_f, size_c = problem.size_f(), problem.size_c()
  psi, flags = _numpy.empty((n_total, 0)), _numpy.zeros((n_total,), dtype=_numpy.int32)

  if size_c:
    try:
      slice_c = slice(input_size + size_f, input_size + size_f + size_c)
      psi, flags = problem._evaluate_psi(all_designs[:, slice_c], constraints_tol)

      basic_fields.append(("v", total_fields, total_fields + size_c)) # componentwise relative feasibilities
      extra_fields.extend(("v." + name, total_fields + k) for k, name in enumerate(problem.constraints_names()))
      basic_fields.append(("psi", total_fields + size_c, total_fields + size_c + 1)) # maximal relative feasibility
      total_fields += 1 + size_c
    except:
      pass

  extra_fields.append(("flag", total_fields))

  designs_table = _numpy.hstack((all_designs, psi, flags.reshape(-1, 1)))
  designs_fields = _filter_designs_fields(designs_table,
                                          tuple(name for name, start, stop in basic_fields if stop > start),
                                          tuple(name for name, index in extra_fields),
                                          dict([(name, slice(start, stop)) for name, start, stop in basic_fields if stop > start]
                                             + [(name, slice(index, index + 1)) for name, index in extra_fields]),)
  designs_samples = _configure_designs_samples(n_initial, n_total)

  return designs_table, designs_fields, designs_samples

class _SolutionSnapshot(object):
  _UNDEFINED            = 0

  # status & 0x01
  _INITIAL              = 1

  # status & 0x06
  _INFEASIBLE           = 2
  _FEASIBLE             = 4
  _POTENTIALLY_FEASIBLE = 6

  # status & 0x18
  _DOMINATED            = 8
  _OPTIMAL              = 16
  _POTENTIALLY_OPTIMAL  = 24

  _NAMES = {
    _UNDEFINED            : "",
    _INITIAL              : "initial",
    _INFEASIBLE           : "infeasible",
    _FEASIBLE             : "feasible",
    _POTENTIALLY_FEASIBLE : "",
    _DOMINATED            : "",
    _OPTIMAL              : "optimal",
    _POTENTIALLY_OPTIMAL  : "optimal(?)",
    }

  _VALID_STATES = _numpy.array((
    '',                              'initial',                       'infeasible',                    'initial, infeasible',
    'feasible',                      'initial, feasible',             '',                              'initial',
    '',                              'initial',                       'infeasible',                    'initial, infeasible',
    'feasible',                      'initial, feasible',             '',                              'initial',
    'optimal',                       'initial, optimal',              'infeasible, optimal',           'initial, infeasible, optimal',
    'feasible, optimal',             'initial, feasible, optimal',    'optimal',                       'initial, optimal',
    'optimal(?)',                    'initial, optimal(?)',           'infeasible, optimal(?)',        'initial, infeasible, optimal(?)',
    'feasible, optimal(?)',          'initial, feasible, optimal(?)', 'optimal(?)',                    'initial, optimal(?)',
    ))

  def __init__(self, design_columns, designs, status_initial, status_feasibility, status_optimality):
    object.__setattr__(self, 'columns', design_columns)
    object.__setattr__(self, 'design', designs)
    object.__setattr__(self, 'missing', _shared._find_holes(designs))
    object.__setattr__(self, 'initial', status_initial)
    object.__setattr__(self, 'feasibility', status_feasibility)
    object.__setattr__(self, 'optimality', status_optimality)

  def __setattr__(self, *args, **kwargs):
    raise TypeError('Immutable object!')

  def __delattr__(self, *args, **kwargs):
    raise TypeError('Immutable object!')

  def __eq__(self, other):
    if self is other:
      return True
    try:
      if self.columns == other.columns and (self.initial == other.initial).all() \
        and (self.feasibility == other.feasibility).all() and (self.optimality == other.optimality).all()\
        and (self.missing == other.missing).all():
          if self.missing.any():
            return (self.design[~self.missing] == other.design[~self.missing]).all()
          return (self.design == other.design).all()
    except:
      pass
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  def __str__(self):
    stream = _six.moves.StringIO()
    self.pprint(file=stream, max_records=20, max_columns=10)
    return stream.getvalue()

  def pprint(self, file=None, precision=8, max_records=None, max_columns=None):
    if not file:
      file = _sys.stdout

    n_designs, n_columns = len(self.design), len(self.columns)
    format_str = "%%-%ds" % (precision + 5,)
    format_dbl = "%%-%d.%dg" % (precision + 5, precision)

    max_columns = int(max_columns) if max_columns else n_columns
    if max_columns >= n_columns:
      left_columns, right_columns, columns_junction = n_columns, n_columns, ""
    else:
      left_columns = max_columns // 2
      right_columns = n_columns - (max_columns - left_columns)
      columns_junction = " | ... | " if left_columns else "... | "

    file.write("#      | " + " | ".join((format_str % _) for _ in self.columns[:left_columns]) + columns_junction \
                           + " | ".join((format_str % _) for _ in self.columns[right_columns:]) + " | status\n")
    if not n_designs:
      file.write("<no data>\n")
      return

    value_none = format_str % ""

    max_records = int(max_records) if max_records else n_designs
    if max_records >= n_designs:
      head_rows, tail_base = n_designs, n_designs
    else:
      head_rows = max_records // 2
      tail_base = n_designs - (max_records - head_rows)

    status = self.explain_design_mark(self.initial[:head_rows] + self.feasibility[:head_rows] + self.optimality[:head_rows])
    for i, (values, missing, status) in enumerate(zip(self.design[:head_rows], self.missing[:head_rows], status)):
      columns_head = " | ".join((value_none if nope else (format_dbl % val)) for val, nope in zip(values[:left_columns], missing[:left_columns]))
      columns_tail = " | ".join((value_none if nope else (format_dbl % val)) for val, nope in zip(values[right_columns:], missing[right_columns:]))
      file.write(("%-6d | " % (i,)) + columns_head + columns_junction + columns_tail + " | " + status + "\n")

    if tail_base < n_designs:
      value_ellipses = format_str % ("...",)
      file.write("...    | " + " | ".join(value_ellipses for _ in self.columns[:left_columns]) + columns_junction \
                             + " | ".join(value_ellipses for _ in self.columns[right_columns:]) + " | ...\n")

      status = self.explain_design_mark(self.initial[tail_base:] + self.feasibility[tail_base:] + self.optimality[tail_base:])
      for i, (values, missing, status) in enumerate(zip(self.design[tail_base:], self.missing[tail_base:], status)):
        columns_head = " | ".join((value_none if nope else (format_dbl % val)) for val, nope in zip(values[:left_columns], missing[:left_columns]))
        columns_tail = " | ".join((value_none if nope else (format_dbl % val)) for val, nope in zip(values[right_columns:], missing[right_columns:]))
        file.write(("%-6d | " % (tail_base + i,)) + columns_head + columns_junction + columns_tail + " | " + status + "\n")

    if tail_base < n_designs or right_columns < n_columns:
      file.write("\n[%d records x %d columns]\n" % (n_designs, n_columns))

  @staticmethod
  def explain_design_mark(code):
    return _SolutionSnapshot._VALID_STATES[_numpy.bitwise_and(_numpy.array(code, copy=False, dtype=int), 0x1F)]

class _SolutionSnapshotFactoryBase(object):
  def __init__(self, generator, watcher, problem, auto_objective_type):
    self.reset()
    self._user_watcher  = watcher

    if not generator:
      return

    try:
      self._generator = generator
      self._problem = problem
      self._setup_fields()
      self._setup_target_objective(auto_objective_type=str(auto_objective_type).lower())
    except:
      self.reset()


  @property
  def watcher(self):
    return self if self._user_watcher else None

  def _setup_target_objective(self, auto_objective_type):
    size_x, size_f = self._problem.size_x(), self._problem.size_f()
    if not size_f:
      return

    try:
      self._target_objective = [(kind or auto_objective_type).lower() for kind in self._problem.elements_hint(slice(size_x, size_x + size_f), "@GT/ObjectiveType")]
      if "auto" in self._target_objective:
        self._target_objective = [(auto_objective_type if kind == "auto" else kind) for kind in self._target_objective]
    except AttributeError:
      pass

    if "minimize" not in self._target_objective and "maximize" not in self._target_objective:
      self._target_objective = []


  def _setup_fields(self):
    self._fields_mapping = {}
    columns_list = []

    fields_of_interest = "x", "f", "c", "nf", "nc"
    accumulated_width = 0

    basic_columns_spec, all_columns = self._problem._history_fields
    for name, start, stop in basic_columns_spec:
      if name in fields_of_interest and start < stop:
        next_width = accumulated_width + (stop - start)
        self._fields_mapping[name] = slice(start, stop), slice(accumulated_width, next_width)
        accumulated_width = next_width
        columns_list.extend((name + "." + _) for _ in all_columns[start:stop])

    self._designs_columns = tuple(columns_list)
    self._designs_width = accumulated_width + 1 # The uncredited "status" field MUST be the last column. See self.snapshot() for details.

  def _write_data(self, field_name, source, designs):
    if source is not None and field_name in self._fields_mapping:
      designs[:, self._fields_mapping[field_name][1]] = source[:]

  def initial_sample(self, sample_x, sample_f, sample_c, sample_nf, sample_nc):
    if self._generator is None or sample_x is None:
      if self._initial_sample is not None:
        self._last_snapshot = None
        self._initial_sample = None
      return

    self._last_snapshot = None
    self._initial_sample = None

    try:
      self._initial_sample = _numpy.empty((len(sample_x), self._designs_width))
      self._initial_sample.fill(_shared._NONE)

      self._write_data("x", sample_x, self._initial_sample)
      self._write_data("f", sample_f, self._initial_sample)
      self._write_data("c", sample_c, self._initial_sample)
      self._write_data("nf", sample_nf, self._initial_sample)
      self._write_data("nc", sample_nc, self._initial_sample)

      self._initial_sample[:, -1] = _SolutionSnapshot._INITIAL # The last column is the uncredited "status" field.
    except:
      self._initial_sample = None

  def _collect_designs(self, extra_designs):
    # Memory-consuming but fast mode
    problem_history = _shared.convert_to_2d_array(self._problem._history_cache, order='C')
    snapshot_designs = _numpy.empty((problem_history.shape[0], self._designs_width))

    if snapshot_designs.size:
      snapshot_designs.fill(_shared._NONE)

      try:
        self._generator._fill_reconstructed_responses(problem_history)
      except AttributeError:
        # These methods are optional
        pass

      for field in self._fields_mapping:
        slice_from, slice_to = self._fields_mapping[field]
        snapshot_designs[:, slice_to] = problem_history[:, slice_from]

    del problem_history

    if extra_designs is not None:
      snapshot_designs = _numpy.vstack((snapshot_designs, extra_designs))

    if self._initial_sample is not None:
      snapshot_designs = _numpy.vstack((self._initial_sample, snapshot_designs))

    if snapshot_designs.size:
      snapshot_designs = _fill_gaps_and_keep_dups(snapshot_designs, self._fields_mapping["x"][1])
      snapshot_designs = _select_unique_rows(_numpy.vstack(snapshot_designs), 0)

      try:
        # Fill known linear dependencies. We must do it here because the self._problem would be changed for another categorical signature
        snapshot_fields = dict((k, self._fields_mapping[k][0]) for k in self._fields_mapping)
        self._problem._refill_analytical_history(history_records=snapshot_designs, history_fields=snapshot_fields)
      except AttributeError:
        # This method is optional.
        pass

    return snapshot_designs

  def _modern_result_to_snapshot(self, result):
    if not result:
      return None

    try:
      designs_table = result._designs(fields=self._designs_columns)

      n_designs = len(designs_table)

      status_initial = _shared._filled_array(shape=(n_designs,), dtype=int, fill_value=_SolutionSnapshot._UNDEFINED)
      status_initial[result._designs_filter(("initial",))] = _SolutionSnapshot._INITIAL

      status_feasibility = _shared._filled_array(shape=(n_designs,), dtype=int, fill_value=_SolutionSnapshot._UNDEFINED)
      status_feasibility[result._designs_filter(("infeasible",))] = _SolutionSnapshot._INFEASIBLE
      status_feasibility[result._designs_filter(("feasible",))] = _SolutionSnapshot._FEASIBLE
      status_feasibility[result._designs_filter(("potentially feasible",))] = _SolutionSnapshot._POTENTIALLY_FEASIBLE

      # Optimality status can be read from the solution only
      solution_x = result._solutions(fields=[_ for _ in self._designs_columns if _.startswith("x.")])
      solution_optimality = _shared._filled_array(shape=(len(solution_x),), dtype=int, fill_value=_SolutionSnapshot._DOMINATED)
      solution_optimality[result._solutions_filter(("undefined",))] = _SolutionSnapshot._UNDEFINED
      solution_optimality[result._solutions_filter(("optimal",))] = _SolutionSnapshot._OPTIMAL
      solution_optimality[result._solutions_filter(("potentially optimal",))] = _SolutionSnapshot._POTENTIALLY_OPTIMAL

      status_optimality = _shared._filled_array(shape=(n_designs,), dtype=int, fill_value=_SolutionSnapshot._UNDEFINED)
      for solution_index, designs_index in _shared._enumerate_equal_keys(solution_x, designs_table[:, self._fields_mapping["x"][1]], decimals=None):
        status_optimality[designs_index] = solution_optimality[solution_index]

      return self._make_snapshot(designs=designs_table,
                                 status_initial=status_initial,
                                 status_feasibility=status_feasibility,
                                 status_optimality=status_optimality)
    except AttributeError:
      pass

    return None

  def _result_to_designs(self, result):
    if not result:
      return self._last_result_designs

    self._last_result_designs = None

    try:
      # try to treat it as a modern result
      solutions_size = result._solutions_size()
      if not solutions_size:
        return None
      snapshot_solutions = _numpy.empty((solutions_size, self._designs_width))
      snapshot_solutions.fill(_shared._NONE)
      result._unsafe_read_solutions(dict((name, self._fields_mapping[name][1]) for name in self._fields_mapping), snapshot_solutions)
      self._last_result_designs = snapshot_solutions
      return self._last_result_designs
    except AttributeError:
      pass

    # Processing of other result formats can be placed here.

    # treat it as a legacy result
    solutions_size = sum(len(solution.x) for solution in (result.optimal, result.infeasible))
    if not solutions_size:
      return None

    snapshot_solutions = _numpy.empty((solutions_size, self._designs_width))
    snapshot_solutions.fill(_shared._NONE)

    # treat it as a legacy result
    solution_end = 0
    for solution in (result.optimal, result.infeasible):
      solution_begin, solution_end = solution_end, solution_end + len(solution.x)
      if solution_end > solution_begin:
        current_solutions = snapshot_solutions[solution_begin:solution_end]
        for name in self._fields_mapping:
          source_data = getattr(solution, name)
          if len(source_data):
            current_solutions[:, self._fields_mapping[name][1]] = source_data[:]

    self._last_result_designs = snapshot_solutions
    return self._last_result_designs

  def commit_subproblem(self, result):
    if self._generator is not None:
      try:
        subproblem_design = self._result_to_designs(result)
        subproblem_design = self._collect_designs(extra_designs=subproblem_design)
        if subproblem_design.size:
          self._subproblems_design.append(subproblem_design)
      except:
        pass

      # reset initial sample but keep the last snapshot because
      # it is valid until the new initial sample or evaluations arrived
      self._history_length = 0
      self._initial_sample = None
      self._last_result_designs = None

  def reset(self):
    self._target_objective = []
    self._designs_columns = tuple()
    self._fields_mapping = None
    self._designs_width = 0
    self._problem = None
    self._generator = None

    self._initial_sample = None
    self._subproblems_design = []
    self._history_length = 0
    self._last_snapshot = None
    self._last_result_designs = None

  def _prepare_final_result(self, sample_x, sample_f, sample_c, sample_nf, sample_nc):
    # re-initialize initial sample and clear accumulated subproblems
    self.initial_sample(sample_x=sample_x, sample_f=sample_f, sample_c=sample_c, sample_nf=sample_nf, sample_nc=sample_nc)
    self._subproblems_design = []
    self._history_length = 0
    self._last_snapshot = None
    self._last_result_designs = None

  def _make_snapshot(self, designs, status_initial, status_feasibility, status_optimality):
    new_snapshot = _SolutionSnapshot(design_columns=self._designs_columns, designs=designs,
                                            status_initial=status_initial, status_feasibility=status_feasibility,
                                            status_optimality=status_optimality)
    if self._last_snapshot is None or new_snapshot != self._last_snapshot:
      self._last_snapshot = new_snapshot
    self._history_length = len(self._problem._history_cache)
    return self._last_snapshot

  def _status_feasibility(self, design, final_result=False):
    status_feasibility = _numpy.empty(len(design), dtype=int)
    if "nc" in self._fields_mapping:
      status_feasibility.fill(_SolutionSnapshot._POTENTIALLY_FEASIBLE)
      return status_feasibility

    status_feasibility.fill(_SolutionSnapshot._UNDEFINED)
    if "c" not in self._fields_mapping:
      return status_feasibility

    try:
      constraints_tolerance = float(self._generator.options._get("GTOpt/ConstraintsTolerance"))
      constraints_values = design[:, self._fields_mapping["c"][1]]

      # estimate bounds violation
      constraints_violation = _numpy.empty_like(constraints_values)
      for k, (lower_bound, upper_bound) in enumerate(zip(*self._problem.constraints_bounds())):
        constraints_violation[:, k] = self._problem._calculate_constraint_violation(constraints_values[:, k], lower_bound, upper_bound)

      deferred_constraints = self._problem._deferred_responses()[1] if final_result else slice(0, constraints_violation.shape[1])

      # evaluate feasibility codes considering all constraints may be evaluated later
      _, feasibility_codes = self._problem._violation_coefficients_to_feasibility(constraints_violation=constraints_violation,
                                                                                  violation_tolerance=constraints_tolerance,
                                                                                  deferred_constraints=deferred_constraints)
      status_feasibility[feasibility_codes == 0] = _SolutionSnapshot._FEASIBLE # GT_SOLUTION_TYPE_CONVERGED (0) - feasible point, all constraints are known and within bounds.
      status_feasibility[feasibility_codes == 2] = _SolutionSnapshot._INFEASIBLE # GT_SOLUTION_TYPE_INFEASIBLE (2) - infeasible point because there is at least one constraint that is out of limits.
      status_feasibility[feasibility_codes == 3] = _SolutionSnapshot._INFEASIBLE # GT_SOLUTION_TYPE_BLACKBOX_NAN (3) - point is infeasible because there is at least one constraint with value NaN.
      status_feasibility[feasibility_codes == 4] = _SolutionSnapshot._POTENTIALLY_FEASIBLE # GT_SOLUTION_TYPE_NOT_EVALUATED (4) - some constraints that could be evaluated have not been evaluated, but all known constraints are in bounds.
      status_feasibility[feasibility_codes == 7] = _SolutionSnapshot._POTENTIALLY_FEASIBLE # GT_SOLUTION_TYPE_POTENTIALLY_FEASIBLE (7) - there are deferred constraints, but all other constraints are known and within limits.
    except AttributeError:
      # may be we are dealing with another kind of problem
      status_feasibility.fill(_SolutionSnapshot._UNDEFINED)

    return status_feasibility

  def _status_optimality(self, design, status_feasibility, final_result=False):
    status_optimality = _numpy.zeros(len(design), dtype=int)

    if not self._target_objective:
      return status_optimality

    if final_result:
      try:
        deferred_targets, _ = self._problem._deferred_responses()
      except AttributeError:
        deferred_targets = (False,)*len(self._target_objective) # good old blackbox: no deferred targets
    else:
      deferred_targets = (True,)*len(self._target_objective) # all targets are deferred yet

    target_objective = []
    deferred_objectives = []
    for kind, deferred, data in zip(self._target_objective, deferred_targets, design[:, self._fields_mapping["f"][1]].T):
      if kind == "maximize":
        target_objective.append(-data.reshape(-1, 1))
      elif kind == "minimize":
        target_objective.append(data.reshape(-1, 1))
      else:
        continue
      deferred_objectives.append((_shared._find_holes(data) if deferred else _numpy.zeros_like(data)).reshape(-1, 1))

    if not target_objective:
      return status_optimality
    elif "nf" in self._fields_mapping:
      # we could take noise into account but not now
      status_optimality[:] = _SolutionSnapshot._POTENTIALLY_OPTIMAL
      return status_optimality

    target_objective = _numpy.hstack(target_objective)
    deferred_objectives = _numpy.hstack(deferred_objectives)
    target_inputs = design[:, self._fields_mapping["x"][1]]

    from .. import result as _result

    basic_options = self._generator.options.values

    target_constraints = design[:, self._fields_mapping.get("c", (None, slice(0)))[1]]
    solutions_mark = _result.solution_filter(x=target_inputs, f=target_objective, c=target_constraints,
                                              c_bounds=(self._problem.constraints_bounds() if target_constraints.size else tuple()),
                                              options=basic_options)

    status_optimality.fill(_SolutionSnapshot._DOMINATED)
    status_optimality[solutions_mark == _result.GT_SOLUTION_TYPE_CONVERGED]     = _SolutionSnapshot._OPTIMAL
    status_optimality[solutions_mark == _result.GT_SOLUTION_TYPE_NOT_DOMINATED] = _SolutionSnapshot._OPTIMAL
    status_optimality[solutions_mark == _result.GT_SOLUTION_TYPE_INFEASIBLE]    = _SolutionSnapshot._OPTIMAL

    # Reveal non-dominated potentially feasible candidates
    potentially_feasible_points = (status_feasibility == _SolutionSnapshot._POTENTIALLY_FEASIBLE)
    if potentially_feasible_points.any():
      #   0. Let set A is "potentially feasible" points with completely defined objectives
      #   1. Let set B is empty
      #   2. Find the Pareto optimal set S from the pooled sets A and the "optimal"
      #   3. Let set C be the intersection of sets A and S. If C is not empty, move set C from set A to set B and repeat step 2.
      #   4. Set B is a solution — the “optimal” set does not dominate these points.
      fake_bounds = ((-1.,), (1.,))
      fake_constraints = _numpy.empty(len(target_objective))
      fake_constraints[:] = -1000. # ignore by default

      fake_constraints[status_optimality == _SolutionSnapshot._OPTIMAL] = 0. # take optimal points
      fake_constraints[potentially_feasible_points] = 0. # take all potentially feasible

      non_dominated_potentially_feasible = potentially_feasible_points # initialization
      while non_dominated_potentially_feasible.any():
        optimality_marks = _result.solution_filter(x=target_inputs, f=target_objective, c=fake_constraints, c_bounds=fake_bounds, options=basic_options)
        non_dominated_potentially_feasible = _numpy.logical_and(_numpy.logical_or((optimality_marks == _result.GT_SOLUTION_TYPE_CONVERGED),
                                                                                  (optimality_marks == _result.GT_SOLUTION_TYPE_NOT_DOMINATED)),
                                                                potentially_feasible_points)
        fake_constraints[non_dominated_potentially_feasible] = 1000. # mark non-dominated potentially feasible points and exclude these points from the account
      status_optimality[fake_constraints > 1.] = _SolutionSnapshot._POTENTIALLY_OPTIMAL

    if deferred_objectives.any():
      invalid_objectives = _numpy.logical_and(_numpy.isnan(target_objective), ~deferred_objectives).any(axis=1)
      deferred_objectives = _numpy.logical_and(deferred_objectives.any(axis=1), ~invalid_objectives)

    if deferred_objectives.any():
      status_optimality[_numpy.logical_and(deferred_objectives, (status_feasibility != _SolutionSnapshot._INFEASIBLE))] = _SolutionSnapshot._POTENTIALLY_OPTIMAL

    if (status_optimality == _SolutionSnapshot._POTENTIALLY_OPTIMAL).any():
      status_optimality[status_optimality == _SolutionSnapshot._OPTIMAL] = _SolutionSnapshot._POTENTIALLY_OPTIMAL

    return status_optimality

class _DetachableSingleCallableRef(object):
  def __init__(self, callable, *args, **kwargs):
    self._callable = callable
    self._args = args
    self._kwargs = kwargs
    self._result = None
    self._called = False

  def _reset(self):
    self._callable = None
    self._args = None
    self._kwargs = None

  def __call__(self):
    if not self._called:
      self._result = self._callable(*self._args, **self._kwargs) if self._callable else None
      self._called = True
    return self._result

