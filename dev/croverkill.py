"""
create two stacked histograms showing distribution of hit and damage
stacked histogram showing hitrates with accuracy on [1,1]
stacked histogram showing crit and non crit damage on [1,2]
"""
import matplotlib.pyplot as plt
import numpy as np

from n_dice_monte import sim_max, histogram, mean_last

#plt.rcParams['text.usetex'] = True
SIM_SIZE = 500000
D6_SIZE = 6
D20_SIZE = 20

names = ["",]
colors = ["",]
d6_sim = np.zeros((SIM_SIZE))

d6_sim = np.vstack((d6_sim, sim_max(SIM_SIZE, D6_SIZE)))
#append the mean value to the names array
names.append(f"1d6, AM={mean_last(d6_sim)}")
#append color to colors array
colors.append('xkcd:lightblue')

d6_sim = np.vstack((d6_sim, sim_max(SIM_SIZE, D6_SIZE, mface=2)))
#append the mean value to the names array
names.append(f"1d6 overkill, AM={mean_last(d6_sim)}")
#append color to colors array
colors.append('xkcd:pink')

d6_sim = np.vstack((d6_sim, sim_max(SIM_SIZE, D6_SIZE, pool_size=2)))
#append the mean value to the names array
names.append(f"1d6 crit, AM={mean_last(d6_sim)}")
#append color to colors array
colors.append('xkcd:goldenrod')

d6_sim = np.vstack((d6_sim, sim_max(SIM_SIZE, D6_SIZE, pool_size=2, mface=2)))
#append the mean value to the names array
names.append(f"1d6 overcrit, AM={mean_last(d6_sim)}")
#append color to colors array
colors.append('xkcd:red')

#remove emptly header entries
names.pop(0)
colors.pop(0)
d6_sim = np.delete(d6_sim, 0, 0)

fig, ax = plt.subplots()

ax = histogram(np.transpose(d6_sim), (D6_SIZE),style='bar', colors=colors, name=names)
ax.legend(loc='upper left')
ax.set_title('Distribution of 1d6 Damage')

plt.show()
plt.savefig("./dev/damage.jpg")
