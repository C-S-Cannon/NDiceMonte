"""
create a histogram showing the distribution of the maximum value pools
of six d20s with the maximum value taken
"""
import matplotlib.pyplot as plt
import numpy as np

from n_dice_monte import sim_pool
from n_dice_monte import histogram

SIM_SIZE = 500000
DICE_SIZE = 6

sim_arr = sim_pool(SIM_SIZE, DICE_SIZE, pool_size=2)
avg = np.mean(sim_arr)

fig, ax = plt.subplots()

ax = histogram(sim_arr, DICE_SIZE)
ax.legend(title=f"Mean is {avg}", loc='upper left', reverse=True)
ax.set_title('Basic d6 distribution')

plt.show()
#plt.savefig("./dev/d6_basic.jpg")
