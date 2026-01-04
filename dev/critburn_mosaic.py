"""
create two stacked histograms showing distribution of hit and damage
stacked histogram showing hitrates with accuracy on [1,1]
stacked histogram showing crit and non crit damage on [1,2]
"""
import matplotlib.pyplot as plt
import numpy as np

from n_dice_monte import sim_max
from n_dice_monte import histogram

SIM_SIZE = 5000
D6_SIZE = 6
D20_SIZE = 20

d20_sim = sim_max(SIM_SIZE, D20_SIZE, pool_size=2)
d6_sim = np.zeros((3, SIM_SIZE))
d6_sim[0] = sim_max(SIM_SIZE, D6_SIZE)
d6_sim[1] = sim_max(SIM_SIZE, D6_SIZE, pool_size=2)
d6_sim[2] = sim_max(SIM_SIZE, D6_SIZE, pool_size=3)
critd6_sim = sim_max(SIM_SIZE, D6_SIZE, pool_size=2, mface=2)

accuracy = np.zeros((4, SIM_SIZE))
accuracy[0] = d20_sim

for x in range(SIM_SIZE):
    for n in range(3):
        accuracy[n+1, x] = d20_sim[x] + d6_sim[n, x]

#avg = np.mean(sim_arr)

colors = ['xkcd:lightblue', 'xkcd:turquoise', 'xkcd:goldenrod', 'xkcd:terracotta']
names = ['No Accuracy', '1d6 accuracy', '2d6 accuracy', '3d6 accuracy']

fig, ax = plt.subplots(2)

ax[0] = histogram(np.transpose(accuracy), (D20_SIZE+D6_SIZE), stack=True, colors=colors, name=names)
ax[0].legend(loc='upper left', reverse=True)
ax[0].set_title('Distribution of Accuracy')
ax[1].set_title('Distribution of Damage')

#plt.show()
plt.savefig("./dev/deathshead.jpg")
