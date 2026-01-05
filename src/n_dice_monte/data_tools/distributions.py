"""
some functions to calculate distributions such as means or quartiles
"""

import numpy as np

def am_array(sim_data):
    """
    create a 1d array of means from a 2d array of simulations
    each simulation occupies an individual row of the data array
    """

    #determine how many simulation rows there are and construct array
    sim_count = np.shape(sim_data)[0]

    #construct array to be used for storing arithmatic means
    means = np.array(sim_count)

    for x in range(sim_count):
        means[x]=np.mean(sim_data[x])

    return means