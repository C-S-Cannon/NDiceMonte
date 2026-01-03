"""
create a histogram showing the distribution of the maximum value pools
of six d20s with the maximum value taken
"""

from n_dice_monte import sim_max
from n_dice_monte import histogram

DICE_FACE = 20

sim_arr = sim_max(DICE_FACE, 6, 500)

histogram(sim_arr, DICE_FACE)
