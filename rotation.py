# rotations : each rotation have a base function and a rotate function 
# the rotate is just a wrapper for the base function, it allows us to rotate a face with the angle we want (90, -90, 180)

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