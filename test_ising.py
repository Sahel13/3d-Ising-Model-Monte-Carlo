from ising import *
import numpy as np

def test_get_neighbours():
    L = 5
    examples = {
        '01': {
            'location': (3,3),
            'neighbours': [(3, 2), (2, 3), (3, 4), (4, 3)]
        },
        '02': {
            'location': (4, 4),
            'neighbours': [(4, 3), (3, 4), (4, 0), (0, 4)]
        }
    }
    checks_passed = True

    for key in examples:
        row, col = examples[key]['location']
        neighbours = get_neighbours(row, col, L)

        if neighbours != examples[key]['neighbours']:
            checks_passed = False
            break

    assert checks_passed


def test_get_magnetization():
    L = 4
    state = np.ones((L, L))
    magnetization = get_magnetization(state, L)
    assert magnetization == 16.0


def test_get_energy():
    L = 4
    state = np.ones((L, L))
    energy = get_energy(state, L)
    assert energy == -32.0
