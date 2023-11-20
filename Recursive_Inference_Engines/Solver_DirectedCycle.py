#! /bin/python3
# vim: set fileencoding=utf-8
#
# (c) February 28, 2019, José Martinez, Polytech Nantes, University of Nantes
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
            initial:          State) -> List[Solution]:
    """
    A basic backtracking solver with directed cycle detection in order to avoid some pseudo infinite searches.

    :param transformations:  The function that return the successors a a given state.
    :param isFinal:  The predicate that determines whether a state is a solution.
    :param initial:  The initial state from which to explore the state graph of the problem.
    :return:  A list of alternative solutions.
    """
    return solver_cycle(transformations, isFinal, initial, []) # type: ignore


def solver_cycle (transformations:  Callable[[State], List[Transition]],
                  isFinal:          Callable[[State], bool],
                  state:            State,
                  ancestors:        List[State]) -> List[Solution]:
    """
    A basic backtracking solver with directed cycle detection in order to avoid some pseudo infinite searches.

    :param transformations:  The function that return the successors of a given state.
    :param isFinal:  The predicate that determines whether a state is a solution.
    :param state:  The current state in the exploration of the state graph of the problem.
    :param ancestors:  The list of states from the initial one to the current one.
    :return:  A list of alternative solutions.
    """
    return []   if state in ancestors else \
           [[]] if isFinal(state)     else \
           [ [(d, s, c)] + solution
             for (d, s, c) in transformations(state)
             for solution in solver_cycle(transformations, isFinal, s, ancestors + [state]) ]
    

if __name__ == "__main__":
    pass

