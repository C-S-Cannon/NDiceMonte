"""
a collection of functions to allow the creation of data sets for dice
"""

import numpy as np

from .dice import Dice


def sim_max(dice_size, pool_size, sim_size):
    """
    create an array holding of the max value rolled for a pool of dice across some arbitrary size
    """

    dice = Dice(dice_size)
    sim_arr = np.zeros(sim_size)

    for x in range(sim_size):
        sim_arr[x] = dice.roll_max(pool_size)

    return sim_arr
