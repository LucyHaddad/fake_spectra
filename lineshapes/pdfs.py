import numpy as np
from scipy.stats import dweibull

def gaussian(x:np.ndarray, mean:float, sigma:float)->np.ndarray:
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mean)**2/(2*sigma**2))

def make_dweibull(energy:np.ndarray, c:float=1.82)->np.ndarray:
    Npoints = len(energy)
    Eres = max(energy)/Npoints
    x = np.linspace(-5, 5, Npoints)
    return dweibull.pdf(x+Eres, c)
    