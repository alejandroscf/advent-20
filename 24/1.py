#!/usr/bin/python3

import sys
#import copy
import re

flip_tiles = set()

trad = {
    'e': (1,0), 
    'se': (1,-1), 
    'sw': (0,-1), 
    'w': (-1,0), 
    'nw': (-1,1), 
    'ne': (0,1)
}

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

    if tile in flip_tiles:
        flip_tiles.discard(tile)
    else:
        flip_tiles.add(tile)

print(len(flip_tiles))
