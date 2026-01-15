import numpy as np

_rng = np.random.default_rng(25)

def sine_init(x:np.ndarray, amp:float, phase:float, shift:float)\
                                                    ->np.ndarray:
    return amp*np.sin(x*(-phase))+shift

def sum_of_sine(N:int, x:np.ndarray, amp0:float=1, phase0:float=0, 
                shift0:float=0, periods:float|int=2, xtrans:float=0):
    """
    Make sum of N sin functions with random amplitudes, phases and x-shifts.
    """
    summed = np.empty((len(x)))
    px = (x-xtrans)/periods
    for i in range(N):
        amp = amp0 + _rng.normal(1, 0.5, 1)
        phase = phase0 + _rng.normal(0, 1, 1)
        shift = shift0 + _rng.normal(0, 1, 1)
        summed += sine_init(px, amp, phase, shift)
    return summed

