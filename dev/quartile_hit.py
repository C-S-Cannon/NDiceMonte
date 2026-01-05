"""
create an errorplot showing the the mean on the x axis with the quartiles as error bars and
the simulation label on the y axis
"""

import numpy as np
import matplotlib.pyplot as plt

from n_dice_monte import sim_max, xqrt_plot, DSize

#how many iterations to run simulation
SIM_SIZE = 10000

#minimum and maximum values representable within simulation data
MAX_VAL = DSize.D20 + DSize.D6
MIN_VAL = 0

#array of SIM_SIZE length filled with MIN_VAL
SIM_MIN = np.full(SIM_SIZE, MIN_VAL)

#names of simulations
sim_list = np.array(["2d6 difficulty", "flat roll", "1d6 accuracy"])

#create header array
sim_data = np.full(SIM_SIZE, -1)

#create a loop to iterate simulation
for d20 in range(1,3):
    #create d20 simulations without accuracy
    sim_data = np.vstack((sim_data, sim_max(SIM_SIZE, DSize.D20, d20)))

    #vertically append simulations with accuracy
    for accuracy in range(1,4):
        #create d20 simulation upon which to project accuracy
        sim_data = np.vstack((sim_data, sim_max(SIM_SIZE, DSize.D20, d20)))
        #project accuracy
        sim_data[sim_data.shape[0]-1] = (
            sim_data[sim_data.shape[0]-1] + sim_max(SIM_SIZE, DSize.D6, accuracy))

    #vertically append simulations with difficulty
    for difficulty in range(1,4):
        #create d20 simulation upon which to project accuracy
        sim_data = np.vstack((sim_data, sim_max(SIM_SIZE, DSize.D20, d20)))
        #project difficulty
        sim_data[sim_data.shape[0]-1] = (
        sim_data[sim_data.shape[0]-1] - sim_max(SIM_SIZE, DSize.D6, accuracy))

#trim simulation header
sim_data = np.delete(sim_data, 0, 0)

_fig, ax = plt.subplots()

ax = xqrt_plot(sim_data, MAX_VAL, MIN_VAL, sim_list)
ax.axvline(x=20, color="grey", linestyle=":")

plt.show()
