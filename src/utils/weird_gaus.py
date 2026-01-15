#want to make a weird gaussian generator to pretend to be xafs(E)..
import numpy as np
import matplotlib.pyplot as plt

_rng = np.random.default_rng()
def weird_gaus(x, mean):
    mean1 = _rng.normal(mean, len(x)/2, 1) #used mean(x) before
    sigma1 = _rng.normal(len(x)/5, len(x)/5, 1)
    wgaus = 1/(sigma1*np.sqrt(2*np.pi))*np.exp(-(x-mean1)**2/(2*sigma1**2))
    return wgaus

def gen_weird_gaus(x, pdf):
    gaus_out = np.zeros_like(x)
    for i in range(len(pdf)):
        pdftmp = pdf[i]
        meantmp = x[i]
        wg = _rng.poisson(pdftmp, 1)*weird_gaus(x, meantmp)
        gaus_out += wg
    return gaus_out
