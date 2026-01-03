"""
create a histogram showing the distribution of the maximum value pools
of six d20s with the maximum value taken
"""
import matplotlib.pyplot as plt
import numpy as np

from n_dice_monte import sim_max
from n_dice_monte import histogram

SIM_SIZE = 5000
DICE_SIZE = 6

sim_arr = sim_max(SIM_SIZE, DICE_SIZE)
avg = np.mean(sim_arr)

fig, ax = plt.subplots()

ax = histogram(sim_arr, DICE_SIZE)
ax.legend(title="Mean is {:.2f}".format(avg), loc='upper left', reverse=True)
ax.set_title('Basic d6 distribution')

plt.show()
#plt.savefig("./dev/d6_basic.jpg")

#bins = np.arange(1,DICE_SIZE+2, dtype=int)-0.5
#print("array bins are")
#print(bins)
