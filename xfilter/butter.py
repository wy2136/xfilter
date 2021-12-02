'''
Butterworth filter: lowpass, highpass and bandpass.

Author: Wenchang Yang (wenchang@princeton.edu)
'''

import numpy as np
from scipy.signal import butter, filtfilt

def _lowpass_ba(cutoff=0.25, order=2, fs=1.0):
    '''Butterworth filter lowpass coefficients.'''
    nyq = 0.5 * fs
    low = cutoff / nyq
    b, a = butter(order, low, btype='lowpass')
    return b, a
def lowpass(X, cutoff=0.25, order=2, axis=0, fs=1.0, **kws):
    '''Butterworth lowpass filter.

    *Parameters*:
        X: ndarray.
        cutoff: float, low-frequency cutoff, default=0.25 (unit is sample freq).
        order: int, default=2.
        axis: int, default=0.
        fs: number, sample freqency, default=1.0

    *Return*:
        Y: ndarray, lowpassed X.'''

    b,a = _lowpass_ba(cutoff=cutoff, order=order, fs=fs)
    Y = filtfilt(b, a, X, axis=axis, **kws)
    return Y

def _highpass_ba(cutoff=0.25, order=2, fs=1.0):
    '''Butterworth filter highpass coefficients.'''
    nyq = 0.5 * fs
    high = cutoff / nyq
    b,a = butter(order, high, btype='highpass')
    return b,a
def highpass(X, cutoff=0.25, order=2, axis=0, fs=1.0, **kws):
    '''Butterworth highpass filter.

    *Parameters*:
        X: ndarray.
        cutoff: float, high-frequency cutoff, default=0.25 (unit is sample freq).
        order: int, default=2.
        axis: int, default=0.
        fs: number, sample freqency, default=1.0

    *Return*:
        Y: ndarray, highpassed X.'''

    b,a = _highpass_ba(cutoff=cutoff, order=order, fs=fs)
    Y = filtfilt(b, a, X, axis=axis, **kws)
    return Y

def _bandpass_ba(cutoff=(0.125, 0.375), order=2, fs=1.0):
    '''Butterworth filter bandpass coefficients.'''
    nyq = 0.5 * fs
    low = cutoff[0] /nyq
    high = cutoff[1] / nyq
    b,a = butter(order, [low,high], btype='bandpass')
    return b,a
def bandpass(X, cutoff=(0.125, 0.375), order=2, axis=0, fs=1.0, **kws):
    '''Butterworth bandpass filter.

    *Parameters*:
        X: ndarray.
        cutoff: (float, float), low/high-frequency cut, default=(0.125, 0.375) (unit is sample freqency).
        order: int, default=2.
        axis: int, default=0.
        fs: number, sample freqency, default=1.0

    *Return*:
        Y: ndarray, highpassed X.'''

    b,a = _bandpass_ba(cutoff=cutoff, order=order, fs=fs)
    Y = filtfilt(b, a, X, axis=axis, **kws)
    return Y
