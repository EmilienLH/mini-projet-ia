#! /bin/python3
# vim: set fileencoding=utf-8
#
# (c) July 5, 2023, José Martinez, Polytech Nantes, University of Nantes
#
# Licence:  proprietary
# The use of this library is not authorised outside the Polytechnic School of the University of Nantes.
#


__all__ = ['solver']


from typing import TypeVar, Callable, Tuple, List, Union
from MetaSolver_IteratedDeepening import meta_solver
import Solver_BranchAndBound as BB


State       = TypeVar('State')
Description = TypeVar('Description')
Cost        = TypeVar('Cost')
Transition  = Tuple[Description, State, Cost]
Solution    = List[Transition]


def solver (successors:  Callable[[State], List[Transition]],
            isFinal:     Callable[[State], bool],
            heuristic:   Callable[[State], Union[int, float]],
            ancestors:   List[State],
            bound:       Union[int, float],
            d_max:       int,
            initial:     State) -> List[Solution]:
    """
    A solver based on the depth-limit solver but that uses the meta-heuristic of depth-deepening.

    :param successors:  The function that return the successors of a given state.
    :param isFinal:  The predicate that determines whether a state is a solution.
    :param isFinal:  The predicate that determines whether a state is a solution.
    :param heuristic:  A function that evaluates the minimal cost to reach a solution from the current state.
    :param ancestors:  The list of states from the root one to the current one.
    :param bound:  The /strictly/ maximal cost of a solution.
    :param d_max:  The maximal depth at which a solution is to be found.
    :param initial:  The initial state from which to explore the state graph of the problem.
    :return:  A list of alternative solutions at some minimal depth up to the maximal depth limit.

    :bug:  The bound should be updated from a level to the next in order to avoid duplicated solutions.
    """

    def curried_solver (d_max:    int,
                        initial:  State) -> List[Solution]:
        """
        Encapsulation of the actual solver in order to use it with the iterated-deepening meta-solver interface.
        """
        return BB.solver(successors, isFinal, heuristic, ancestors, d_max, bound, initial)

    return meta_solver(curried_solver, d_max, initial)


if __name__ == "__main__":
    pass

