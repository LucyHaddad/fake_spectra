import numpy as np
from xraydb.xray import xray_edge

def energy_axis_uniform(absorber:str, edge:str, Npoints:int, 
                            minE:int, maxE:int)->np.ndarray:
    e0 = xray_edge(absorber, edge, energy_only=True)
    energy = np.linspace(e0-minE, e0+maxE, Npoints)
    return e0, energy


def sawtooth_init(x:np.ndarray, amp:float|int=1, angle:int=209,
                  phase:float|int=1, delay:float|int=0)->np.ndarray:
    return amp*2*np.arctan(np.tan(((x+delay)*(-phase)/(2*angle))))

def sawtooth_center(x:np.ndarray, e0:float, f0:np.ndarray)\
                                            ->np.ndarray:
    df0 = np.gradient(f0)
    c_old = np.where(df0 == np.max(df0))[0][0]
    c_new = np.where(x >= e0)[0][0]
    diff = x[c_new]-x[c_old]
    return sawtooth_init(x, delay=-diff)

def sawtooth(x:np.ndarray, e0:float)->np.ndarray:
    """
    Make a sawtooth function of ~1 periods centering around e0.
    """
    f0 = sawtooth_init(x)
    #this centering isn't working particularly well.. double check with gradients?
    #/use ~unit x axis to make it easier?
    f01 = sawtooth_center(x, e0, f0)
    return f01

def arctan():
    """
    arctan function for softer bkg..
    """
    pass