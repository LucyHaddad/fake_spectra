#sawtooth on new energy axis to (hopefully) simplify the aligning.
import numpy as np
import matplotlib.pyplot as plt

def sawtooth_init(energy, e0):
    angle = 0.3; Npoints = len(energy)
    x = np.linspace(-1, 1, Npoints)

    st_trial = 2*np.arctan(np.tan(((x)*(-1)/(2*angle))))
    df = np.gradient(st_trial)
    c_old = np.where(df==np.max(df))[0][0]
    c_target = np.where(energy >= e0)[0][0]
    diff = np.abs(c_old-c_target)

    st = 2*np.arctan(np.tan(((x-diff)*(-1)/(2*angle))-diff))
    return st/np.max(st)

#too difficult..... try with numpy sawtooth?/some interpolated stepwise function?

from background import energy_axis_uniform

e0, energy = energy_axis_uniform("Cu", "K", 4000, 500, 2000)
#delay needs to be dependent on minE and maxE prior to edge somehow....
sawt = sawtooth_init(energy, e0)

plt.title(f"target: {e0}")
plt.plot(energy, sawt)

plt.show()