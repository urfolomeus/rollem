import random
import re

from functools import reduce

# needs to be a raw string in order to avoid deprecation warnings
# https://stackoverflow.com/a/50504635
DICE_STRING_MATCHER = r'(\d*)d(100|20|12|10|8|6|4|3|2)\+?([-\d]*)'

MULTIPLIER_INDEX = 1
DIE_INDEX = 2
MODIFIER_INDEX = 3

def roll(dice_string, seed=None):
    # allows us to avoid randomness in tests, will be random as long as seed is
    # not set
    random.seed(seed)

    match = re.search(DICE_STRING_MATCHER, dice_string)

    multiplier = match[MULTIPLIER_INDEX] or 1
    multiplier = int(multiplier)

    die = int(match[DIE_INDEX])

    modifier = match[MODIFIER_INDEX] or 0
    modifier = int(modifier)

    result = reduce(
        lambda memo, value: memo + random.randrange(die), range(multiplier), 0
    )

    return result + modifier
