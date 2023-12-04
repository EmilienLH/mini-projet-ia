from typing import TypeVar, Callable, Tuple, List, Union
from rotation import *
from algo import *

# solver :

State = TypeVar('State')
Description = TypeVar('Description')
Cost = TypeVar('Cost')
Transition = Tuple[Description, State, Cost]
Solution = List[Transition]


def etape(state):
    # etape 1 : solve the bottom face

    bottom = state[20:]
    bottom_colors = [color for (number, color) in bottom]

    if len(set(bottom_colors)) == 1:
        return True
    else:
        return False


def etape2(state):
    # solve two faces, opposite from each other, since we solved the bottom, we now want to solve the top
    top = state[:4]
    bottom = state[20:]

    top_colors = [color for (number, color) in top]
    bottom_colors = [color for (number, color) in bottom]

    if (len(set(top_colors)) == 1 and len(set(bottom_colors)) == 1):
        return True
    else:
        return False


def isFinal(state):
    # a state is final if all the colors on a face are the same
    top = state[:4]
    left = state[4:8]
    front = state[8:12]
    right = state[12:16]
    back = state[16:20]
    bottom = state[20:]

    top_colors = [color for (number, color) in top]
    left_colors = [color for (number, color) in left]
    front_colors = [color for (number, color) in front]
    right_colors = [color for (number, color) in right]
    back_colors = [color for (number, color) in back]
    bottom_colors = [color for (number, color) in bottom]

    # if a set of colors has a length of 1, it means that all the colors are the same, allows us to check if a face is solved without checking numbers
    if len(set(top_colors)) == 1 and len(set(left_colors)) == 1 and len(set(front_colors)) == 1 and len(set(right_colors)) == 1 and len(set(back_colors)) == 1 and len(set(bottom_colors)) == 1:
        return True
    else:
        return False

# all the possible moves, with their description, the state after the move, and the cost of the move, needed for DL and IDS
def transformations(state, path=None):
    # all the possible rotations
    all_moves = [("top", rotate_top(state, 90), 1), ("top*", rotate_top(state, -90), 1), ("top**", rotate_top(state, 180), 1),
                 ("left", rotate_left(state, 90), 1), ("left*",
                                                       rotate_left(state, -90), 1), ("left**", rotate_left(state, 180), 1),
                 ("front", rotate_front(state, 90), 1), ("front*",
                                                         rotate_front(state, -90), 1), ("front**", rotate_front(state, 180), 1),
                 ("right", rotate_right(state, 90), 1), ("right*",
                                                         rotate_right(state, -90), 1), ("right**", rotate_right(state, 180), 1),
                 ("back", rotate_back(state, 90), 1), ("back*",
                                                       rotate_back(state, -90), 1), ("back**", rotate_back(state, 180), 1),
                 ("bottom", rotate_bottom(state, 90), 1), ("bottom*", rotate_bottom(state, -90), 1), ("bottom**", rotate_bottom(state, 180), 1)]

    # get the last move from the path
    last_move = None
    if path is not None and len(path) > 0:
        last_move = path[-1][0]

    # if there is no last move, all the moves are possible
    if last_move is None:
        return all_moves

    # get last move's direction and number of stars
    last_dir = last_move.split("*")[0]
    last_stars = len(last_move.split("*")) - 1

    # filter the possible moves to remove the useless ones
    possible_moves = []
    for move in all_moves:
        dir = move[0].split("*")[0]
        stars = len(move[0].split("*")) - 1

        # Check if the move ends up to a 0 degree rotation : 90 + -90 = 0, 180 + 180 = 0 (in a 360° circle)
        # 0 + 1 = 1, 1 + 0 = 1, 2 + 2 = 1
        if dir == last_dir and (last_stars + stars) % 3 == 1:
            continue

        # Check if the move is the same as the last move : useless, might as well do move** instead
        if dir == last_dir and stars == last_stars:
            continue
        # If the move is not useless, add it to the list of possible moves
        possible_moves.append(move)

    return possible_moves

# all the possibles algorithms to go from solved bottom to both solved bottom and top, defined in algo.py
def transformationsAlgo(state, path=None):
    # Following the Ortega method, once the bottom is solved, 7 algorithms can be used to solve the top face
    return [("algo1", algo1(state), 1), ("algo2", algo2(state), 1), ("algo3", algo3(state), 1),
            ("algo4", algo4(state), 1), ("algo5", algo5(
                state), 1), ("algo6", algo6(state), 1),
            ("algo7", algo7(state), 1)]

# all the possible algorithms to go from solved bottom and top to solved cube, defined in algo.py
def transformationsAlgoFin(state, path=None):
    # Still following the Ortega method, once both the bottom and the top are solved, 6 algorithms can be used to solve the cube
    return [("algo_fin1", algo_fin1(state), 1), ("algo_fin2", algo_fin2(state), 1), ("algo_fin3", algo_fin3(state), 1),
            ("algo_fin4", algo_fin4(state), 1), ("algo_fin5", algo_fin5(state), 1), ("algo_fin6", algo_fin6(state), 1)]

# basic DL search
def solverDL(transformations, isFinal, state, d_max, path=None):
    if path is None:
        path = []

    if d_max < 0:
        return None

    if isFinal(state):
        return [path, state]

    for (description, next_state, cost) in transformations(state, path):
        next_path = path + [(description,)]
        result = solverDL(transformations, isFinal,
                         next_state, d_max - 1, next_path)

        if result is not None:
            return result

    return None

# IDS search
def solverIDS(transformations:  Callable[[State], List[Transition]],
              etape:          Callable[[State], bool],
              d_max:            int,
              initial:          State) -> List[Solution]:
    for depth in range(1, d_max + 1):
        print("depth : ", depth)
        result = solverDL(transformations, etape, initial, depth)
        if result is not None:
            return result

# Using IDS, algorithms and 3 steps to solve the cube, it's a bit slower but it works everytime, unlike the IDS or DL that sometimes get stuck / search for too long
def solveWithStep(cube):
    print("Starting etape 1 ...")
    # IDS to solve the bottom face
    result_etape = solverIDS(transformations, etape, 8, cube)
    
    # Once the bottom is solved, we can use the algorithms to solve the top
    if result_etape is not None:
        # Get the path and the cube after the first step
        path_after_etape = result_etape[0]
        cube_after_etape = result_etape[1]

        print("Etape 1 : OK\n")
        print("Starting etape 2 ...")

        # IDS to solve the top face, using the algorithms
        result_etape2 = solverIDS(
            transformationsAlgo, etape2, 8, cube_after_etape)
        
        # Once the top is solved, we can use the algorithms to solve the cube
        if result_etape2 is not None:
            # Get the path and the cube after the second step
            path_after_etape2 = path_after_etape + result_etape2[0] # concatenate the two paths
            cube_after_etape2 = result_etape2[1]

            print("Etape 2 : OK\n")
            print("Starting final step ...")

            # IDS to solve the cube, using the algo_fin algorithms
            result_final = solverIDS(
                transformationsAlgoFin, isFinal, 8, cube_after_etape2)
            
            # If the cube is solved, return the path and the solved cube
            if result_final is not None:
                result_final[0][0:0] = path_after_etape2
                print("Rubik's cube solved !\n")
                return result_final
            else:
                return None
        else:
            return None
    else:
        return None
