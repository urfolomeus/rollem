from rollem import __version__, roller

# Set the seed when using the random generator in tests to avoid randomness
BASE_SEED = 1

# If we seed the random number generator with 1 then the following are the
# first values returned for each of the permitted die types
SEED_1_FIRST_VALUES = {
    'd2': 0,
    'd3': 0,
    'd4': 1,
    'd6': 1,
    'd8': 2,
    'd10': 2,
    'd12': 2,
    'd20': 0,
    'd100': 2,
}

def test_version():
    assert __version__ == '0.1.0'


def test_d2_returns_expected_value():
    assert roller.roll("d2", BASE_SEED) == SEED_1_FIRST_VALUES['d2']


def test_d3_returns_expected_value():
    assert roller.roll("d3", BASE_SEED) == SEED_1_FIRST_VALUES['d3']


def test_d4_returns_expected_value():
    assert roller.roll("d4", BASE_SEED) == SEED_1_FIRST_VALUES['d4']


def test_d6_returns_expected_value():
    assert roller.roll("d6", BASE_SEED) == SEED_1_FIRST_VALUES['d6']


def test_d8_returns_expected_value():
    assert roller.roll("d8", BASE_SEED) == SEED_1_FIRST_VALUES['d8']


def test_d10_returns_expected_value():
    assert roller.roll("d10", BASE_SEED) == SEED_1_FIRST_VALUES['d10']


def test_d12_returns_expected_value():
    assert roller.roll("d12", BASE_SEED) == SEED_1_FIRST_VALUES['d12']


def test_d20_returns_expected_value():
    assert roller.roll("d20", BASE_SEED) == SEED_1_FIRST_VALUES['d20']


def test_d100_returns_expected_value():
    assert roller.roll("d100", BASE_SEED) == SEED_1_FIRST_VALUES['d100']
