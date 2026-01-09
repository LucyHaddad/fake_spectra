#want a chi(E) function that produces decaying sine waves in energy....
#ignore baseline for now.

#maybe use +- gaussian/gammas with poisson probability....
import numpy as np; import matplotlib.pyplot as plt
from scipy.stats import dweibull

def gaussian(x, mean, sigma):
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mean)**2/(2*sigma**2))

x = np.linspace(-5, 5, 4000)
rng = np.random.default_rng(42)

def get_dweibull(x, c, xshift=-2.14):
    return dweibull.pdf(x-xshift, c)

from xraydb.xray import xray_edge

e0 = xray_edge("Cu", "K", energy_only=True)
npoints = 4000

rlow = 400; rhigh = 1000
energy = np.linspace(e0-rlow, e0+rhigh, npoints)

c = 1.82
start = get_dweibull(x, c)

from get_sine import make_sawtooth, center_sawtooth

st = make_sawtooth(energy, delay=0)
st2 = center_sawtooth(energy, e0, st)
st2 = st2 + np.abs(np.min(st2)); st2 = st2/np.max(st2)

plt.plot(energy, st2)
plt.plot(energy, start); plt.show()

#add poisson noise with event freq of start randomly onto the sawtooth and interpolate!

