import random
import re

# needs to be a raw string in order to avoid deprecation warnings
# https://stackoverflow.com/a/50504635
DICE_STRING_MATCHER = r'(\d*)d(2|3|4|6|8|10|12|20|100)(\+|-)?(\d*)'

DIE_INDEX = 2

def roll(dice_string, seed=None):
    # allows us to avoid randomness in tests, will be random as long as seed is
    # not set
    random.seed(seed)

    match = re.search(DICE_STRING_MATCHER, dice_string)

    die = int(match[DIE_INDEX])

    return random.randrange(die)
