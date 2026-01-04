"""
basic graphing functions for x-y representations
"""

import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np

def major_ticks(max_val):
    """
    accepts the maximum value of a histogram and returns an array of appropriate major ticks
    """

    tick_count = 0
    if max_val<=6:
        tick_count = max_val
    elif max_val<=30:
        tick_count = max_val/2
    elif max_val <=50:
        tick_count = max_val/5
    else:
        tick_count = 10

    tick_count = int(tick_count)
    ticks = np.zeros(tick_count)

    for x in range(tick_count):
        ticks[x] = int((x+1) * max_val / tick_count)

    return ticks

def minor_ticks(max_val):
    """
    accepts the maximum value of a histogram and returns an array of appropriate minor ticks
    """

    ticks = np.zeros(max_val)
    for x in range(max_val):
        ticks[x] = x+1

    return ticks

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
    _n, _bins, _patches = ax.hist(sim_data,
        bins=np.arange(min_val,max_val+2, dtype=int)-0.5, range=[min_val, max_val],
        density=True, histtype=style, color=colors, stacked=stack, label=name)


    ax.set_xlabel('Roll Value')
    ax.set_ylabel('Chance')

    #convert y axis to display as a percentage chance rather than norm from 1
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))

    #set x axis tick locations and values
    ax.set_xticks(major_ticks(max_val))
    ax.set_xticks(minor_ticks(max_val), minor=True)

    return ax

def layer_hist(sim_data, max_val, min_val=1, style='stepfilled',
    colors=('xkcd:cerulean',), stack=False, name=("",)):
    """
    creation of a 2d histogram for visualizing dice results

    sim_data is input data, max_val is the maximum value a group of data can be,
    min_val is the minimum value, sim_width is how many dice per simulation pool,
    colors are xkcd color names, stack and style are graph settings
    """
    _fig, ax = plt.subplots()

    #iterate once for each row in data array
    for x in range(np.shape(sim_data)[0]):
        #generate a 2d layered histogram
        _n, _bins, _patches = ax.hist(np.flip(sim_data, axis=0)[x],
        bins=np.arange(min_val,max_val+2, dtype=int)-0.5, range=[min_val, max_val], density=True,
        histtype=style, color=np.flip(colors)[x], stacked=stack, label=np.flip(name)[x])


    ax.set_xlabel('Roll Value')
    ax.set_ylabel('Chance')

    #convert y axis to display as a percentage chance rather than norm from 1
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))

    ax.set_xticks(major_ticks(max_val))
    ax.set_xticks(minor_ticks(max_val), minor=True)

    return ax
