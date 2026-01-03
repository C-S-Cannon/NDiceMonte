"""
basic graphing functions for x-y representations
"""

import matplotlib.pyplot as plt
#import numpy as np

def histogram( sim_data, dice_size, min_face=1, style='stepfilled',
    colors=('xkcd:cerulean',), stack=False, name=("",)):
    """
    creation of a 2d histogram for visualizing dice results

    sim_data is input data, dice_size is the number of dice faces,
    min_face is the starting face of the dice, sim_width is how many dice per simulation pool,
    colors are xkcd color names, stack and style are graph settings
    """

    #generate a single histogram
    ax = plt.hist(sim_data, dice_size, [min_face, dice_size],
        density=True, histtype=style, color=colors, stacked=stack, label=name)
    return ax
