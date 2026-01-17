"""
a collection of functions to allow the creation of data sets for dice
"""

import numpy as np

from .dice import Dice


def sim_max(sim_size, dice_size, pool_size=1, mface=1):
    """
    create an array holding of the max value rolled for a pool of dice across some arbitrary size
    """

    dice = Dice(dice_size, min_face=mface)
    sim_arr = np.zeros(sim_size)

    for x in range(sim_size):
        sim_arr[x] = dice.roll_max(pool_size)

    return sim_arr

def sim_pool(sim_size, dice_size, pool_size=1, mface=1):
    """
    create an array holding the total value rolled for a pool of dice across some arbitrary size
    """

    dice = Dice(dice_size, min_face=mface)
    sim_arr = np.zeros(sim_size)

    for x in range(sim_size):
        sim_arr[x] = np.sum(dice.roll(pool_size))

    return sim_arr