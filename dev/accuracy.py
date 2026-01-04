"""
create two stacked histograms showing distribution of hit and damage
stacked histogram showing hitrates with accuracy on [1,1]
stacked histogram showing crit and non crit damage on [1,2]
"""
import matplotlib.pyplot as plt
import numpy as np

from n_dice_monte import sim_max
from n_dice_monte import histogram

#plt.rcParams['text.usetex'] = True
SIM_SIZE = 5000000
D6_SIZE = 6
D20_SIZE = 20
SIM_RUNS = 3

d6_sim = np.zeros((SIM_RUNS, SIM_SIZE))
d6_sim[0] = sim_max(SIM_SIZE, D6_SIZE)
d6_sim[1] = sim_max(SIM_SIZE, D6_SIZE, pool_size=2)
d6_sim[2] = sim_max(SIM_SIZE, D6_SIZE, pool_size=3)

avg = np.zeros(SIM_RUNS)
for x in range(SIM_RUNS):
    avg[x] = np.mean(d6_sim[x])

colors = ['xkcd:lightblue', 'xkcd:turquoise', 'xkcd:goldenrod']
names = ["1d6 accuracy, AM={:.2f}".format(avg[0]),
    "2d6 accuracy, AM={:.2f}".format(avg[1]), "3d6 accuracy, AM={:.2f}".format(avg[2])]

fig, ax = plt.subplots()

ax = histogram(np.transpose(d6_sim), (D6_SIZE),style='bar', colors=colors, name=names)
ax.legend(loc='upper left', reverse=True)
ax.set_title('Distribution of Accuracy')

plt.show()
plt.savefig("./dev/accuracy.jpg")
