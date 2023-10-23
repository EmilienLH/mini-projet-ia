#! /bin/python3
# vim: set fileencoding=utf-8
#
# (c) March 20, 2019, July 5, 2023 José Martinez, Polytech Nantes, University of Nantes
#
# Licence:  proprietary
# The use of this library is not authorised outside the Polytechnic School of the University of Nantes.
#


__all__ = ['solver']


from typing import TypeVar, Callable, Tuple, List, Union


State       = TypeVar('State')
Description = TypeVar('Description')
Cost        = TypeVar('Cost')
Transition  = Tuple[Description, State, Cost]
Solution    = List[Transition]


def solver (successors:  Callable[[State], List[Transition]],
            isFinal:     Callable[[State], bool],
            heuristic:   Callable[[State], Union[int, float]],
            ancestors:   List[State],
            depth:       int,
            bound:       Union[int, float],
            state:       State) -> List[Solution]:
    """
    An advanced backtracking solver with two simple strategies and a more complex one combined together.

    Firstly, a directed cycle detection is enforced.
    This allows to avoid pseudo infinite graphs, i.e., loops between a node and one of its ancestors in a path from the initial state to itself.

    Secondly, a depth limit is enforced.
    This avoids infinite searches into actually infinite graphs, though it also prohibits finding deep solutions.
    It would also alleviate the problem of loops, but their detection may be way too deep.

    Finally, if offers an informed branch-and-bound strategy, i.e., a way to guide the search in the most promising part of the graph.
    Furthermore, this ensures, through a somewhat exhaustive search, to find one of the very best solutions, though only one of them if there exist ex aequo solutions.
    Notice, that some problems can exhibit an exponential number of solutions with the very same cost.
    So, it turns to be a wise solution to retrieve only one.
    Should the user be really interested in finding several, or even all the solutions with the best cost, he or she can run another solver looking for the solutions with the given cost.

    :param successors:  The function that return the successors of a given state.
    :param isFinal:  The predicate that determines whether a state is a solution.
    :param heuristic:  A function that evaluates the minimal cost to reach a solution from the current state.
    :param ancestors:  The list of states from the initial one to the current one.
    :param bound:  The /strictly/ maximal cost of a solution.
    :param d_max:  The maximal depth at which a solution is to be found.
    :param state:  The initial state from which to explore the state graph of the problem.
    :return:  A sequence of solutions down to /one/ of the best solutions.

    :post:  For a solution, the sequence of steps is indeed a solution.
    :post:  No solution can be of length greater than the depth limit.
    :post:  No solution has a cost higher than the cost bound.
    :post:  No solution contains the same state twice or more.
    :post:  Solutions appear in strictly decreasing cost order.
    """
    if depth < 0 or state in ancestors or bound < 0:
        return []
    elif isFinal(state):
        return [[]]
    else:
        branches = sorted([ ((d, s, c), hc)
                            for (d, s, c) in successors(state)
                            if c < bound
                            for hc in [c + heuristic(s)] # let
                            if hc < bound ],
                          key = lambda k: k[1])
        solutions = [] # type: List[Solution]
        ancestors_union_state = ancestors + [state]
        depth_minus_1 = depth - 1
        for ((d, s, c), hc) in branches:
            for solution in solver(successors, isFinal, heuristic, ancestors_union_state, depth_minus_1, bound - c, s):
                solutions = solutions + [[(d, s, c)] + solution]
                assert c + sum([ c for (_, _, c) in solution ]) < bound
                bound = c + sum([ c for (_, _, c) in solution ])
        return solutions


if __name__ == "__main__":
    pass

