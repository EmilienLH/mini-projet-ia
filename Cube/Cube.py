# Create the code to implement a cube mathematically : each tile has one unique number et a colour : 
# {1,2...24} and {red, blue, green, yellow, orange, white}
# the cube is represented by a a list of 24 tiles
# each tile is represented by a tuple (number, colour)

cube = []
numbers = range(1, 25)
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'white']
for number in numbers:
    for color in colors:
        cube.append((number, color))

# next : shuffle the cube

import random
random.shuffle(cube)

