#!/usr/bin/python3

import sys

# sys.argv[1]: horizontal movement (rigth > 0)
# sys.argv[2]: vertical movement (down > 0)

forest_tile = []
for line in sys.stdin:
    forest_tile.append([ pixel for pixel in line if pixel != '\n'])

print(forest_tile)
width=len(forest_tile[0])
length=len(forest_tile)

x=0
y=0

print("width: " + str(width))
print("length: " + str(length))
print()

def is_tree(x, y):
    print(forest_tile[y][x%width])
    if forest_tile[y][x%width] == '#':
        return True
    else:
        return False

trees = 0

for row in range(length):
    print(is_tree(x,y))
    if is_tree(x,y):
        trees = trees + 1
    x=x+int(sys.argv[1])
    y=y+int(sys.argv[2])
print("Trees: " + str(trees))
