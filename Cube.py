import random
from rotation import *
from solver import *

# create the cube :

cube = []
colors = ["yellow", "blue", "red", "green", "orange", "white"]
numbers = [i for i in range(1, 25)]
for numbers in numbers:
    color = colors[-1]
    if numbers % 4 == 0:
        color = colors.pop()
    cube.append((numbers, color))

# list of moves in each algorithm (for printing purposes) :

algo1 = ["right*", "top*", "right", "top*", "right*", "top**", "right"]
algo2 = ["right*", "top**", "right", "top", "right*", "top", "right"]
algo3 = ["front*", "right", "top", "right*", "top*", "right*", "front", "right"]
algo4 = ["right*", "front*", "right", "top", "right", "top", "right*", "front"]
algo5 = ["front", "right", "top", "right*", "top*", "front*"]
algo6 = ["right*", "top", "right**", "top*", "right**", "top*", "right**", "top", "right*"]
algo7 = ["right**", "top**", "right", "top**", "right**"]

algo_fin1 = ["left", "top*", "right", "top**", "right*", "front", "right", "top**", "right*", "left*"]
algo_fin2 = ["right**", "bottom*", "right", "top*", "right*", "top", "front*", "top", "right", "top*", "right"]
algo_fin3 = ["right", "top*", "left", "top**", "right*", "top", "left*"]
algo_fin4 = ["right**", "front**", "right**"]
algo_fin5 = ["right**", "top*", "right**", "top*", "bottom*", "right**", "top*", "right**"]
algo_fin6 = ["left*", "bottom*", "right", "top**", "right*", "bottom", "left"]

algos = {
    "algo1" : algo1,
    "algo2" : algo2,
    "algo3" : algo3,
    "algo4" : algo4,
    "algo5" : algo5,
    "algo6" : algo6,
    "algo7" : algo7,
    "algo_fin1" : algo_fin1,
    "algo_fin2" : algo_fin2,
    "algo_fin3" : algo_fin3,
    "algo_fin4" : algo_fin4,
    "algo_fin5" : algo_fin5,
    "algo_fin6" : algo_fin6
}

# random rotations :

def random_rotation(cube, n=48):
    rotations = [rotate_top, rotate_left, rotate_front,
                 rotate_right, rotate_back, rotate_bottom]
    angles = [90, -90, 180]
    for i in range(n):
        rotation = random.choice(rotations) # choose a random rotation
        print(rotation)
        angle = random.choice(angles) # with a random angle
        print(angle)
        cube = rotation(cube, angle)
    return cube

def print_solution(path, algos):
    num_moves = 0
    for move in path:
        algo = algos.get(move[0])
        if algo is not None:
            print(f"{move[0]} : ")
            for sub_move in algo:
                print("\t", sub_move)
                num_moves += 1
        else:
            print(move[0])
            num_moves += 1
    print("Number of moves : ", num_moves)

def solveDL(cube): # basic depth limited search
    return solverDL(transformations, isFinal, cube, 7)

def solveIDS(cube): # iterative deepening search, depth limited search with increasing depth
    return solverIDS(transformations, isFinal, 8, cube)

def solveStep(cube): # added step by step solving and algorithms to the solver
    return solveWithStep(cube)

random_cube = random_rotation(cube, n = 48)

# print(solveDL(random_cube))

# print(solveIDS(random_cube))

print_solution(solveStep(random_cube)[0], algos)
