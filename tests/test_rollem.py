from rollem import __version__, roller

# If we seed the random number generator with 1 then the following are the
# first values returned for each of the permitted die types
SEED_1_FIRST_VALUES = {
    'd6': 1
}

def test_version():
    assert __version__ == '0.1.0'


def test_d6_returns_4():
    assert roller.roll("d6", 1) == SEED_1_FIRST_VALUES['d6']
