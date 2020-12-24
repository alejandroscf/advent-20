#!/usr/bin/python3

import sys
#import copy
import re

#alive_set = set()
alive_set = set()
neig_set = set()


trad = {
    'e': (1,0), 
    'se': (1,-1), 
    'sw': (0,-1), 
    'w': (-1,0), 
    'nw': (-1,1), 
    'ne': (0,1)
}

dirs = trad.values()

def check_neig(old_alive_set,coor):
    global neig_set
    neigs = [ tuple(map(sum, zip(dire,coor))) for dire in dirs]
    #print(neigs)
    #print(len(neigs))
    result = len(old_alive_set.intersection(neigs))
    #if result == 0:
    #    neig_set.discard(coor)
    return result

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


def aggregate(ins):
    result = (0,0)
    for dire in ins:
        dire = trad[dire]
        result = tuple(map(sum, zip(dire,result)))
    return result

for line in sys.stdin:
    ins = re.findall('(se|sw|nw|ne|e|w)',line.strip())
    #print(ins)
    tile = aggregate(ins)
    #print(tile)

    if tile in alive_set:
        turn_dead(tile)
        #alive_set.discard(tile)
    else:
        turn_alive(tile)
        #alive_set.add(tile)

print('part one')
print(len(alive_set))

print('part two')
for cycle in range(1,100+1):
    print("cycle: " + str(cycle))
    old_alive_set = alive_set.copy()
    old_neig_set = neig_set.copy()
    # Black
    for cell in old_alive_set:
        adj = check_neig(old_alive_set,cell)
        if adj == 0 or adj > 2:
           turn_dead(cell) 
    # White
    for cell in old_neig_set:
        if check_neig(old_alive_set,cell) == 2:
           turn_alive(cell)  
    #print(alive_set)
    #print_set(alive_set)
    print(len(alive_set))

