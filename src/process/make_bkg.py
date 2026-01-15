from utils.background import sawtooth_wave
import numpy as np

def make_background(params):
    absorber = params["atsym"]; edge = params["edge"]
    minE = np.abs(params["pad_lower"]); maxE = params["pad_upper"]
    npts = params["npoints"]; e0 = params["e0"]
    n_edge = params["n_edge"]

    energy = np.linspace(e0-minE, e0+maxE, npts)
    bkg = sawtooth_wave(energy, e0, num_edges=n_edge)
    return bkg