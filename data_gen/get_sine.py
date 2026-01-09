import numpy as np
import matplotlib.pyplot as plt

_rng = np.random.default_rng(42)

def fsine(x, amp, phase, shift):
    return amp*np.sin(x*(-phase))+shift

def get_sum_sine(N, x, amp0, phase0, shift0, periods, xtrans):
    sum_sine = np.empty((len(x)))
    px = (energy-xtrans)/periods

    for i in range(N):
        amp = amp0+_rng.normal(1, 0.5, 1)
        phase = phase0+_rng.normal(0, 0.5, 1)
        shift =shift0+ _rng.normal(0, 0.5, 1)
        sum_sine += fsine(px, amp, phase, shift)
    return sum_sine

from scipy.signal import sawtooth

from xraydb.xray import xray_edge

e0 = xray_edge("Fe", "K", energy_only=True)
npoints = 4000

rlow = 400; rhigh = 1000
energy = np.linspace(e0-rlow, e0+rhigh, npoints)

def make_sawtooth(x, amp=1, angle=209, phase=1, delay=0):
    return amp*2*np.arctan(np.tan(((x+delay)*(-phase)/(2*angle))))

def center_sawtooth(x, e0, old_sawtooth):
    old_c = np.where(np.gradient(old_sawtooth) == np.max(np.gradient(old_sawtooth)))[0][0]
    new_c = np.where(x >= e0)[0][0]
    diff = x[new_c]-x[old_c]
    return make_sawtooth(x, delay=-diff)

# st = make_sawtooth(energy, delay= len(energy))
# st = st + np.abs(np.min(st)); st = st/np.max(st)
# plt.plot(energy, st)
# out = get_sum_sine(5, energy, 1, 0, 10, 50, 1)
# #out = out/np.max(out)
# plt.plot(energy, out)

# plt.plot(energy, st*out)

# plt.show()