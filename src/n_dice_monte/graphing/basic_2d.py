"""
basic graphing functions for 2d representations
"""

import matplotlib as mpl
import numpy as np

def histogram( sim_data, dice_size, sim_width = 1, hist_color='b'):
    """
    creation of a 2d histogram for visualizing dice results
    """

    if sim_width == 1:
        parsed_data = sim_data
    else:
        parsed_data = np.zeros(sim_data.size)

    mpl.pyplot.hist(parsed_data, dice_size, [1, dice_size], density=True, color=hist_color)
