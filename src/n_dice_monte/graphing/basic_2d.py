"""
basic graphing functions for 2d representations
"""

import matplotlib.pyplot as plt
import numpy as np

def histogram( sim_data, dice_size, sim_width = 1):
    """
    creation of a 2d histogram for visualizing dice results
    """

    if sim_width == 1:
        parsed_data = sim_data
    else:
        parsed_data = np.zeros(sim_data.size)

    #generate a single histogram
    return plt.hist(parsed_data, dice_size, [1, dice_size], density=True)
