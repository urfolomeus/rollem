from rollem import __version__, roller

# Set the seed when using the random generator in tests to avoid randomness
BASE_SEED = 1

# If we seed the random number generator with 1 then the following are the
# values returned for each of the permitted die types
SEED_1_VALUES = {
    'd2': [0,0],
    'd3': [0,2],
    'd4': [1,0],
    'd6': [1,4],
    'd8': [2,1],
    'd10': [2,9],
    'd12': [2,9],
    'd20': [4,18],
    'd100': [17,72],
}


def test_version():
    assert __version__ == '0.1.0'


def test_d2():
    assert roller.roll("d2", BASE_SEED) == SEED_1_VALUES['d2'][0]


def test_2d2():
    assert roller.roll("2d2", BASE_SEED) == SEED_1_VALUES['d2'][0] + SEED_1_VALUES['d2'][1]


def test_d3():
    assert roller.roll("d3", BASE_SEED) == SEED_1_VALUES['d3'][0]


def test_2d3():
    assert roller.roll("2d3", BASE_SEED) == SEED_1_VALUES['d3'][0] + SEED_1_VALUES['d3'][1]


def test_d4():
    assert roller.roll("d4", BASE_SEED) == SEED_1_VALUES['d4'][0]


def test_2d4():
    assert roller.roll("2d4", BASE_SEED) == SEED_1_VALUES['d4'][0] + SEED_1_VALUES['d4'][1]


def test_d6():
    assert roller.roll("d6", BASE_SEED) == SEED_1_VALUES['d6'][0]


def test_2d6():
    assert roller.roll("2d6", BASE_SEED) == SEED_1_VALUES['d6'][0] + SEED_1_VALUES['d6'][1]


def test_d8():
    assert roller.roll("d8", BASE_SEED) == SEED_1_VALUES['d8'][0]


def test_2d8():
    assert roller.roll("2d8", BASE_SEED) == SEED_1_VALUES['d8'][0] + SEED_1_VALUES['d8'][1]


def test_d10():
    assert roller.roll("d10", BASE_SEED) == SEED_1_VALUES['d10'][0]


def test_2d10():
    assert roller.roll("2d10", BASE_SEED) == SEED_1_VALUES['d10'][0] + SEED_1_VALUES['d10'][1]


def test_d12():
    assert roller.roll("d12", BASE_SEED) == SEED_1_VALUES['d12'][0]


def test_2d12():
    assert roller.roll("2d12", BASE_SEED) == SEED_1_VALUES['d12'][0] + SEED_1_VALUES['d12'][1]


def test_d20():
    assert roller.roll("d20", BASE_SEED) == SEED_1_VALUES['d20'][0]


def test_2d20():
    assert roller.roll("2d20", BASE_SEED) == SEED_1_VALUES['d20'][0] + SEED_1_VALUES['d20'][1]


def test_d100():
    assert roller.roll("d100", BASE_SEED) == SEED_1_VALUES['d100'][0]


def test_2d100():
    assert roller.roll("2d100", BASE_SEED) == SEED_1_VALUES['d100'][0] + SEED_1_VALUES['d100'][1]
