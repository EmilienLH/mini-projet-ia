import random
from typing import TypeVar, Callable, Tuple, List


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

def random_rotation(cube, n =6) :
    rotations = [rotate_top, rotate_left, rotate_front, rotate_right, rotate_back, rotate_bottom]
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
                    ("left", rotate_left(state, 90), 1), ("left*", rotate_left(state, -90), 1), ("left**", rotate_left(state, 180), 1),
                    ("front", rotate_front(state, 90), 1), ("front*", rotate_front(state, -90), 1), ("front**", rotate_front(state, 180), 1),
                    ("right", rotate_right(state, 90), 1), ("right*", rotate_right(state, -90), 1), ("right**", rotate_right(state, 180), 1),
                    ("back", rotate_back(state, 90), 1), ("back*", rotate_back(state, -90), 1), ("back**", rotate_back(state, 180), 1),
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
        # If the move is not useless, add it to the list of possible moves
        possible_moves.append(move)

    return possible_moves


def solver2(transformations, isFinal, state, d_max, path=None):
    if path is None:
        path = []  

    if d_max < 0:
        return None  

    if isFinal(state):
        return path  

    for (description, next_state, cost) in transformations(state, path):
        next_path = path + [(description,)]  
        result = solver2(transformations, isFinal, next_state, d_max - 1, next_path)

        if result is not None:
            return result  

    return None  


def solve(cube):
    return solver2(transformations, isFinal, 10, cube)


def print_solution(solution):
    print("solution :")
    # Imprime la solution
    for i in range(len(solution)):
        print("step", i, ":", solution[i][0], solution[i][2])
        print(solution[i][1])
        print()

print(cube)

random_cube = random_rotation(cube)

print(random_cube)


print(solve(random_cube))

