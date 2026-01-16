import numpy as np
from xraydb.xray import xray_edge
from larch.math import smooth
from larch import Group
from scipy.interpolate import PchipInterpolator

def energy_axis_uniform(absorber:str, edge:str, Npoints:int, 
                            minE:int, maxE:int)->tuple[float, np.ndarray]:
    e0 = xray_edge(absorber, edge, energy_only=True)
    energy = np.linspace(e0-minE, e0+maxE, Npoints)
    return e0, energy

def interpolate_1d(y, energy):
    xold = np.linspace(0, 1, len(y))
    xtarget = np.linspace(0, 1, len(energy))
    interpd = PchipInterpolator(xold, y)
    fx = interpd(xtarget)
    return fx

edge_dict = {1: [-3*np.pi, -np.pi],
             2: [-3*np.pi, 0],
             3: [-3*np.pi, 2*np.pi]}

def sawtooth_wave(energy, e0, num_edges=1):
    angle = np.pi/4; npoints = len(energy)
    xrange = edge_dict[num_edges]
    x0 = np.linspace(xrange[0], xrange[-1], npoints)

    fx0  = 2*np.arctan(np.tan(((x0)*(-1)/(2*angle))))
    dfx0 = np.gradient(fx0)
    wheremax = np.where(dfx0 >= np.pi - 0.05)[0][0::2]

    max_end_abs = wheremax[num_edges-1]
    max_end0 = wheremax[0]
    dexp_up = int(energy[-1]-e0)
    dexp_low = int(np.abs(energy[0]-e0))

    fx1 = fx0[max_end0-dexp_low: max_end_abs+dexp_up]

    out = interpolate_1d(fx1, energy)
    y_out = smooth(energy, out)
    #at e0 fit with quatratic to make whiteline?
    group = Group(energy=energy, mu=y_out, e0=e0)
    group.mu = whiteline_peak(group)
    return group

from numpy.linalg import lstsq

def whiteline_peak(signal):
    dmu = np.gradient(signal.mu)
    dmumax = np.where(dmu > np.mean(dmu))[0]
    lb = dmumax[0]; ub = dmumax[-1]
    lb1 = int((lb+ub)/2)
    ub1 = ub+lb1
    #may be best to fit a gaussian..
    y_tmp = signal.mu[lb1:ub1]
    ymat = np.ones([3, y_tmp.shape[0]])
    ymat[1,:] = np.arange(y_tmp.shape[0])
    ymat[2,:] = np.arange(y_tmp.shape[0])**2
    fitted = lstsq(ymat.T, y_tmp.T)
    yfit = ymat.T@fitted[0]

    y_out = np.empty_like(signal.mu)
    y_out[:lb1] = signal.mu[:lb1]
    y_out[lb1:ub1] = yfit
    y_out[ub1:] = signal.mu[ub1:]
    #yout = smooth(signal.energy, y_out, sigma=1)
    return y_out

