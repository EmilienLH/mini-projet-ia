#! /bin/python3
# vim: set fileencoding=utf-8
#
# (c) March 1st, 2019, July 20, 2022, José Martinez, Polytech Nantes, University of Nantes
#
# Licence:  proprietary
# The use of this library is not authorised outside the Polytechnic School of the University of Nantes.
#


__all__ = [ 'frog_solver',
            'canonical_frog_solver' ]


from typing import TypeVar, Tuple, List, Any
from itertools import dropwhile
from Utilities import splits_2, splits_3

from Solver_Naive import solver


GreenFrog = ' > '
RedFrog   = ' < '
WaterLily = ' _ '


Element     = str
State       = List[Element]
Description = str
Cost        = int
Transition  = Tuple[Description, State, Cost]
Solution    = List[Transition]


def frog_solver (state:  State) -> List[Solution]:
    """
    Instantiation of a general solver with the frog problem specific arguments, i.e., 'frog_moves' for generating the successor states and 'frog_solved' for recognising a solution.
    
    :param state:  A frog puzzle state
    :return:       The list of solutions, themselves lists of states along with explanation and cost of the used elementary operations
    """
    return solver(frog_moves, frog_solved, state)


def canonical_frog_solver (n_green:  int,
                           n_lily:   int,
                           n_red:    int) -> List[Solution]:
    return solver(frog_moves, frog_solved, canonical_frog_puzzle(n_green, n_lily, n_red))


def canonical_frog_puzzle (n_green:  int,
                           n_lily:   int,
                           n_red:    int) -> State:
    """
    A standard initial state consists of a series of green frogs ready to cross over a sequence of red frogs, both parties being separated by (a single) water lilies.

    :param n_green:  The number of green frogs, on the left.
    :param n_lily:   The number of water lilies, in the middle.
    :param n_red:    The number of red frogs, on the right.
    :return:         The corresponding canonical puzzle.
    """
    return [GreenFrog] * n_green + [WaterLily] * n_lily + [RedFrog] * n_red


def frog_moves (state:  State) -> List[Transition]:
    """
    This function generates all the successors of a given state, obeying some movement rule.
    Currently, there are only two rules.
    Either a frog can advance to the next place if it is empty, or it can jump over an opposite frog if the place located after is free.

    :param state:  a frog puzzle state
    :return:       the list of positions that can be reached from s within a single frog walk    
    """
    return green_frog_advances(state) + red_frog_advances(state) + green_frog_jumps(state) + red_frog_jumps(state)


def green_frog_advances (state:  State) -> List[Transition]:
    return [ ("green_frog_advances", X + [w, g] + Y, 1)
             for (X, g, w, Y) in splits_2(state)
             if (g, w) == (GreenFrog, WaterLily) ]


def red_frog_advances (state:  State) -> List[Transition]:
    return [ ("red_frog_advances", X + [r, w] + Y, 1)
             for (X, w, r, Y) in splits_2(state)
             if (w, r) == (WaterLily, RedFrog) ]


def green_frog_jumps (state:  State) -> List[Transition]:
    return [ ("green_frog_jumps", X + [w, r, g] + Y, 1)
             for (X, g, r, w, Y) in splits_3(state)
             if (g, r, w) == (GreenFrog, RedFrog, WaterLily) ]


def red_frog_jumps (state:  State) -> List[Transition]:
    return [ ("red_frog_jumps", X + [r, g, w] + Y, 1)
             for (X, w, g, r, Y) in splits_3(state)
             if (w, g, r) == (WaterLily, GreenFrog, RedFrog) ]


def frog_solved (state:  State) -> bool:
    """
    a final state consists of any situation where no more frog needs to cross frogs from the opposite party.
    
    :param state:  a frog puzzle state
    :return:       True if, and only if, all the red frogs appear before all the green frogs
    """
    return all([ e in [GreenFrog, WaterLily]
                 for e in dropwhile(lambda x:  x in [RedFrog, WaterLily], state) ])
    
    
if __name__ == "__main__":
    for s in canonical_frog_solver(3, 1, 3):
        print()
        print("".join(canonical_frog_puzzle(3, 1, 3)))
        for t in s:
            print("".join(t[1]))

