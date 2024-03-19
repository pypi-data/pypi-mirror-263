#!/usr/bin/python3

from scipy import ndimage
import numpy as np
from xarray import DataArray
import pytest, logging

'''
Helpers for X-ray diffraction data analysis
'''

def series_cntrmass(data, series=None):
    ''' Calculates N-1 dimensional center of mass for an N-dimensional array.

    Args:
    
        data: This is expected to be an `xarray` with at least 2
           named dimensions, or a list of N-dimensional arrays.

        series: If `data` is an `xarray`, this is expected to be a string
           naming the axis along which to break data apart and form
           a series of.
           
           If data is a `numpy` array or a regular (nested) list,
           `series` is expected to be an axis index.
           
           If data is an iterable (e.g. a list of arrays), then `series`
           must remain `None`, and the `data` iterable already defines
           the series.

           In all cases, if `series=None` (the default), the center of
           mass series will be built along the 1st dimension.
    
    Returns: a 2D `xarray.DataArray`. The first dimension has the same length as the
        length of the series (i.e. the length of the `series` dimension).
        The 2nd dimension hs a length of N-1, where N is the number of dimensions
        of the original data series.
        Each entry being an N-1 dimensional coordinate of the center of mass in 
        the respective plane.
    '''
    
    
    # The difficult part is going to be that ndimage's center_of_mass()
    # returns a fractional (!) positional (!!) index, i.e. one that's
    # related to the position.
    
    # Push the dimension we want to keep to the begging (that's
    # apparently the only one we can iterate over)
    if series is not None:
        view = data.transpose(series, ...)
    else:
        view = data
        
    index_list = []

    if hasattr(view, 'dims'):
        # ...if input is a single DataArray
        
        if len(view.shape) <= 1:
            raise RuntimeError(f'Input data must be a sequence of datasets (i.e. multiple arrays),'
                               f' or a multi-dimensional array.')
        
        other_axes = [o for o in view.dims[1:]]
    else:
        # ...if input series is actually a list of (1D) datasets
        other_axes = list(next(iter(data)).dims)

    
    ## iterate along `axis` and collect all the COMs in index_list
    for img in view:
        try:
            com = ndimage.measurements.center_of_mass(img.data)
            ci  = np.array(com, dtype=int)
            cf  = com-ci
        except ValueError as e:
            # All-zero datasets produce errors (there's no useful definition
            # of a COM on an all-zero dataset). It's the upper layer's responsibility
            # to fix this, but we want to give the user a little bit more information
            # to go on.
            logging.error(f'Error: {str(e)}: this is probably because you have all-zero datasets')
            raise
        
        # iterate over each COM coordinate of the N-1 dim 
        #index = [ view.coords[c].values[i] + f*(img.coords[c].values[i+1]-img.coords[c].values[i])
        #             for c,i,f in zip(other_axes, ci, cf) ]

        index = [ img.coords[c].values[i] + f*(img.coords[c].values[i+1]-img.coords[c].values[i])
                     for c,i,f in zip(other_axes, ci, cf) ]
        
        index_list.append(index)

    # We return a 2D DataArray. In the first dimension, we have one entry
    # for each of the COM sets. We're naming this as the original axis
    # was named (if 'series' is defined), or simply 'plane' if the data sets
    # were passed on as a list.
    # The 2nd dimension is a string list of all the other dimension names
    # (so that we know how to attribute the COM components).
    
    if series is not None:
        series_coords = view.coords[series].values
        series_dim = series
    else:
        series_coords = [i for i in range(len(view))]
        series_dim = 'plane'
        
    coords = {
        series_dim: series_coords,
        'axis': other_axes
    }
        
    return DataArray(data=index_list, coords=coords)


def sqdistance(*axes, center, shape=None):
    '''
    Takes a list of axes and a location desginated `center` and returns
    a N-dimensional array with all the squared distances from `center`
    to each of the points. The array dimensions are assumed to be
    equivalent in size.
    
    Parameters:
    
      - `*axes`: Axis objects, one per parameter. One axis object
        can either be an `xarray` coordinates tuple `(dim, values)`
        with `dim` as a string identifyer and `values` as the axis
        values; or they can be plain iterables (regular `numpy` 1D
        arrays or lists).
        
      - `center`: needs to be 1-dimensional vector with N values,
        if `axes` items are regular `numpy` arrays or iterables.
        Otherwise 
        It represents the point relative to which the squared distance
        of all other points is calculated.
        Despite its name it does not need to be, and typically is
        not, the actual center of the field.
        
      - `shape`: Instead of explicitly specifying a list of axes,
        a single vector continaing an N-dimensional array shape
        can also be specified. In that case, the axes will be
        constructed as regular indices ranging from `0` to `len(shape[n])`
        
    Returns: N-dimensional array of size `len(axes[0]) * len(axes[1]) * ... * len(axes[n])`
    contraining the squared distance to `center` for each point.
    '''
        
    if (not axes or len(axes) == 0) and shape is not None:
        # numpy array style shape. We don't actually have axis
        # values, we need to build them first. `center` is a
        # 1D-array (one coordinate per axis) we can juse for
        # indexing.
        axvalues = [[i for i in range(s)] for s in shape] 
        cvalues = tuple(center)
        return_numpy = True
        
    elif isinstance(axes[0], tuple) and len(axes[0]) == 2 and isinstance(axes[0][0], str):
        # Named axes, `xarray` or `pandas` style. Each axis element
        # is either one `xarray` Axis object (with values in the .values
        # property) or a (name, values) axis tuple.
        # `center` is either a dict, or a list of (key, val) tuples.
        axvalues =  [ (x[1].values if hasattr(x[1], "values") else x[1])   for x in axes]
        cobj = dict(center)
        cvalues = tuple([cobj[x[0]] for x in axes])
        return_numpy = False
        
    else:
        # numpy array, explicit axes. Each axis is a 1D-iterable
        # and `center` is a 1D-tuple (one coordinate per axis).
        axvalues = axes
        cvalues = center
        return_numpy = True
    
    sqdist = np.abs(axvalues[0] - cvalues[0])**2
    for ax,c in zip(axvalues[1:], cvalues[1:]):
        sqdist = sqdist[...,None]
        sqdist = sqdist + np.ones(sqdist.shape) * (ax-c)**2
    
    if return_numpy:
        return sqdist
    
    return DataArray(data=sqdist, coords=[(x[0], x[1].values) for x in axes])
    
    
def stdwidth1d(data, center):
    ''' Calculates the standard deviation a.k.a. "peak width".

    This is defined as the square-root of the
    [variance](https://en.wikipedia.org/wiki/Variance#Discrete_random_variable)
    of an experimental data array with respect to the value located in the
    same array at index position called `center`.

    For 1-dimensional arrays of discrete points, the variance is essentially
    defined as `(Xi-M)**2`, i.e. the squared sum of the differences of the
    poins `Xi` from a mean value `M`. It's a measure of how much each
    value differs from the mean.

    For N-dimensional data, the statistical reasoning is more complex and
    evolves around [the covariance matrix](https://en.wikipedia.org/wiki/Covariance_matrix).
    This function does *not* implement the covariance matrix version
    (serach for `stdvariance()` instead), but only the simple 1D version.
    If fed with a multiple N-dimensional input, it *still* only calculates
    one variance, which can essentially be interpreted as an "average variance"
    along all dimensions.
    
    Args:
    
        data: The data for which to calculate the standard width.
          This can either be:
            - an N-dimensional `numpy` array
            - an N-dimensinonal `xarray.DataArray`
        
        center: The center of mass relative to which to calculate the
          deviation. This can be:
    
            - an N-tuple capable of indexing `data`. This is expected,
              if `data` is an numpy array.

            - a dictionary with dimension names as keys, and positions
              (coordinate lists/arrays) as values, or...

            - ...a single `(dim, value)` tuple, or...

            - ...an `xarray.DataArray` with positions / center-of-mass
              coordinates.
      
    Returns: One single value, represending the sum of suqare distances
    weighted by the function value at the respective place, if
    `axis=None`. If `axis` is specified, then the result will be a
    1-dimensional array containing standard widths along `axis`.
    '''
    
    # Preparing the coordinate axis array of `data' -- for an xarray
    # we just build (name, values) tuples of its dims; for numy arrays,
    # we generate an integer index corresponding to the length.
    if hasattr(data, "coords"):
        axes = [(d, data.coords[d]) for d in data.dims]
    else:
        axes = [range(i) for i in data.shape]
        
    pos = center
        
    sqdist = sqdistance(*axes, center=pos)
    sqvar  = (sqdist * data / data.sum()).sum()
    
    return np.sqrt(sqvar)


def series_stdwidth1d(data, center, axis=0):
    '''
    Wrapper for `stdwidth1()` to act on a collection of data sets at once.
    #
    '''
    pass


def test_stdwidth1d_ndarray(test_ndarray):
    '''
    Test for stdwidth()
    '''

    center = (np.array(test_ndarray.shape)/2).astype(int)
    
    v = stdwidth1d(test_ndarray, center)

    # We're measuring the variance ("width") with regards to the
    # actual center of the data patch, so this should always essentially
    # be smaller than half the field.
    # This being random data, it *should* have a width larger than 1
    # grid point, though...
    assert (v <= np.abs(center.max()))
    assert (v >= 1.0)

    
def test_stdwidth1d_xarray(test_xarray):
    '''
    Test for stdwidth()
    '''

    # alias
    dta = test_xarray

    center = [ (x, dta.coords[x].values[0]+(dta.coords[x].values[-1]-dta.coords[x].values[0])/2 ) \
                     for x in test_xarray.dims ]
    
    v = stdwidth1d(test_xarray, center=dict(center))

    # We're measuring the variance ("width") with regards to the
    # actual center of the data patch, so this should always essentially
    # be smaller than the field.
    c_coord = np.array([dta.coords[x].values[-1]-dta.coords[x].values[0] for x in dta.dims])
    assert (v <= np.abs(c_coord.max()))


    
@pytest.fixture
def test_ndarray():
    ''' Returns a an ndarray of variable size and shape (i.e. dimensions) '''

    ## ...up to 7 dimensions should prove the point.
    ## Configurable for debugging.
    
    min_dims = 2
    max_dims = 2 #7

    min_size = 2
    max_size = 10 #20
    
    dims = min_dims + int(np.random.random() * (max_dims-min_dims))
    shp  = min_size + (np.random.random(dims) * (max_size-min_size)).astype(int)
    return np.array(np.random.random(shp.prod())).reshape(shp)


@pytest.fixture
def test_ndcenter(test_ndarray):
    ''' Returns a random 'center' coordinate that lies within the array '''
    return (np.random.random(len(test_ndarray.shape)) * test_ndarray.shape).astype(int)
    

def test_sqdist_ndarray(test_ndarray, test_ndcenter):
    '''
    Tests sqdistance() on an ndarray (i.e. no named axes)
    '''
    
    assert ((test_ndcenter < test_ndarray.shape).all())
    
    sqd1 = sqdistance(center=test_ndcenter, shape=test_ndarray.shape)
    
    axlist = tuple([range(s) for s in test_ndarray.shape])
    sqd2 = sqdistance(*axlist, center=test_ndcenter)

    # No distance can be longer than the diagonal across all dimensions
    assert (sqd1.max() <= (np.array(test_ndarray.shape)**2).sum())
    assert (sqd2.max() <= (np.array(test_ndarray.shape)**2).sum())
    
    # The square distance result has exactly one point for every input point
    assert (sqd1.shape == test_ndarray.shape)
    assert (sqd2.shape == test_ndarray.shape)
    
    assert ((sqd1[tuple(test_ndcenter)] == sqd2[tuple(test_ndcenter)]).all())
    
    # Distance at center is always zero
    assert((sqd1[tuple(test_ndcenter)] == 0).all())
    assert((sqd2[tuple(test_ndcenter)] == 0).all())
                                                                      
                                                                      
def test_sqdist_ndtuple(test_ndarray, test_ndcenter):
    '''
    Test whether sqtistance() accepts tuples as arguments
    '''
    axlist = tuple([range(s) for s in test_ndarray.shape])
    sqd = sqdistance(*axlist, center=tuple(test_ndcenter))
    assert (sqd.shape == test_ndarray.shape)
                                                                      
                                                                      
@pytest.fixture
def test_xarray(test_ndarray):
    ''' Creates an `xarray` with named axes based on a random ndarray '''
    
    axis_names = ['physics', 'trustee', 'warning', 'ethnic',
                  'tree', 'text', 'contraction', 'shell' ]
    
    return DataArray(data=test_ndarray,
                     coords=[np.array(range(s))*0.1-(s/20) for s in test_ndarray.shape],
                     dims=axis_names[:len(test_ndarray.shape)])
    

@pytest.fixture
def test_xcenter(test_xarray):
    '''
    Generates a random single-point center coordinate based on an
    array with named axes. The coordinate tuple has named dimensions.
    '''
    
    pos = {}
    for d in test_xarray.dims:
        ax = test_xarray.coords[d].values
        r = np.random.random()
        c = ax[0] + r*(ax[-1]-ax[0])
        pos[d] = c

    return pos


def test_sqdist_xarray(test_xarray, test_xcenter):
    '''
    Tests the sqdistance() function with xarray-like named axes.
    '''
        
    ## This is for more specific testing / debugging.
    #shape  = (5, 5)
    #data   = np.ones(shape)
    #axes   = [(np.array(range(s))-s/2)*0.1 for s in shape]
    #center = {'x': 0, 'y': 0 }
    #xdata  = DataArray (data=data, coords=axes, dims=['x', 'y'])
    
    center = test_xcenter
    xdata  = test_xarray
    
    sqd = sqdistance(*xdata.coords.items(), center=center)
    
    assert (sqd.max() <= (np.array(xdata.shape)**2).sum())
    
    # The square distance result has exactly one point for every input point
    assert (sqd.shape == xdata.shape)
    
    # Calculate distance (N-dim diagonal) between two ajacent axis coordinates.
    # This will give us a very crude estimate of an error measure which is
    # (1) smaller than a pixel, but
    # (2) still large enough such that an interpolation of the array value
    # at that specfic point will still fit well within that error value.
    
    pix_diag = np.sqrt(np.array([ (x[1].values[1]-x[1].values[0])**2 for x in xdata.coords.items() ]).sum())
    maxerr = pix_diag*0.5 / len(xdata.shape)
    
    #print ("### distances:\n", np.sqrt(sqd.values))
    #print ('### pixdiag:', pix_diag)
    #print ('### maxerr:', maxerr)
    #print ('### value(s) at center:', sqd.interp(center).values)
    #print ('### center coordinates:', center)
        
    # Distance at center is always zero
    assert( (sqd.interp(center) < maxerr).all())

    # Make sure sqdistance() accepts a list of tuples as center coordinates
    sqd2 = sqdistance(*xdata.coords.items(), center=center.items())
    assert ((sqd2 == sqd).all())

    # Make sure sqdistance() accepts a dict() center coordinates
    sqd3 = sqdistance(*xdata.coords.items(), center=dict(center.items()))
    assert ((sqd3 == sqd).all())

    # Make sure sqdistance() accepts a list of tuples as axes
    #sqd3 = sqdistance(*tuple( [(d,xdata.coords[d]) for d in xdata.dims] ),
    #                  center=center)
    #assert ((sqd2 == sqd3).all())
