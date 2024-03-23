""" Methods for smoothing dataset

The main method, `smooth(...)`, takes a number of steps:

    a. linear interpolation
    b. remove drops
    c. sg smoothing
    d. window smoothing

License:
    BSD, see LICENSE.md
"""


import numpy as np
import xarray as xr
import scipy.signal as sig


#
# CONSTANTS
#
DEFAULT_SMOOTHING = sig.savgol_filter
DEFAULT_SMOOTHING_CONFIG = dict(
    window_length=20,
    polyorder=3)
NP_ARRAY_TYPE = 'array'
DATA_ARRAY_TYPE = 'data_array'
DATASET_TYPE = 'dataset'
SAME_CONV_MODE = 'same'
VALID_CONV_MODE = 'valid'
DEFAULT_CONV_MODE = SAME_CONV_MODE
SMOOTHING_DATA_VAR = 'ndvi'
LINEAR_CONV_TYPE = 'linear'
MEAN_CONV_TYPE = 'mean'
DEFAULT_WINDOW_CONV_TYPE = MEAN_CONV_TYPE
DEFAULT_WINDOW_RADIUS = 5


#
# MAIN
#
def smooth(
        data,
        data_var=SMOOTHING_DATA_VAR,
        result_data_var=None,
        remove_dips=True,
        func=DEFAULT_SMOOTHING,
        window_conv_type=DEFAULT_WINDOW_CONV_TYPE,
        smooth_dips_config={},
        func_config=DEFAULT_SMOOTHING_CONFIG,
        window_radius=DEFAULT_WINDOW_RADIUS):
    """
    Runs a series of smoothing steps against an xr.dataset or xr.data_array and
    returning the data in the same format as the input data.

    Steps:

    1. linearly interpolate to fill np.nan
    2. (optional) removes "dips" - sudden large drops in the data that bounce back
    3. (optional) apply a smoothing func (defaults to Savitzky-Golay filter)
    4. (optional) window mean (optionally linearly weighted around point)

    Args:
        data (xr.dataset|xr.data_array): source np.array|xr.dataset|xr.data_array
        data_var (str|None):
            (if exists) use the named data_var
            if falsey: if only 1 data_var exists use that data_var
            otherwise throw error
        result_data_var (None|str|list|):
            if None overwrite <data_var>
            if (str) name of final resulting data-var
            if (list) keeps all the intermediate values using names in list
        remove_dips (bool): if true remove dips using `smooth_dips(..,**smooth_dips_config)`
        func (function): if exists apply smoothing function
        window_conv_type (str|None):
            if exist post-process curve by applying window-smoothing function. one of
            'linear' or 'mean' to run `linear_window_smoothing(...,**window_conv_config)` or
            `mean_window_smoothing(...,**window_conv_config)`
        (smooth_dips/func)_config (dict):
            kwarg-dicts for smooth_dips, func. see methods
            below for details
        window_radius (int): half-size of window for window_conv

    Returns:
        (xr.dataset|xr.data_array) data with smoothed data values
    """
    dvar, rdvar, next_index = _process_data_vars(data_var, result_data_var, 0)
    data = linearly_interpolate(data, data_var=dvar, result_data_var=rdvar)
    if remove_dips:
        dvar, rdvar, next_index = _process_data_vars(rdvar, result_data_var, next_index)
        data, drop_indices = smooth_dips(
            data,
            data_var=dvar,
            result_data_var=rdvar,
            **smooth_dips_config)
        data = data.assign_attrs(drop_indices=drop_indices)
    if func:
        dvar, rdvar, next_index = _process_data_vars(rdvar, result_data_var, next_index)
        data = execute(data, data_var=dvar, result_data_var=rdvar, func=func, **func_config)
    if window_conv_type:
        dvar, rdvar, next_index = _process_data_vars(rdvar, result_data_var, next_index)
        if window_conv_type == LINEAR_CONV_TYPE:
            win_conv = linear_window_smoothing
        else:
            win_conv = mean_window_smoothing
        data = win_conv(data, data_var=dvar, result_data_var=rdvar, radius=window_radius)
    return data


def execute(
        data,
        func=DEFAULT_SMOOTHING,
        func_config=DEFAULT_SMOOTHING_CONFIG,
        return_data_var=False,
        data_var=None,
        result_data_var=None,
        result_prefix=None,
        result_suffix=None,
        **kwargs):
    """
    Runs a function takes an array (np.array|xr.data_array) of values, and returns the
    data in the same format as the input data (np.array|xr.dataset|xr.data_array)

    Args:
        data (np.array|xr.dataset|xr.data_array): source np.array|xr.dataset|xr.data_array
        func (func):
            func that takes and returns a numpy array.
            defaults to scipy's Savitzky-Golay filter
        data_var (str|None):
            [only used for xr.dataset] if exists update
            the named data_var. if falsey: if only 1
            data_var exists use that data_var, otherwise
            throw error.
        result_data_var (str):
            [only used for xr.dataset] name of resulting data-var.
            if None defaults (and overwrites) <data_var>
        result_prefix (str):
            [only used for xr.dataset] ignored if <result_data_var>,
            sets <result_data_var> = <result_prefix>_<data_var>
        result_suffix (str):
            [only used for xr.dataset] ignored if <result_data_var>,
            sets <result_data_var> = <data_var>_<result_suffix>
        **kwargs: kwargs for <func>

    Returns:
        (np.array|xr.dataset|xr.data_array) data with values replace by `func(values)`.
        if <return_data_var> return tuple (data, <result_data_var>)
    """
    data = data.copy()
    da, data_object_type, data_var, result_data_var = _preprocess_xarray_data(
        data,
        data_var,
        result_data_var,
        result_prefix,
        result_suffix)
    values = func(da, **func_config)
    data = _postprocess_xarray_data(
        da,
        data,
        data_object_type,
        result_data_var,
        return_data_var,
        values=values)
    return data


def linearly_interpolate(
        data,
        return_data_var=False,
        data_var=None,
        result_data_var=None,
        result_prefix=None,
        result_suffix=None):
    """ linearly interpolate series xr.dataset/data_array

    Replaces np.nan in a 1-d array with linear interpolation

    Args:
        data (np.array|xr.dataset|xr.data_array): source xr.dataset/data_array
        data_var (str|None):
            [only used for xr.dataset] if exists update
            the named data_var. if falsey: if only 1
            data_var exists use that data_var, otherwise
            throw error.
        result_data_var (str):
            [only used for xr.dataset] name of resulting data-var.
            if None defaults (and overwrites) <data_var>
        result_prefix (str):
            [only used for xr.dataset] ignored if <result_data_var>,
            sets <result_data_var> = <result_prefix>_<data_var>
        result_suffix (str):
            [only used for xr.dataset] ignored if <result_data_var>,
            sets <result_data_var> = <data_var>_<result_suffix>

    Returns:
        (np.array|xr.dataset|xr.data_array) linearly interpolated data
        if <return_data_var> return tuple (data, <result_data_var>)
    """
    data = data.copy()
    da, data_object_type, data_var, result_data_var = _preprocess_xarray_data(
        data,
        data_var,
        result_data_var,
        result_prefix,
        result_suffix)
    values = linearly_interpolate_array(da)
    data = _postprocess_xarray_data(
        da,
        data,
        data_object_type,
        result_data_var,
        return_data_var,
        values=values)
    return data


def smooth_dips(
        data,
        drop_ratio=0.3,
        smoothing_radius=8,
        replacement_radius=1,
        use_maximum=True,
        return_drop_indices=True,
        return_data_var=False,
        data_var=None,
        result_data_var=None,
        result_prefix=None,
        result_suffix=None):
    """
    Replaces points in data where the value has a large dip by

    1. calculating smooth_data = mean of original data at window endpoints
    2. calc ratio of data/smooth_data
    3. if ratio < drop_ratio replace values in window with smoothed_data

    Args:
        data (np.array|xr.dataset|xr.data_array): source np.array|xr.dataset|xr.data_array
        drop_ratio (float): replace data if data/smooth_data <= <drop_ratio>
        smoothing_radius (int):
            half-size of window where data is smoothed by averaging the values
            at the window endpoints.
        replacement_radius (int):
            half-size of window where data will be replaced around drop_indices
        use_maximum (bool):
            if true, use take the max of (smoothed_data, data) as the smoothed_data
        return_drop_indices (bool):
            if true, return the indices for the drops that have been replaced
        data_var (str|None):
            [only used for xr.dataset] if exists update
            the named data_var. if falsey: if only 1
            data_var exists use that data_var, otherwise
            throw error.
        result_data_var (str):
            [only used for xr.dataset] name of resulting data-var.
            if None defaults (and overwrites) <data_var>
        result_prefix (str):
            [only used for xr.dataset] ignored if <result_data_var>,
            sets <result_data_var> = <result_prefix>_<data_var>
        result_suffix (str):
            [only used for xr.dataset] ignored if <result_data_var>,
            sets <result_data_var> = <data_var>_<result_suffix>

    Returns:
        (np.array|xr.dataset|xr.data_array) data with drops removed
        if <return_data_var> return tuple (data, <result_data_var>)
        if <return_drop_indices> return as a tuple:
            (data or (data, result_data_var)), drop_indices)

    """
    data = data.copy()
    da, data_object_type, data_var, result_data_var = _preprocess_xarray_data(
        data,
        data_var,
        result_data_var,
        result_prefix,
        result_suffix)
    kernel = np.zeros(2 * smoothing_radius + 1)
    kernel[0] = kernel[-1] = 1 / 2
    smoothed_data = np.convolve(da, kernel, mode=SAME_CONV_MODE)
    if use_maximum:
        smoothed_data = np.maximum(smoothed_data, da)
    ratio = da / smoothed_data
    test = ratio <= drop_ratio
    drop_indices = np.where(test)[0]
    if drop_indices.shape[0]:
        da = replace_windows(da, smoothed_data, drop_indices, radius=replacement_radius)
    data = _postprocess_xarray_data(
        da,
        data,
        data_object_type,
        result_data_var,
        return_data_var)
    if return_drop_indices:
        return data, drop_indices
    else:
        return data


def kernel_smoothing(
        data,
        kernel,
        normalize=True,
        return_data_var=False,
        data_var=None,
        result_data_var=None,
        result_prefix=None,
        result_suffix=None):
    """
    Smoothes data by convolution over kernel

    Args:
        data (np.array|xr.dataset|xr.data_array): source np.array|xr.dataset|xr.data_array
        kernel (np.array): kernel for convolution
        normalize (bool):
            if true normalize kernel by `<kernel>=<kernel>/<kernel>.sum()`
        data_var (str|None):
            [only used for xr.dataset] if exists update
            the named data_var. if falsey: if only 1
            data_var exists use that data_var, otherwise
            throw error.
        result_data_var (str):
            [only used for xr.dataset] name of resulting data-var.
            if None defaults (and overwrites) <data_var>
        result_prefix (str):
            [only used for xr.dataset] ignored if <result_data_var>,
            sets <result_data_var> = <result_prefix>_<data_var>
        result_suffix (str):
            [only used for xr.dataset] ignored if <result_data_var>,
            sets <result_data_var> = <data_var>_<result_suffix>

    Returns:
        (np.array|xr.dataset|xr.data_array) data convolved over kernel
        if <return_data_var> return tuple (data, <result_data_var>)
    """
    data = data.copy()
    da, data_object_type, data_var, result_data_var = _preprocess_xarray_data(
        data,
        data_var,
        result_data_var,
        result_prefix,
        result_suffix)
    if normalize:
        kernel = kernel / kernel.sum()
    values = np.convolve(da, kernel, mode=SAME_CONV_MODE)
    data = _postprocess_xarray_data(
        da,
        data,
        data_object_type,
        result_data_var,
        return_data_var,
        values=values)
    return data


def mean_window_smoothing(
        data,
        radius=DEFAULT_WINDOW_RADIUS,
        return_data_var=False,
        data_var=None,
        result_data_var=None,
        result_prefix=None,
        result_suffix=None):
    """
    Smoothes data by replacing values with mean over window

    Args:
        data (np.array): input 1-d array in which to replace data
        radius (int): half-size of window
        data_var (str|None):
            [only used for xr.dataset] if exists update
            the named data_var. if falsey: if only 1
            data_var exists use that data_var, otherwise
            throw error.
        result_data_var (str):
            [only used for xr.dataset] name of resulting data-var.
            if None defaults (and overwrites) <data_var>
        result_prefix (str):
            [only used for xr.dataset] ignored if <result_data_var>,
            sets <result_data_var> = <result_prefix>_<data_var>
        result_suffix (str):
            [only used for xr.dataset] ignored if <result_data_var>,
            sets <result_data_var> = <data_var>_<result_suffix>

    Returns:
        (np.array|xr.dataset|xr.data_array) mean-window-smoothed version of data
        if <return_data_var> return tuple (data, <result_data_var>)
    """
    kernel = np.ones(2 * radius + 1)
    return kernel_smoothing(
        data,
        kernel,
        return_data_var=return_data_var,
        data_var=data_var,
        result_data_var=result_data_var,
        result_prefix=result_prefix,
        result_suffix=result_suffix)


def linear_window_smoothing(
        data,
        radius=DEFAULT_WINDOW_RADIUS,
        return_data_var=False,
        data_var=None,
        result_data_var=None,
        result_prefix=None,
        result_suffix=None):
    """
    Smoothes data by replacing values with weighted-mean over window

    Args:
        data (np.array): input 1-d array in which to replace data
        radius (int): half-size of window
        data_var (str|None):
            [only used for xr.dataset] if exists update
            the named data_var. if falsey: if only 1
            data_var exists use that data_var, otherwise
            throw error.
        result_data_var (str):
            [only used for xr.dataset] name of resulting data-var.
            if None defaults (and overwrites) <data_var>
        result_prefix (str):
            [only used for xr.dataset] ignored if <result_data_var>,
            sets <result_data_var> = <result_prefix>_<data_var>
        result_suffix (str):
            [only used for xr.dataset] ignored if <result_data_var>,
            sets <result_data_var> = <data_var>_<result_suffix>

    Returns:
        (np.array|xr.dataset|xr.data_array) linear-window-smoothed version of data
        if <return_data_var> return tuple (data, <result_data_var>)
    """
    left = np.arange(radius) + 1
    right = left[::-1]
    kernel = np.concatenate([left, [radius + 1], right])
    return kernel_smoothing(
        data,
        kernel,
        return_data_var=return_data_var,
        data_var=data_var,
        result_data_var=result_data_var,
        result_prefix=result_prefix,
        result_suffix=result_suffix)


#
# HELPERS
#
def linearly_interpolate_array(data):
    """ linearly interpolate time series

    Replaces np.nan in a 1-d array with linear interpolation

    Args:
        data (np.array|xr.data_array): 1-d np-array

    Returns:
        np.array with np.nan replaced by with linear interpolation
    """
    nb_points = len(data)
    indices = np.arange(nb_points)
    notna = ~np.isnan(data)
    if not isinstance(notna, np.ndarray):
        try:
            notna = notna.compute()
        except:
            pass
    return np.interp(
        indices,
        indices[notna],
        data[notna])


def replace_windows(data, replacement_data, indices, radius=1):
    """ replace data with replacement data for windows around indices

    Replaces data around indices.  For instance, if <radius>=2 and
    there is an index=6 the following data will be replaced

    `data[[4,5,6,7,8]] = replacement_data[[4,5,6,7,8]]`

    Args:
        data (np.array): input 1-d array in which to replace data
        replacement_data 1-d array to replace data with
        indices (list|np.array): indices around wich to replace data
        radius (int): half-size of window
    Returns:
        np.array with data around <indices> replaced
    """
    data = data.copy()
    indices = [range(i - radius, i + radius + 1) for i in indices]
    indices = np.array([i for r in indices for i in r])
    indices = indices.clip(0, len(data) - 1)
    data[indices] = replacement_data[indices]
    return data


#
# INTERNEL
#
def _process_data_vars(data_var, result_data_var, index):
    """
    if <result_data_var> is a list use value at <index>
    for  as result_data_var. increament index

    Returns:
        tuple (data_var, result_data_var, next_index [index + 1])
    """
    if isinstance(result_data_var, list):
        result_data_var = result_data_var[index]
    return data_var, result_data_var, index + 1


def _preprocess_xarray_data(
        data,
        data_var,
        result_data_var,
        result_prefix,
        result_suffix):
    """
    Args:
        data (xr.dataset|xr.data_array): data to process
        data_var (str|None):
            only used for xr.dataset. if exists update
            the named data_var. if falsey: if only 1
            data_var exists use that data_var, otherwise
            throw error.

    Returns:
        tuple (data, datatype, result_data_var)
    """
    da = data
    if isinstance(data, np.ndarray):
        result_data_var = None
        data_object_type = NP_ARRAY_TYPE
    else:
        if isinstance(data, xr.Dataset):
            data_var, result_data_var = _get_data_var_names(
                list(data.keys()),
                data_var,
                result_data_var,
                result_prefix,
                result_suffix)
            data_object_type = DATASET_TYPE
            da = data[data_var]
        else:
            data_object_type = DATA_ARRAY_TYPE
        da.name = result_data_var or da.name
    return da, data_object_type, data_var, result_data_var


def _postprocess_xarray_data(
        da,
        data,
        data_object_type,
        result_data_var,
        return_data_var,
        values=None):
    """
    Returns:
        * if data_object_type is DATASET_TYPE:
            - return a xr.dataset with values assigned to the <result_data_var> data-var
        * otherwise: return da <np.array|xr.data_array>
        * if <return_data_var> return tuple (<xr.dataset>, <result_data_var>)
    """
    if values is not None:
        if data_object_type == NP_ARRAY_TYPE:
            da = values
        else:
            da = xr.DataArray(data=values, coords=da.coords)
    if isinstance(da, xr.DataArray):
        da.name = result_data_var
    if data_object_type == DATASET_TYPE:
        data[result_data_var] = da
    else:
        data = da
    if return_data_var:
        return data, result_data_var
    else:
        return data


def _get_data_var_names(data_var_names, data_var, result_data_var, result_prefix, result_suffix):
    """
    - if not <data_var> extract from data_var_names[0] or raise exception
    - if not <result_data_var> create from [data_var, result_prefix, result_suffix]
    Returns:
        tuple (data_var, result_data_var)
    """
    if not data_var:
        if len(data_var_names) > 1:
            err = (
                'ndvi_trends.smoothing._get_data_var_names: '
                '<data_var> required if multiple data_vars exist '
                f'(data_vars={data_var_names})'
            )
            raise ValueError(err)
        else:
            data_var = data_var_names[0]
    if not result_data_var:
        result_data_var = data_var
        if result_prefix:
            result_data_var = f'{result_prefix}_{result_data_var}'
        if result_suffix:
            result_data_var = f'{result_data_var}_{result_suffix}'
    return data_var, result_data_var
