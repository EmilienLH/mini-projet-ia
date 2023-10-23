import random

# create the cube : 

cube = []
colors = ["red", "blue", "green", "yellow", "orange", "white"]
numbers = [i for i in range(1, 25)]

for numbers in numbers :
    color = colors[-1]
    if numbers % 4 == 0 :
        color = colors.pop()
    cube.append((numbers, color))

# rotations : each rotation have a base function and a rotate function

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

def base_front(cube) :
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

    new_cube = rotated_top + rotated_left + rotated_front + rotated_right + rotated_back + rotated_bottom
    return new_cube

def rotate_front(cube, angle) :
    if angle == 90 :
        return base_front(cube)
    elif angle == -90 :
        return base_front(base_front(base_front(cube)))
    elif angle == 180 :
        return base_front(base_front(cube))
    
def base_right(cube) :
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
    
    new_cube = rotated_top + rotated_left + rotated_front + rotated_right + rotated_back + rotated_bottom
    return new_cube

def rotate_right(cube, angle) :
    if angle == 90 :
        return base_right(cube)
    elif angle == -90 :
        return base_right(base_right(base_right(cube)))
    elif angle == 180 :
        return base_right(base_right(cube))
    

def base_back(cube) :
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
    rotated_bottom = [bottom[0],bottom[1], left[3], left[0]]

    new_cube = rotated_top + rotated_left + rotated_front + rotated_right + rotated_back + rotated_bottom
    return new_cube

def rotate_back(cube, angle) :
    if angle == 90 :
        return base_back(cube)
    elif angle == -90 :
        return base_back(base_back(base_back(cube)))
    elif angle == 180 :
        return base_back(base_back(cube))

def base_bottom(cube) :
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

    new_cube = rotated_top + rotated_left + rotated_front + rotated_right + rotated_back + rotated_bottom
    return new_cube

def rotate_bottom(cube, angle) :
    if angle == 90 :
        return base_bottom(cube)
    elif angle == -90 :
        return base_bottom(base_bottom(base_bottom(cube)))
    elif angle == 180 :
        return base_bottom(base_bottom(cube))

# random rotations :

def random_rotation(cube, n = 10) :
    rotations = [rotate_top, rotate_left, rotate_front, rotate_right, rotate_back, rotate_bottom]
    angles = [90, -90, 180]
    for i in range(n) :
        rotation = random.choice(rotations)
        angle = random.choice(angles)
        cube = rotation(cube, angle)
    return cube

print(random_rotation(cube, 10))

# solve the cube :

def solve(cube) :
    top = cube[:4]
    left = cube[4:8]
    front = cube[8:12]
    right = cube[12:16]
    back = cube[16:20]
    bottom = cube[20:]

    if top[0][1] == top[1][1] == top[2][1] == top[3][1] and left[0][1] == left[1][1] == left[2][1] == left[3][1] and front[0][1] == front[1][1] == front[2][1] == front[3][1] and right[0][1] == right[1][1] == right[2][1] == right[3][1] and back[0][1] == back[1][1] == back[2][1] == back[3][1] and bottom[0][1] == bottom[1][1] == bottom[2][1] == bottom[3][1] :
        return True
    else :
        cube = random_rotation(cube)
        return solve(cube)
    
print(solve(random_rotation(cube)))
    
