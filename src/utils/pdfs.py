import numpy as np
from scipy.stats import dweibull, betaprime
from scipy.interpolate import PchipInterpolator

def gaussian(x:np.ndarray, mean:float, sigma:float)->np.ndarray:
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mean)**2/(2*sigma**2))

def make_dweibull(energy:np.ndarray, e0:float, c:float=1.82)->np.ndarray:
    NPoints = len(energy)
    x = np.linspace(-10, 10, NPoints)
    pdf = dweibull.pdf(x, c); dpdf = np.gradient(pdf)
    wheremax = np.where(dpdf == np.max(dpdf))[0][0]
    dexp_up = int(energy[-1]-e0)
    dexp_low = int(np.abs(energy[0]-e0))
    pdf_croppd = pdf[wheremax-dexp_low:wheremax+dexp_up]
    
    xout = np.linspace(-10, 10, len(pdf_croppd))
    xtarget = np.linspace(-10, 10, NPoints)
    fdw = PchipInterpolator(xout, pdf_croppd)
    out = fdw(xtarget)
    return out

def make_bprime(energy:np.ndarray, e0:float, a:float=10)->np.ndarray:
    npoints = len(energy)
    x = np.linspace(-1, 1, len(energy))
    bprime = betaprime(a, len(energy)*10**-2)
    pdf = bprime.pdf(x); dpdf = np.gradient(pdf)
    wheremax = np.where(dpdf == np.max(dpdf))[0][0]
    dexp_up = int(energy[-1]-e0)
    dexp_low = int(np.abs(energy[0]-e0))
    pdf_croppd = pdf[wheremax-dexp_low:wheremax+dexp_up]

    xout = np.linspace(-10, 10, len(pdf_croppd))
    xtarget = np.linspace(-10, 10, npoints)
    fdw = PchipInterpolator(xout, pdf_croppd)
    out = fdw(xtarget)
    return out

def make_pdf(energy:np.ndarray, e0:float, c:float=1.82, a:float=10)->np.ndarray:
    twopeak =make_dweibull(energy, e0, c)
    bprime = make_bprime(energy, e0, a)

    pdf = twopeak*bprime
    pdf = pdf/np.max(pdf)
    return pdf
