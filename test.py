from lineshapes.background import energy_axis_uniform, sawtooth
from lineshapes.pdfs import make_dweibull
from lineshapes.modulations import sum_of_sine

e0, energy = energy_axis_uniform("Fe", "K", 4000, 400, 1000)

pdf = make_dweibull(energy)
bkg = sawtooth(energy, e0)

import matplotlib.pyplot as plt
import numpy as np
plt.plot(energy, pdf/np.max(pdf))
plt.plot(energy, bkg/np.max(bkg))
plt.show()