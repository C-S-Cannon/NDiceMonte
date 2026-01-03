"""
a basic multifunctional dice object that can have a designated size and be rolled

it defaults to a d20 in a pool of 1
"""

import random
import numpy as np

class Dice(object):
    """
    A basic class for dice objects to enable rolling in multiple modes.
    """

    dice_size = 20
    min_face = 1


    def __init__(self, dice_size = 20, min_face = 1):
        self.dice_size = dice_size
        self.min_face = min_face

    def roll(self, dice_pool = 1):
        """
        roll one or more dice as part of a pool, then return results as a numpy array
        """

        results = np.array(dice_pool) #construct array to hold dice pool results

        for x in range(dice_pool): #fill dice pool
            results[x] = random.randint(1,self.dice_size)

            return results

    def roll_max(self, dice_pool = 1):
        """
        roll a pool of dice, and return only the highest value among them
        """
        high_roll = -1

        for _ in range(dice_pool):
            roll = random.randint(self.min_face, self.dice_size)
            high_roll = max(high_roll, roll)

        return high_roll

    def roll_min(self, dice_pool = 1):
        """
        roll a pool of dice and return only the lowest value among them
        """
        low_roll = -1

        for _ in range(dice_pool):
            roll = random.randint(self.min_face, self.dice_size)
            if low_roll == -1:
                low_roll = roll
            else:
                low_roll = min(low_roll,roll)

        return low_roll
