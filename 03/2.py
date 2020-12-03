#!/usr/bin/python3

import sys
import math

# sys.argv[1]: horizontal movement (rigth > 0)
# sys.argv[2]: vertical movement (down > 0)

slopes = []
slopes.append((1,1))
slopes.append((3,1))
slopes.append((5,1))
slopes.append((7,1))
slopes.append((1,2))

forest_tile = []
for line in sys.stdin:
    forest_tile.append([ pixel for pixel in line if pixel != '\n'])

#print(forest_tile)
width=len(forest_tile[0])
length=len(forest_tile)

x=0
y=0

print("width: " + str(width))
print("length: " + str(length))
print()

def is_tree(x, y):
    #print(forest_tile[y][x%width])
    if forest_tile[y][x%width] == '#':
        return True
    else:
        return False

result = 1

for slope in slopes:
    trees = 0
    for row in range(math.ceil(length/slope[1])):
        #print(is_tree(x,y))
        if is_tree(x,y):
            trees = trees + 1
        x=x+slope[0]
        y=y+slope[1]
    x=0
    y=0
    result=result*trees
    print("Trees: " + str(trees))
print("result: " + str(result))
