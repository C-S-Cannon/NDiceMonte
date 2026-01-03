"""
create a histogram showing the distribution of the maximum value pools
of six d20s with the maximum value taken
"""
import matplotlib.pyplot as plt
import numpy as np

from n_dice_monte import sim_max
from n_dice_monte import histogram

SIM_SIZE = 10000
DICE_FACE = 20
DICE_POOL = 6

sim_arr = sim_max(SIM_SIZE, DICE_FACE, DICE_POOL)
avg = np.mean(sim_arr)

fig, ax = plt.subplots()

ax = histogram(sim_arr, DICE_FACE)
ax.set_title('6d20 Maxpool Distribution')
ax.legend(title="Mean is {:.2f}".format(avg), loc='upper left', reverse=True)


#ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))

#plt.savefig("./dev/six_20s.jpg")
plt.show()
