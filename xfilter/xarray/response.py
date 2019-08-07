'''
Response function for different types of filters.

Author: Wenchang Yang (wenchang@princeton.edu)
'''
import xarray as xr
from scipy.signal import freqz
from ..butter import _lowpass_ba, _highpass_ba, _bandpass_ba

def lowpass_response(cutoff=0.25, order=2, fs=1.0):
    '''calculate the lowpass response given the lowcut and order of the Butterworth
    filter.'''
    b, a = _lowpass_ba(cutoff=cutoff, order=order, fs=fs)
    f, h = freqz(b=b, a=a, whole=False, fs=fs)
    # the actual order is 2x the given order since a forward-backward filter is appled
    da = xr.DataArray(h.real**2 + h.imag**2,
        dims='freq', coords=[f,],
        name='response')
    da.attrs['info'] = f'Butterworth {order}-order forward-backward lowpass response'
    da['freq'].attrs['units'] = 'sample freq'

    return da

def highpass_response(cutoff=0.25, order=2, fs=1.0):
    '''calculate the highpass response given the lowcut and order of the Butterworth
    filter.'''
    b, a = _highpass_ba(cutoff=cutoff, order=order, fs=fs)
    f, h = freqz(b=b, a=a, whole=False, fs=fs)
    # the actual order is 2x the given order since a forward-backward filter is appled
    da = xr.DataArray(h.real**2 + h.imag**2,
        dims='freq', coords=[f,],
        name='response')
    da.attrs['info'] = f'Butterworth {order}-order forward-backward highpass response'
    da['freq'].attrs['units'] = 'sample freq'

    return da

def bandpass_response(cutoff=(0.125, 0.375), order=2, fs=1.0):
    '''calculate the bandpass response given the cutoff and order of the Butterworth
    filter.'''
    b, a = _bandpass_ba(cutoff=cutoff, order=order, fs=fs)
    f, h = freqz(b=b, a=a, whole=False, fs=fs)
    # the actual order is 2x the given order since a forward-backward filter is appled
    da = xr.DataArray(h.real**2 + h.imag**2,
        dims='freq', coords=[f,],
        name='response')
    da.attrs['info'] = f'Butterworth {order}-order forward-backward bandpass response'
    da['freq'].attrs['units'] = 'sample freq'

    return da
