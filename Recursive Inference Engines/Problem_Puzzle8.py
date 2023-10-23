#! /bin/python3
# vim: set fileencoding=utf-8
#
# (c) July 6, 2023, José Martinez, Polytech Nantes, University of Nantes
#
# Licence:  proprietary
# The use of this library is not authorised outside the Polytechnic School of the University of Nantes.
#


__all__ = [ 'puzzle8_solver_DL', 'puzzle8_solver_BB', 'puzzle8_solver_IDA' ]


from typing import Tuple, List

# import Solver_Naive as N # DON'T DO THAT!
# import Solver_DirectedCycle as DC # DON'T DO THAT EITHER!
import Solver_DepthLimit as DL # Possibly modify the depth parameter
import Solver_IDS as IDS # Possibly modify the depth
import Solver_BranchAndBound as BB # Possibly modify the depth and bound parameters, and possibly add a heuristics
import Solver_IDA as IDA # Possibly modify the depth and bound parameters, and possibly change the heuristics


Description = str
State       = Tuple[Tuple[str, str, str], Tuple[str, str, str], Tuple[str, str, str]]
Cost        = int
Transition  = Tuple[Description, State, Cost]
Solution    = List[Transition]


def operations (s:  State) -> List[Transition]:

    def right (puzzle: State) -> List[State]:
        ((a, b, c), (d, e, f), (g, h, j)) = puzzle
        return ( [] if a == ' ' or d == ' ' or g == ' ' else
                 [ ((' ', a, c), (d, e, f), (g, h, j)) ] if b == ' ' else
                 [ ((a, ' ', b), (d, e, f), (g, h, j)) ] if c == ' ' else
                 [ ((a, b, c), (' ', d, f), (g, h, j)) ] if e == ' ' else
                 [ ((a, b, c), (d, ' ', e), (g, h, j)) ] if f == ' ' else
                 [ ((a, b, c), (d, e, f), (' ', g, j)) ] if h == ' ' else
                 [ ((a, b, c), (d, e, f), (g, ' ', j)) ] if j == ' ' else
                 [] )

    def left (puzzle: State) -> List[State]:
        ((a, b, c), (d, e, f), (g, h, j)) = puzzle
        return ( [] if c == ' ' or f == ' ' or j == ' ' else
                 [ ((b, ' ', c), (d, e, f), (g, h, j)) ] if a == ' ' else
                 [ ((a, c, ' '), (d, e, f), (g, h, j)) ] if b == ' ' else
                 [ ((a, b, c), (e, ' ', f), (g, h, j)) ] if d == ' ' else
                 [ ((a, b, c), (d, f, ' '), (g, h, j)) ] if e == ' ' else
                 [ ((a, b, c), (d, e, f), (h, ' ', j)) ] if g == ' ' else
                 [ ((a, b, c), (d, e, f), (g, j, ' ')) ] if h == ' ' else
                 [] )

    def up (puzzle: State) -> List[State]:
        ((a, b, c), (d, e, f), (g, h, j)) = puzzle
        return ( [] if g == ' ' or h == ' ' or j == ' ' else
                 [ ((d, b, c), (' ', e, f), (g, h, j)) ] if a == ' ' else
                 [ ((a, e, c), (d, ' ', f), (g, h, j)) ] if b == ' ' else
                 [ ((a, b, f), (d, e, ' '), (g, h, j)) ] if c == ' ' else
                 [ ((a, b, c), (g, e, f), (' ', h, j)) ] if d == ' ' else
                 [ ((a, b, c), (d, h, f), (g, ' ', j)) ] if e == ' ' else
                 [ ((a, b, c), (d, e, j), (g, h, ' ')) ] if f == ' ' else
                 [] )

    def down (puzzle: State) -> List[State]:
        ((a, b, c), (d, e, f), (g, h, j)) = puzzle
        return ( [] if a == ' ' or b == ' ' or c == ' ' else
                 [ ((' ', b, c), (a, e, f), (g, h, j)) ] if d == ' ' else
                 [ ((a, ' ', c), (d, b, f), (g, h, j)) ] if e == ' ' else
                 [ ((a, b, ' '), (d, e, c), (g, h, j)) ] if f == ' ' else
                 [ ((a, b, c), (' ', e, f), (d, h, j)) ] if g == ' ' else
                 [ ((a, b, c), (d, ' ', f), (g, e, j)) ] if h == ' ' else
                 [ ((a, b, c), (d, e, ' '), (g, h, f)) ] if j == ' ' else
                 [] )

    return ( [ (u"◀", p, 1) for p in left(s) ] + 
             [ (u"▶", p, 1) for p in right(s) ] + 
             [ (u"▲", p, 1) for p in up(s) ] +
             [ (u"▼", p, 1) for p in down(s) ] )


def puzzle8_solver_DL (puzzle:  State,
                       d_max:   int) -> List[Solution]:
    """
    Instantiation of a general solver with the puzzle8 problem specific arguments, i.e., 'puzzle8_moves' for generating the successor states and 'puzzle8_solved' for recognising a solution.
    
    :param puzzle:  A puzzle 8 initial state.
    :param d_max:  The maximal depth that is allowed for a solution.
    :return:  The list of solutions, themselves lists of states along with explanation and cost of the used elementary operations
    """

    def is_solved (puzzle:  State) -> bool:
        return puzzle == (('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'H', ' '))

    return DL.solver(operations, is_solved, puzzle, 11)


def puzzle8_solver_BB (puzzle:  State,
                       b:       int,
                       d_max:   int) -> List[Solution]:
    """
    Instantiation of a general solver with the puzzle8 problem specific arguments, i.e., 'puzzle8_moves' for generating the successor states and 'puzzle8_solved' for recognising a solution.
    
    :param state:  A puzzle 8 initial state.
    :param b:  The maximal cost, plus one, that is allowed for a solution.
    :param d_max:  The maximal depth that is allowed for a solution.
    :return:  The list of solutions, themselves lists of states along with explanation and cost of the used elementary operations
    """

    def is_solved (puzzle:  State) -> bool:
        return puzzle == (('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'H', ' '))

    def hamming_heuristics (puzzle:  State) -> int:
        ((a, b, c), (d, e, f), (g, h, j)) = puzzle
        return len([ 1
                     for (c, l) in zip([a, b, c, d, e, f, g, h, h], "ABCDEFGH ")
                     if c != l ])

    return BB.solver(operations,  # type:  ignore
                     is_solved, hamming_heuristics, [], d_max, b, puzzle)


def puzzle8_solver_IDS (puzzle:  State,
                        d_max:   int) -> List[Solution]:
    """
    Instantiation of a general solver with the puzzle8 problem specific arguments, i.e., 'puzzle8_moves' for generating the successor states and 'puzzle8_solved' for recognising a solution.
    
    :param state:  A puzzle 8 initial state.
    :param d_max:  The maximal depth that is allowed for a solution.
    :return:  The list of solutions, themselves lists of states along with explanation and cost of the used elementary operations
    """

    def is_solved (puzzle:  State) -> bool:
        return puzzle == (('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'H', ' '))

    return IDS.solver(operations,  # type:  ignore
                      is_solved, d_max, puzzle)


def puzzle8_solver_IDA (puzzle:  State,
                        b:       int,
                        d_max:   int) -> List[Solution]:
    """
    Instantiation of a general solver with the puzzle8 problem specific arguments, i.e., 'puzzle8_moves' for generating the successor states and 'puzzle8_solved' for recognising a solution.
    
    :param state:  A puzzle 8 initial state.
    :param b:  The maximal cost, plus one, that is allowed for a solution.
    :param d_max:  The maximal depth that is allowed for a solution.
    :return:  The list of solutions, themselves lists of states along with explanation and cost of the used elementary operations
    """

    def is_solved (puzzle:  State) -> bool:
        return puzzle == (('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'H', ' '))

    def hamming_heuristics (puzzle:  State) -> int:
        ((a, b, c), (d, e, f), (g, h, j)) = puzzle
        return len([ 1
                     for (c, l) in zip([a, b, c, d, e, f, g, h, h], "ABCDEFGH ")
                     if c != l ])

    return IDA.solver(operations,  # type:  ignore
                      is_solved, hamming_heuristics, [], d_max, b, puzzle)


if __name__ == "__main__":
    print(">>> Depth-limit solver (with depth-limit set to 11)")
    for (i, s) in enumerate(puzzle8_solver_DL((('D', 'A', 'C'), (' ', 'H', 'E'), ('B', 'G', 'F')), 11), 1):
        print("Solution #", i, "for a cost of", sum([ c for (_, _, c) in s ]), ":", " ".join([ m for (m, _, _) in s ]))
        for (m, ((a, b, c), (d, e, f), (g, h, j)), _) in s:
            print("   ", m)
            print("      ", a, b, c)
            print("      ", d, e, f)
            print("      ", g, h, j)
    print()
    print("=====================================================================")
    print()
    print(">>> IDS solver (with maximal depth-limit set to 13;  limited to the first 5 solutions)")
    for (i, s) in enumerate(puzzle8_solver_IDS((('D', 'A', 'C'), (' ', 'H', 'E'), ('B', 'G', 'F')), 13), 1):
        if i > 5:  break
        print("Solution #", i, "for a cost of", sum([ c for (_, _, c) in s ]), ":", " ".join([ m for (m, _, _) in s ]))
        for (m, ((a, b, c), (d, e, f), (g, h, j)), _) in s:
            print("   ", m)
            print("      ", a, b, c)
            print("      ", d, e, f)
            print("      ", g, h, j)
    print()
    print("=====================================================================")
    print()
    print(">>> Branch-and-bound solver (with depth-limit and cost-bound set to 21, since they are equivalent here)")
    for (i, s) in enumerate(puzzle8_solver_BB((('D', 'A', 'C'), (' ', 'H', 'E'), ('B', 'G', 'F')), 21, 21), 1):
        print("Solution #", i, "for a cost of", sum([ c for (_, _, c) in s ]), ":", " ".join([ m for (m, _, _) in s ]))
        for (m, ((a, b, c), (d, e, f), (g, h, j)), _) in s:
            print("   ", m)
            print("      ", a, b, c)
            print("      ", d, e, f)
            print("      ", g, h, j)
    print()
    print("=====================================================================")
    print()
    print(">>> IDA* solver with Hamming heuristic (with maximal depth-limit and cost-bound set to 21, since they are equivalent here)")
    for (i, s) in enumerate(puzzle8_solver_IDA((('D', 'A', 'C'), (' ', 'H', 'E'), ('B', 'G', 'F')), 21, 21), 1):
        print("Solution #", i, "for a cost of", sum([ c for (_, _, c) in s ]), ":", " ".join([ m for (m, _, _) in s ]))
        for (m, ((a, b, c), (d, e, f), (g, h, j)), _) in s:
            print("   ", m)
            print("      ", a, b, c)
            print("      ", d, e, f)
            print("      ", g, h, j)

