#!/usr/bin/python3

import sys
import re
from functools import lru_cache


tile_num = 0
forest_tile = {}

for line in sys.stdin:
    if line == '\n':
        pass
    elif line[0] == 'T':
        tile_num = re.match('^Tile (\d+):$', line.strip())
        tile_num = int(tile_num.group(1))
        forest_tile[tile_num] = []
    else:
        forest_tile[tile_num].append([ pixel for pixel in line.strip()])


@lru_cache(maxsize=len(forest_tile))
def extract_borders(tile):
    tile = forest_tile[tile]
    result = set()
    f_row = tile[0][0:width]
    result.add(''.join(f_row))
    result.add(''.join(reversed(f_row)))

    l_row = tile[height-1][0:width]
    result.add(''.join(l_row))
    result.add(''.join(reversed(l_row)))
    
    f_col = [row[0] for row in tile]
    result.add(''.join(f_col))
    result.add(''.join(reversed(f_col)))

    l_col = [row[-1] for row in tile]
    result.add(''.join(l_col))
    result.add(''.join(reversed(l_col)))
    
    return result

#print(forest_tile)
width = len(forest_tile[tile_num][0])
height = len(forest_tile[tile_num])

print(len(forest_tile))

borders = {}

for tile in forest_tile:
    for border in extract_borders(tile):
        if border not in borders:
            borders[border] = []
        borders[border].append(tile)

print(borders)

border_tiles = [ borders[line][0] for line in borders if len(borders[line]) == 1 ]
print(border_tiles)
result = 1
for tile in set(border_tiles):
    if border_tiles.count(tile) == 4:
        print(tile)
        result *= tile

print(result)
