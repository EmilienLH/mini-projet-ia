#! /bin/python3
# vim: set fileencoding=utf-8
#
# (c) July 5, 2023, José Martinez, Polytech Nantes, University of Nantes
#
# Licence:  proprietary
# The use of this library is not authorised outside the Polytechnic School of the University of Nantes.
#


__all__ = [ 'match_solver' ]


from typing import TypeVar, Tuple, List, Any
from itertools import dropwhile
from Utilities import splits

from Solver_IDS import solver


State       = List[bool]
Description = Tuple[int, int]
Cost        = int
Transition  = Tuple[Description, State, Cost]
Solution    = List[Transition]


def matches_solver (state:  State,
                    d_max:  int) -> List[Solution]:
    return solver(matches_moves, lambda s: all(s), d_max, state)


def matches_moves (state:  State) -> List[Transition]:

    def rules_2 (state:  State) -> List[Transition]:
        return [ ( (2, len(xs)),
                   xs + [ys[1], ys[0]] + ys[2:],
                   2 )
                 for (xs, ys) in splits(state)
                 if len(ys) >= 2
                 if ys[0] != ys[1] ]

    def rules_3 (state:  State) -> List[Transition]:
        return [ ( (3, len(xs)),
                   xs + [not ys[0], not ys[1], not ys[2]] + ys[3:],
                   3 )
                 for (xs, ys) in splits(state)
                 if len(ys) >= 3
                 if ys[0] == ys[1] == ys[2] ]
    
    return rules_2(state) + rules_3(state)


if __name__ == "__main__":
    for (i, s) in enumerate(matches_solver([False, True, False, True, False, True], 7), 1):
        print("Solution #{} de profondeur {} et coût {}".format(i, len(s), sum([ c for (_, _, c) in s ])))
        for ((r, j), ms, c) in s:
            print("   rule #{} at indice {} for a cost of {}:  {}".format(r, j, c, "".join([ ('^' if m else 'v') for m in ms])))

