import random

# Create the code to implement a cube mathematically : each tile has one unique number et a colour : 
# {1,2...24} and {red, blue, green, yellow, orange, white}
# the cube is represented by a a list of 24 tiles
# each tile is represented by a tuple (number, colour)

# first : create the cube

cube = []
colors = ["red", "blue", "green", "yellow", "orange", "white"]
numbers = [i for i in range(1, 25)]

for numbers in numbers :
    color = colors[-1]
    if numbers % 4 == 0 :
        color = colors.pop()
    cube.append((numbers, color))

# rotations : 

def base_top(cube) :
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
    new_cube = rotated_top + rotated_left + rotated_front + rotated_right + rotated_back + rotated_bottom
    return new_cube

def rotate_top(cube, angle) :
    if angle == 90 :
        return base_top(cube)
    elif angle == -90 :
        return base_top(base_top(base_top(cube)))
    elif angle == 180 :
        return base_top(base_top(cube))
    
def base_left(cube) :
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
    rotated_back = [back[0],bottom[3], bottom[0], back[3]]
    rotated_bottom = [front[0], bottom[1], bottom[2], front[3]]

    new_cube = rotated_top + rotated_left + rotated_front + rotated_right + rotated_back + rotated_bottom
    return new_cube

def rotate_left(cube, angle) :
    if angle == 90 :
        return base_left(cube)
    elif angle == -90 :
        return base_left(base_left(base_left(cube)))
    elif angle == 180 :
        return base_left(base_left(cube))
    

