from rotation import *

def algo1(state):
    state = rotate_right(state, -90)  # R'
    state = rotate_top(state, -90)    # U'
    state = rotate_right(state, 90)   # R
    state = rotate_top(state, -90)    # U'
    state = rotate_right(state, -90)  # R'
    state = rotate_top(state, 180)    # U2
    state = rotate_right(state, 90)   # R
    return state

def algo2(state):
    state = rotate_right(state, -90)  # R'
    state = rotate_top(state, 180)   # U2
    state = rotate_right(state, 90)  # R
    state = rotate_top(state, 90)    # U
    state = rotate_right(state, -90)  # R'
    state = rotate_top(state, 90)   # U
    state = rotate_right(state, 90)  # R
    return state


def algo3(state):
    state = rotate_front(state, -90)  # F'
    state = rotate_right(state, 90)   # R
    state = rotate_top(state, 90)  # U
    state = rotate_right(state, -90)    # R'
    state = rotate_top(state, -90)  # U'
    state = rotate_right(state, -90)   # R'
    state = rotate_front(state, 90)  # F
    state = rotate_right(state, 90)  # R

    return state


def algo4(state):
    state = rotate_right(state, -90)  # R'
    state = rotate_front(state, -90)  # F'
    state = rotate_right(state, 90)  # R
    state = rotate_top(state, 90)    # U
    state = rotate_right(state, 90)  # R
    state = rotate_top(state, -90)   # U'
    state = rotate_right(state, -90)  # R'
    state = rotate_front(state, 90)  # F

    return state


def algo5(state):
    state = rotate_front(state, 90)  # F
    state = rotate_right(state, 90)    # R
    state = rotate_top(state, 90)  # U
    state = rotate_right(state, -90)  # R'
    state = rotate_top(state, -90)   # U'
    state = rotate_front(state, -90)  # F'

    return state


def algo6(state):
    state = rotate_right(state, -90)  # R'
    state = rotate_top(state, 90)   # U
    state = rotate_right(state, 180)  # R2
    state = rotate_top(state, -90)   # U'
    state = rotate_right(state, 180)  # R2
    state = rotate_top(state, -90)   # U'
    state = rotate_right(state, 180)  # R2
    state = rotate_top(state, 90)    # U
    state = rotate_right(state, -90)  # R'

    return state


def algo7(state):
    state = rotate_right(state, 180)  # R2
    state = rotate_top(state, 180)    # U2
    state = rotate_right(state, 90)   # R
    state = rotate_top(state, 180)    # U2
    state = rotate_right(state, 180)  # R2

    return state


def algo_fin1(state):
    state = rotate_left(state, 90)  # L
    state = rotate_top(state, -90)  # U'
    state = rotate_right(state, 90)  # R
    state = rotate_top(state, 180)  # U2
    state = rotate_right(state, -90)  # R'
    state = rotate_front(state, 90)  # F
    state = rotate_right(state, 90)  # R
    state = rotate_top(state, 180)  # U2
    state = rotate_right(state, -90)  # R'
    state = rotate_left(state, -90)  # L'
    return state


def algo_fin2(state):
    state = rotate_right(state, 180)  # R2
    state = rotate_bottom(state, -90)  # D'
    state = rotate_right(state, 90)  # R
    state = rotate_top(state, -90)  # U'
    state = rotate_right(state, -90)  # R'
    state = rotate_top(state, 90)  # U
    state = rotate_front(state, 180)  # F2
    state = rotate_top(state, 90)  # U
    state = rotate_right(state, 90)  # R
    state = rotate_top(state, 90)  # U
    state = rotate_right(state, -90)  # R'
    return state


def algo_fin3(state):
    state = rotate_right(state, 90)  # R
    state = rotate_top(state, -90)  # U'
    state = rotate_left(state, 90)  # L
    state = rotate_top(state, 180)  # U2
    state = rotate_right(state, -90)  # R'
    state = rotate_top(state, 90)  # U
    state = rotate_left(state, -90)  # L'
    return state


def algo_fin4(state):
    state = rotate_right(state, 180)  # R2'
    state = rotate_front(state, 180)  # F2
    state = rotate_right(state, 180)  # R2
    return state


def algo_fin5(state):
    state = rotate_right(state, 180)  # R2
    state = rotate_top(state, -90)  # U'
    state = rotate_right(state, 180)  # R2
    state = rotate_top(state, -90)  # U'
    state = rotate_bottom(state, -90)  # D'
    state = rotate_right(state, 180)  # R2
    state = rotate_top(state, -90)  # U'
    state = rotate_right(state, 180)  # R2'
    return state


def algo_fin6(state):
    state = rotate_left(state, 90)  # L
    state = rotate_bottom(state, -90)  # D'
    state = rotate_right(state, 90)  # R
    state = rotate_top(state, 180)  # U2
    state = rotate_right(state, -90)  # R'
    state = rotate_bottom(state, 90)  # D
    state = rotate_left(state, -90)  # L'
    return state