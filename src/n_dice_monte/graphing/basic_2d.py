"""
basic graphing functions for x-y representations
"""

import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np

def histogram( sim_data, max_val, min_val=1, style='stepfilled',
    colors=('xkcd:cerulean',), stack=False, name=("",)):
    """
    creation of a 2d histogram for visualizing dice results

    sim_data is input data, max_val is the maximum value a group of data can be,
    min_val is the minimum value, sim_width is how many dice per simulation pool,
    colors are xkcd color names, stack and style are graph settings
    """

    _fig, ax = plt.subplots()

    #generate a single histogram
    ax.hist(sim_data, bins=np.arange(min_val,max_val+2, dtype=int)-0.5,
        range=[min_val, max_val], density=True, histtype=style, color=colors,
        stacked=stack, label=name)

    ax.set_xlabel('Roll Value')
    ax.set_ylabel('Chance')
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))


    return ax
