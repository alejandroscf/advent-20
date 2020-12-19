#!/usr/bin/python3

import sys

# sys.argv[1]: horizontal movement (rigth > 0)
# sys.argv[2]: vertical movement (down > 0)

alive_set = set()
neig_set = set()

dirs = [
    (1, 1, 1),
    (1, 1, 0),
    (1, 1, -1),
    (1, 0, 1),
    (1, 0, 0),
    (1, 0, -1),
    (1, -1, 1),
    (1, -1, 0),
    (1, -1, -1),
    (0, 1, 1),
    (0, 1, 0),
    (0, 1, -1),
    (0, 0, 1),
    (0, 0, -1),
    (0, -1, 1),
    (0, -1, 0),
    (0, -1, -1),
    (-1, 1, 1),
    (-1, 1, 0),
    (-1, 1, -1),
    (-1, 0, 1),
    (-1, 0, 0),
    (-1, 0, -1),
    (-1, -1, 1),
    (-1, -1, 0),
    (-1, -1, -1)
] 

def turn_alive(coor):
    global alive_set
    global neig_set

    alive_set.add(coor)
    neig_set.discard(coor)
    for dire in dirs:
        neig = tuple(map(sum, zip(dire,coor)))
        if neig not in alive_set:
            neig_set.add(neig)

def turn_dead(coor):
    global alive_set
    global neig_set

    alive_set.discard(coor)

    for dire in dirs:
        neig = tuple(map(sum, zip(dire,coor)))
        if neig in alive_set:
            neig_set.add(coor)
            break


def check_neig(old_alive_set,coor):
    global neig_set
    neigs = [ tuple(map(sum, zip(dire,coor))) for dire in dirs]
    #print(neigs)
    #print(len(neigs))
    result = len(old_alive_set.intersection(neigs))
    #if result == 0:
    #    neig_set.discard(coor)
    return result

def print_set(cells):
    cell_dict = {}
    min_x = 0
    max_x = 0
    #min_y = 0
    #max_y = 0
    #print(min(cells))
    #print(max(cells))
    for cell in cells:
        if cell[2] not in cell_dict:
            cell_dict[cell[2]] = {}
        if cell[1] not in cell_dict[cell[2]]:
            cell_dict[cell[2]][cell[1]] = set()
        cell_dict[cell[2]][cell[1]].add(cell[0])

        if cell[0] > max_x:
            max_x = cell[0]
        if cell[0] < min_x:
            min_x = cell[0]
    keys=list(cell_dict.keys())
    keys.sort()
    for layer in keys:
        print("z=" + str(layer))
        y_keys=list(cell_dict[layer].keys())
        y_keys.sort()
        #print(y_keys)
        for y_key in y_keys:
            print(y_key, end=': ')
            for x_key in range(min_x,max_x+1):
                if x_key in cell_dict[layer][y_key]:
                    #print(check_neig(alive_set,(x_key,y_key,layer)), end='')
                    print('#', end='')
                else:
                    print('.', end='')
            print(cell_dict[layer][y_key], end='')
            #cell_dict[layer][y_key].sort()
            #for char in cell_dict[layer][y_key]:
            #    if char == min(cell_dict[layer][y_key]):
            #        print('#', end='')
            #    else:
            #        for i in range(last, char-1):
            #            print('.', end='')
            #        print('#', end='')
            #    last = char
            print()
        print()

x = 0
y = 0
z = 0

for line in sys.stdin:
    x = 0
    for pixel in line.strip():
        if pixel == '#':
            turn_alive((x, y, z))
        x += 1
    y += 1

print(alive_set)
print(len(alive_set))
#print_set(alive_set)

#print(check_neig(alive_set,(1,0,0)))

for cycle in range(6):
    print("cycle: " + str(cycle))
    old_alive_set = alive_set.copy()
    old_neig_set = neig_set.copy()
    for cell in old_alive_set:
        if not (2 <= check_neig(old_alive_set,cell) <= 3):
           turn_dead(cell) 
    for cell in old_neig_set:
        if check_neig(old_alive_set,cell) == 3:
           turn_alive(cell)  
    #print(alive_set)
    #print_set(alive_set)
    print(len(alive_set))
