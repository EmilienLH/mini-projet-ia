import random
from typing import TypeVar, Callable, Tuple, List, Union


# MetaSolver_IteratedDeepening.py is in ../Recursive_Inferences_Engines folder
# Solver_DepthLimit.py is in ../Recursive_Inferences_Engines folder

from Recursive_Inference_Engines.MetaSolver_IteratedDeepening import meta_solver
import Recursive_Inference_Engines.Solver_DepthLimit as SDL

# create the cube :

cube = []
colors = ["yellow", "blue", "red", "green", "orange", "white"]
numbers = [i for i in range(1, 25)]

for numbers in numbers:
    color = colors[-1]
    if numbers % 4 == 0:
        color = colors.pop()
    cube.append((numbers, color))

# rotations : each rotation have a base function and a rotate function


def base_top(cube):
    top = cube[:4]
    left = cube[4:8]
    front = cube[8:12]
    right = cube[12:16]
    back = cube[16:20]

    rotated_top = [top[3], top[0], top[1], top[2]]
    rotated_left = [front[0], front[1], left[2], left[3]]
    rotated_front = [right[0], right[1], front[2], front[3]]
    rotated_right = [back[0], back[1], right[2], right[3]]
    rotated_back = [left[0], left[1], back[2], back[3]]
    rotated_bottom = cube[20:]
    new_cube = rotated_top + rotated_left + rotated_front + \
        rotated_right + rotated_back + rotated_bottom
    return new_cube


def rotate_top(cube, angle):
    if angle == 90:
        return base_top(cube)
    elif angle == -90:
        return base_top(base_top(base_top(cube)))
    elif angle == 180:
        return base_top(base_top(cube))


def base_left(cube):
    top = cube[:4]
    left = cube[4:8]
    front = cube[8:12]
    right = cube[12:16]
    back = cube[16:20]
    bottom = cube[20:]

    rotated_top = [back[2], top[1], top[2], back[1]]
    rotated_left = [left[3], left[0], left[1], left[2]]
    rotated_front = [top[0], front[1], front[2], top[3]]
    rotated_right = right
    rotated_back = [back[0], bottom[3], bottom[0], back[3]]
    rotated_bottom = [front[0], bottom[1], bottom[2], front[3]]

    new_cube = rotated_top + rotated_left + rotated_front + \
        rotated_right + rotated_back + rotated_bottom
    return new_cube


def rotate_left(cube, angle):
    if angle == 90:
        return base_left(cube)
    elif angle == -90:
        return base_left(base_left(base_left(cube)))
    elif angle == 180:
        return base_left(base_left(cube))


def base_front(cube):
    top = cube[:4]
    left = cube[4:8]
    front = cube[8:12]
    right = cube[12:16]
    back = cube[16:20]
    bottom = cube[20:]

    rotated_top = [top[0], top[1], left[1], left[2]]
    rotated_left = [left[0], bottom[0], bottom[1], left[3]]
    rotated_front = [front[3], front[0], front[1], front[2]]
    rotated_right = [top[3], right[1], right[2], top[2]]
    rotated_back = back
    rotated_bottom = [right[3], right[0], bottom[2], bottom[3]]

    new_cube = rotated_top + rotated_left + rotated_front + \
        rotated_right + rotated_back + rotated_bottom
    return new_cube


def rotate_front(cube, angle):
    if angle == 90:
        return base_front(cube)
    elif angle == -90:
        return base_front(base_front(base_front(cube)))
    elif angle == 180:
        return base_front(base_front(cube))


def base_right(cube):
    top = cube[:4]
    left = cube[4:8]
    front = cube[8:12]
    right = cube[12:16]
    back = cube[16:20]
    bottom = cube[20:]

    rotated_top = [top[0], front[1], front[2], top[3]]
    rotated_left = left
    rotated_front = [front[0], bottom[1], bottom[2], front[3]]
    rotated_right = [right[3], right[0], right[1], right[2]]
    rotated_back = [top[2], back[1], back[2], top[1]]
    rotated_bottom = [bottom[0], back[3], back[0], bottom[3]]

    new_cube = rotated_top + rotated_left + rotated_front + \
        rotated_right + rotated_back + rotated_bottom
    return new_cube


def rotate_right(cube, angle):
    if angle == 90:
        return base_right(cube)
    elif angle == -90:
        return base_right(base_right(base_right(cube)))
    elif angle == 180:
        return base_right(base_right(cube))


def base_back(cube):
    top = cube[:4]
    left = cube[4:8]
    front = cube[8:12]
    right = cube[12:16]
    back = cube[16:20]
    bottom = cube[20:]

    rotated_top = [right[1], right[2], top[2], top[3]]
    rotated_left = [top[1], left[1], left[2], top[0]]
    rotated_front = front
    rotated_right = [right[0], bottom[2], bottom[3], right[3]]
    rotated_back = [back[3], back[0], back[1], back[2]]
    rotated_bottom = [bottom[0], bottom[1], left[3], left[0]]

    new_cube = rotated_top + rotated_left + rotated_front + \
        rotated_right + rotated_back + rotated_bottom
    return new_cube


def rotate_back(cube, angle):
    if angle == 90:
        return base_back(cube)
    elif angle == -90:
        return base_back(base_back(base_back(cube)))
    elif angle == 180:
        return base_back(base_back(cube))


def base_bottom(cube):
    top = cube[:4]
    left = cube[4:8]
    front = cube[8:12]
    right = cube[12:16]
    back = cube[16:20]
    bottom = cube[20:]

    rotated_top = top
    rotated_left = [left[0], left[1], back[2], back[3]]
    rotated_front = [front[0], front[1], left[2], left[3]]
    rotated_right = [right[0], right[1], front[2], front[3]]
    rotated_back = [back[0], back[1], right[2], right[3]]
    rotated_bottom = [bottom[3], bottom[0], bottom[1], bottom[2]]

    new_cube = rotated_top + rotated_left + rotated_front + \
        rotated_right + rotated_back + rotated_bottom
    return new_cube


def rotate_bottom(cube, angle):
    if angle == 90:
        return base_bottom(cube)
    elif angle == -90:
        return base_bottom(base_bottom(base_bottom(cube)))
    elif angle == 180:
        return base_bottom(base_bottom(cube))

# random rotations :


def random_rotation(cube, n=16):
    rotations = [rotate_top, rotate_left, rotate_front,
                 rotate_right, rotate_back, rotate_bottom]
    angles = [90, -90, 180]
    for i in range(n):
        rotation = random.choice(rotations)
        print(rotation)
        angle = random.choice(angles)
        print(angle)
        cube = rotation(cube, angle)
    return cube


# solver :

State = TypeVar('State')
Description = TypeVar('Description')
Cost = TypeVar('Cost')
Transition = Tuple[Description, State, Cost]
Solution = List[Transition]


def all_same(items):
    return all(x == items[0] for x in items)


def etape(state):
    # etape 1 : une face is de la même couleur
    faces = [state[i:i+4] for i in range(0, len(state), 4)]
    return any(all_same([color for (number, color) in face]) for face in faces)


def etape2(state):
    # etape 2 : deux faces opposées sont de la même couleur (ex : top and bottom)
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

    solved_face = any(all_same([color for (number, color) in face]) for face in [
                        top, left, front, right, back, bottom])
    solved_color = [color for (number, color) in solved_face]

    # check which face is the solved one : 
    if solved_face == top :
        print("Solved : top, opposite : bottom")
        opposite_face = bottom
    elif solved_face == left :
        print("Solved : left, opposite : right")
        opposite_face = right
    elif solved_face == front :
        print("Solved : front, opposite : back")
        opposite_face = back
    elif solved_face == right :
        print("Solved : right, opposite : left")
        opposite_face = left
    elif solved_face == back :
        print("Solved : back, opposite : front")
        opposite_face = front
    elif solved_face == bottom :
        print("Solved : bottom, opposite : top")
        opposite_face = top

    opposite_color  = [color for (number, color) in opposite_face]
    # etape2 is when both the solved face and opposite face are solved. Each face is one color, the color of the already solved face should not change
    # the goal is only to go from one solved face to two opposite solved faces. they cannot be the same color as it's impossible to have two faces of the same color on a cube
    if (len(set(solved_color)) == 1 and len(set(opposite_color)) == 1 and solved_color != opposite_color):
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
    all_moves = [("top", rotate_top(state, 90), 1), ("top*", rotate_top(state, -90), 1),
                 ("left", rotate_left(state, 90),
                  1), ("left*", rotate_left(state, -90), 1),
                 ("front", rotate_front(state, 90),
                  1), ("front*", rotate_front(state, -90), 1),
                 ("right", rotate_right(state, 90),
                  1), ("right*", rotate_right(state, -90), 1),
                 ("back", rotate_back(state, 90),
                  1), ("back*", rotate_back(state, -90), 1),
                 ("bottom", rotate_bottom(state, 90), 1), ("bottom*", rotate_bottom(state, -90), 1)]
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
    result_etape = solverIDS(transformations, etape2, 8, cube)

    print("ok etape 1")

    if result_etape is not None:
        cube_after_etape = result_etape[1]
        print(cube_after_etape)
        print("ok etape 1_2")

        result_final = solverIDS(transformations, isFinal, 8, cube_after_etape)
        print("ok etape 2")

        if result_final is not None:
            return result_final
        else:
            return None
    else:
        return None


def solverStep(cube):
    print("Etape 1 : ")
    result_etape = solverIDS(transformations, etape, 8, cube)

    if result_etape is not None:
        cube_after_etape = result_etape[1]
        print(cube_after_etape)
        print("Etape 2 : ")
        result_etape2 = solverIDS(
            transformations, isFinal, 7, cube_after_etape)
        if result_etape2 is not None:
            print("Final : ")
            cube_after_final = result_etape2[1]
            resultat_final = solverIDS(
                transformations, isFinal, 4, cube_after_final)
            if resultat_final is not None:
                return resultat_final
            else:
                return None
        else:
            return None
    else:
        return None


def solve(cube):
    return solverDL(transformations, isFinal, cube, 7)


def solveIDS(cube):
    return solverIDS(transformations, isFinal, 8, cube)


def solveStep(cube):
    return solverStep(cube)


print(cube)

random_cube = random_rotation(cube)

print(random_cube)


# print(solve(random_cube))

# print(solve3(random_cube))

print(solveStep(random_cube))
