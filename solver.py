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

    if len(set(top_colors)) == 1 and len(set(left_colors)) == 1 and len(set(front_colors)) == 1 and len(set(right_colors)) == 1 and len(set(back_colors)) == 1 and len(set(bottom_colors)) == 1:
        return True
    else:
        return False


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

    last_move = None
    if path is not None and len(path) > 0:
        last_move = path[-1][0]

    if last_move is None:
        return all_moves

    last_dir = last_move.split("*")[0]
    last_stars = len(last_move.split("*")) - 1

    possible_moves = []
    for move in all_moves:
        dir = move[0].split("*")[0]
        stars = len(move[0].split("*")) - 1

        # Check if the move is the inverse of the last move
        # 0 + 1 = 1, 1 + 0 = 1, 2 + 2 = 1
        if dir == last_dir and (last_stars + stars) % 3 == 1:
            continue

        # Check if the move is the same as the last move : useless, might as well do move** instead
        if dir == last_dir and stars == last_stars:
            continue
        # If the move is not useless, add it to the list of possible moves
        possible_moves.append(move)

    return possible_moves


def transformationsAlgo(state, path=None):
    # Following the Ortega method, once the bottom is solved, 7 algorithms can be used to solve the top face
    return [("algo1", algo1(state), 1), ("algo2", algo2(state), 1), ("algo3", algo3(state), 1),
            ("algo4", algo4(state), 1), ("algo5", algo5(
                state), 1), ("algo6", algo6(state), 1),
            ("algo7", algo7(state), 1)]


def transformationsAlgoFin(state, path=None):
    # Still following the Ortega method, once both the bottom and the top are solved, 6 algorithms can be used to solve the cube
    return [("LT*RT**R*FRT**R*L*", algo_fin1(state), 1), ("R**D*RT*R*TF**TRTR*", algo_fin2(state), 1), ("RT*LT**R*TL*", algo_fin3(state), 1),
            ("R**F**R**", algo_fin4(state), 1), ("R**T*R**T*D*R**T*R**", algo_fin5(state), 1), ("LD*RT**R*DL*", algo_fin6(state), 1)]


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


def solverIDS(transformations:  Callable[[State], List[Transition]],
              etape:          Callable[[State], bool],
              d_max:            int,
              initial:          State) -> List[Solution]:
    for depth in range(1, d_max + 1):
        print("depth : ", depth)
        result = solverDL(transformations, etape, initial, depth)
        if result is not None:
            return result


def solveWithStep(cube):
    print("Etape 1 :")
    result_etape = solverIDS(transformations, etape, 8, cube)
    if result_etape is not None:

        path_after_etape = result_etape[0]
        cube_after_etape = result_etape[1]

        print(cube_after_etape)
        print(result_etape[0])
        print("Etape 1 : OK")

        print("Etape 2 :")
        result_etape2 = solverIDS(
            transformationsAlgo, etape2, 8, cube_after_etape)
        if result_etape2 is not None:

            path_after_etape2 = path_after_etape + result_etape2[0]
            cube_after_etape2 = result_etape2[1]
            print(cube_after_etape2)
            print(path_after_etape2)
            print("Etape 2 : OK")

            print("Etape finale :")
            result_final = solverIDS(
                transformationsAlgoFin, isFinal, 8, cube_after_etape2)
            if result_final is not None:
                result_final[0][0:0] = path_after_etape2
                return result_final
            else:
                return None
        else:
            return None
    else:
        return None
