#! /bin/python3
# vim: set fileencoding=utf-8
#
# (c) July 6, 2023, José Martinez, Polytech Nantes, University of Nantes
#
# Licence:  proprietary
# The use of this library is not authorised outside the Polytechnic School of the University of Nantes.
#


__all__ = [ 'jug_solver_DC, jug_solver_DL, jug_solver_BB' ]


from typing import Tuple, List, Union

# import Solver_Naive as SN # DON'T DO THAT!
import Solver_DirectedCycle as DC # First usable solver
import Solver_DepthLimit as DL # Possibly modify the depth parameter
import Solver_BranchAndBound as BB # Possibly modify the depth and bound parameters, and possibly add a heuristics


Quantity    = int
Capacity    = int
Jug         = Tuple[Quantity, Capacity]
Description = Union[Tuple[str, int], Tuple[str, int, str, int]]
State       = List[Jug]
Cost        = int
Transition  = Tuple[Description, State, Cost]
Solution    = List[Transition]


def quantity (j:  Jug) -> int:  return j[0]
def capacity (j:  Jug) -> int:  return j[1]
def free_capacity (j:  Jug) -> Capacity:  return j[1] - j[0]
def is_empty (j:  Jug) -> bool:  return j[0] == 0
def is_full (j:  Jug) -> bool:  return j[0] == j[1]
def empty (j:  Jug) -> Jug:  return (0, j[1])
def fill (j:  Jug) -> Jug:  return (j[1], j[1])


def jugs_operations (s:  State) -> List[Transition]:

    def jugs_empty (jugs: State) -> List[Transition]:
        return [ ( ("empty", i),
                    s[:i] + [empty(j)] + s[i + 1:],
                    quantity(j) )
                 for (i, j) in enumerate(jugs)
                 if not is_empty(j) ]


    def jugs_fill (jugs: State) -> List[Transition]:
        return [ ( ("fill", i),
                   s[:i] + [fill(j)] + s[i + 1:],
                   free_capacity(j) )
                 for (i, j) in enumerate(jugs)
                 if not is_full(j) ]


    def jugs_transfer (jugs: State) -> List[Transition]:
        return [ ( ("transfer from", i1, "to", i2),
                   s[:i_min] + [j_min] + s[i_min + 1:i_max - 1] + [j_max] + s[i_max + 1:],
                   q )
                 for (i1, j1) in enumerate(jugs)
                 if not is_empty(j1)
                 for (i2, j2) in enumerate(jugs)
                 if i1 != i2
                 if not is_full(j2)
                 for q in [ min(quantity(j1), free_capacity(j2)) ] # let
                 for (j1_new, j2_new) in [ ( (quantity(j1) - q, capacity(j1)),
                                             (quantity(j2) + q, capacity(j2)) ) ] # let
                 for (i_min, j_min, i_max, j_max) in [ (i1, j1_new, i2, j2_new) if i1 < i2 else
                                                       (i2, j2_new, i1, j1_new) ] ]

    return jugs_empty(s) + jugs_fill(s) + jugs_transfer(s)


def jugs_solver_DC (jugs:  State,
                    i:     int,
                    q:     Quantity) -> List[Solution]:
    """
    Instantiation of a general solver with the jug problem specific arguments, i.e., 'jug_moves' for generating the successor states and 'jug_solved' for recognising a solution.
    
    :param jugs:  A jug puzzle initial state.
    :param i:  The indice of one of the jugs.
    :param q:  The quantity of water that we want to obtain in jug #i.
    :return:  The list of solutions, themselves lists of states along with explanation and cost of the used elementary operations
    """

    def is_solved (jugs:  State) -> bool:  return any([ quantity(j) == q for j in jugs ]) # does not work as a lambda function ...

    assert 0 <= i < len(jugs)
    return DC.solver(jugs_operations, is_solved, jugs)


def jugs_solver_DL (d_max:  int,
                    jugs:  State,
                    i:     int,
                    q:     Quantity) -> List[Solution]:

    def is_solved (jugs:  State) -> bool:  return any([ quantity(j) == q for j in jugs ])
    
    assert 0 <= i < len(jugs)
    return DL.solver(jugs_operations, is_solved, jugs, d_max)


def jugs_solver_BB (d_max: int,
                    b: int,
                    jugs:  State,
                    i:     int,
                    q:     Quantity) -> List[Solution]:

    def is_solved (jugs:  State) -> bool:  return any([ quantity(j) == q for j in jugs ])
    
    assert 0 <= i < len(jugs)
    return BB.solver(jugs_operations, is_solved, lambda _: 0, [], d_max, b, jugs) # type:  ignore # for SolverBranchAndBound


if __name__ == "__main__":
    print(">>> Directed-cycle solver")
    for (i, s) in enumerate(jugs_solver_DC([(0, 3), (0, 5)], 1, 4), 1):
        print("Solution #{} for a cost of {} at depth {}".format(i, sum([ c for (_, _, c) in s ]), len(s)))
        for t in s:
            print("   ", t)
    print()
    print("=====================================================================")
    print()
    print(">>> Depth-limit solver (with depth-limit set to 9)")
    for (i, s) in enumerate(jugs_solver_DL(9, [(0, 3), (0, 5)], 1, 4), 1):
        print("Solution #{} for a cost of {} at depth {}".format(i, sum([ c for (_, _, c) in s ]), len(s)))
        for t in s:
            print("   ", t)
    print()
    print("=====================================================================")
    print()
    print(">>> Branch-and-bound solver (with depth-limit set to 10 and cost-bound set to 27)")
    for (i, s) in enumerate(jugs_solver_BB(10, 27, [(0, 3), (0, 5), (0, 11)], 2, 7), 1):
        print("Solution #{} for a cost of {} at depth {}".format(i, sum([ c for (_, _, c) in s ]), len(s)))
        for t in s:
            print("   ", t)

