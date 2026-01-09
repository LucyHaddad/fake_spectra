import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

from get_sine import make_sawtooth, energy

fig, ax = plt.subplots()

st = make_sawtooth(energy, 1, 209, 1, 100)

line = ax.plot(energy, st)
fig.subplots_adjust(left=0.25, bottom=0.25)

amp_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03])
amp_slider = Slider(ax=amp_ax,label="amp", valmin=0.1, valmax=5,
                     valstep=0.1, valinit=1)

angle_ax = fig.add_axes([0.25, 0.05, 0.65, 0.03])
angle_slider = Slider(ax = angle_ax, label="angle", valmin=1, valmax=np.max(energy)/2,
                       valstep=1, valinit=209)

phase_ax = fig.add_axes([0.13, 0.25, 0.0225, 0.63])
phase_slider = Slider(ax=phase_ax, orientation="vertical",
                      valmin=-100, valmax=100, valinit=1, valstep=1, label="phase")

delay_ax = fig.add_axes([0.05, 0.25, 0.0225, 0.63])
delay_slider = Slider(ax=delay_ax, orientation="vertical",
                      valmin=-100, valmax=np.max(energy), valinit=100, valstep=1, label="delay")

def onchange(v):
    line[0].set_ydata(make_sawtooth(energy, amp_slider.val, angle_slider.val,
                                     phase_slider.val, delay_slider.val))
    fig.canvas.draw_idle()

[s.on_changed(onchange) for s in [amp_slider, angle_slider, phase_slider, delay_slider]]

plt.show()