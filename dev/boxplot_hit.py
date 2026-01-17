"""
create a boxplot showing the a mean/quartile distribution in the box and 90% within bars
the simulation labels are on the y axis

matplot boxplot demo link
https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html
"""

import numpy as np
import matplotlib.pyplot as plt

from n_dice_monte import sim_max, xbox_plot, DSize

#how many iterations to run simulation
SIM_SIZE = 3000000

#minimum and maximum values representable within simulation data
MAX_VAL = DSize.D20 + DSize.D6
MIN_VAL = 0

#array of d20 combinations to simulate
D20_COMB = [1,2,4]

#array of SIM_SIZE length filled with MIN_VAL
SIM_MIN = np.full(SIM_SIZE, MIN_VAL)

#array header for simulation names
sim_name = np.array([""])

#array header for simulation data
sim_data = np.full(SIM_SIZE, -1)

#tuple header for colors
colors = ["",]

#create a loop to iterate simulation
for d20 in D20_COMB:

    #vertically append simulations with difficulty
    for difficulty in reversed(range(1,4)):
        #create d20 simulation upon which to project difficulty
        sim_data = np.vstack((sim_data, sim_max(SIM_SIZE, DSize.D20, d20)))
        #project difficulty
        sim_data[sim_data.shape[0]-1] = (
        sim_data[sim_data.shape[0]-1] - sim_max(SIM_SIZE, DSize.D6, difficulty))
        #append simulation name
        sim_name = np.append(sim_name, f"{d20}d20 +{difficulty} dif")
        #append simulation color
        colors.append("xkcd:red")

    #vertically append d20 simulations without accuracy or difficulty
    sim_data = np.vstack((sim_data, sim_max(SIM_SIZE, DSize.D20, d20)))
    #append simulation name to end of array
    sim_name = np.append(sim_name, f"{d20}d20 flat")
    #append simulation color
    colors.append("xkcd:green")


    #vertically append simulations with accuracy
    for accuracy in range(1,4):
        #create d20 simulation upon which to project accuracy
        sim_data = np.vstack((sim_data, sim_max(SIM_SIZE, DSize.D20, d20)))
        #project accuracy
        sim_data[sim_data.shape[0]-1] = (
            sim_data[sim_data.shape[0]-1] + sim_max(SIM_SIZE, DSize.D6, accuracy))
        #append simulation name
        sim_name = np.append(sim_name, f"{d20}d20 +{accuracy} acc")
        #append simulation color
        colors.append("xkcd:cerulean")

#trim simulation header
sim_data = np.delete(sim_data, 0, 0)
#trim simulation names header
sim_name = np.delete(sim_name, 0)
#trim color header
colors.pop(0)

fig, ax = plt.subplots()

ax = xbox_plot(sim_data, MAX_VAL, MIN_VAL, name=sim_name, colors=colors)
ax.axvline(x=20, color="grey", linestyle=":")
fig.suptitle("Lancer Attack Roll Distributions")
ax.set_title("Bar is mean, 50% of rolls are inside box, 90% are inside whiskers")

plt.show()
#plt.savefig("./dev/attack_roll_distribution.jpg")
