from src.process.make_bkg import make_background
from xraydb.xray import xray_edge
from src.utils.pdfs import make_dweibull

e0 = xray_edge("Fe", "K", energy_only=True)

params = {"edge": "K",
          "atsym": "Fe",
          "n_edge": 1,
          "pad_lower":40,
          "pad_upper":500,
          "e0":e0,
          "npoints":1000}

bkg = make_background(params)
#bkg is okay.... for no_edge = 1
#i think it could be better though
#and the stability wrt. multiple edges needs to be fixed.

pdf = make_dweibull(bkg.energy, e0)


import matplotlib.pyplot as plt
import numpy as np
plt.plot(bkg.energy, pdf/np.max(pdf))
plt.plot(bkg.energy, bkg.mu/np.max(bkg.mu))
plt.show()