import numpy as np

J_ising = 1.0  # Coupling strength

def initialize_lattice(L):
    """
    Generate a random spin configuration for the initial state.
    """
    initial_state = np.random.randint(2, L)
    return initial_state


def get_neighbours(row, col, L):
    """
    Find the neighbours of a given spin site
    according to periodic boundary conditions.
    """
    l = L - 1
    row_down = row + 1 if row < l else 0
    row_up = row - 1 if row > 0 else l
    col_left = col - 1 if col > 0 else l
    col_right = col + 1 if col < l else 0

    return [(row, col_left), (row_up, col), (row, col_right), (row_down, col)]


def get_magnetization(state, L):
    """
    Get the magnetization of a given state.
    """
    M = 0
    for row in range(L):
        for col in range(L):
            M += state[row, col]

    return M


def get_energy(state, L):
    """
    Get the energy of a given state.
    """
    E = 0
    for row in range(L):
        for col in range(L):
            for (i, j) in get_neighbours(row, col, L):
                E -= J_ising * state[row, col] * state[i, j]
    return E * 0.5
