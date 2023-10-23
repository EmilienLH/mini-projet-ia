#! /bin/python3
# vim: set fileencoding=utf-8
#
# (c) February 28, 2019, July 20, 2022, José Martinez, Polytech Nantes, University of Nantes
#
# Licence:  proprietary
# The use of this library is not authorised outside the Polytechnic School of the University of Nantes.
#


__all__ = ['solver']


from typing import TypeVar, Callable, Tuple, List


State       = TypeVar('State')
Description = TypeVar('Description')
Cost        = TypeVar('Cost')
Transition  = Tuple[Description, State, Cost]
Solution    = List[Transition]


def solver (transformations:  Callable[[State], List[Transition]],
            isFinal:          Callable[[State], bool],
            state:            State) -> List[Solution]:
    """
    A very basic backtracking solver.

    :param transformations:  The function that return the successors of a given state.
    :param isFinal:  The predicate that determines whether a state is a solution.
    :param state:  A state from which to explore the state graph of the problem.
    :return:  A list of alternative solutions.
    """
    return ([[]] if isFinal(state) else
            [ [(d, s, c)] + solution
              for (d, s, c) in transformations(state)
              for solution in solver(transformations, isFinal, s) ])


if __name__ == "__main__":
    pass

