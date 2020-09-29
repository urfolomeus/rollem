import random

def roll(roll_string, seed=None):
    # allows us to avoid randomness in tests, will be random as long as seed is
    # not set
    random.seed(seed)

    return random.randrange(6)
