"""
creating a histogram showing the distribution of the maximum value pools of six d20s with the maximum value taken
"""

from src.n_dice_monte import sim_max
from src.n_dice_monte import histogram

dice_face = 20

sim_arr = sim_max(dice_face, 6, 500)

histogram(sim_arr, dice_face)
