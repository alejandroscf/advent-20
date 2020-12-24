#!/usr/bin/python3

import sys
import re
from functools import lru_cache


tile_num = 0
forest_tile = {}

#tile = {
#    content: 
#    borders:
#    rotate:
#    flip:
#    adjacent_n
#    adjacent_s
#    adjacent_e
#    adjacent_w


for line in sys.stdin:
    if line == '\n':
        pass
    elif line[0] == 'T':
        tile_num = re.match('^Tile (\d+):$', line.strip())
        tile_num = int(tile_num.group(1))
        forest_tile[tile_num] = {}
        forest_tile[tile_num]['content'] = []
    else:
        forest_tile[tile_num]['content'].append([ pixel for pixel in line.strip()])


@lru_cache(maxsize=len(forest_tile))
def extract_borders(tile):
    tile = forest_tile[tile]['content']
    result = set()
    f_row = tile[0][0:width]
    result.add(''.join(f_row))
    #result.add(''.join(reversed(f_row)))

    l_row = tile[height-1][0:width]
    result.add(''.join(l_row))
    #result.add(''.join(reversed(l_row)))
    
    f_col = [row[0] for row in tile]
    result.add(''.join(f_col))
    #result.add(''.join(reversed(f_col)))

    l_col = [row[-1] for row in tile]
    result.add(''.join(l_col))
    #result.add(''.join(reversed(l_col)))
    
    return result

#print(forest_tile)
width = len(forest_tile[tile_num]['content'][0])
height = len(forest_tile[tile_num]['content'])

print(len(forest_tile))

borders = {}

for tile in forest_tile:
    tile_borders = extract_borders(tile)
    forest_tile[tile]['borders'] = tile_borders
    for border in tile_borders:
        r_border = ''.join(reversed(border))
        if border not in borders and r_border not in borders:
            borders[border] = []
            borders[border].append(tile)
        elif border in borders:
            borders[border].append(tile)
        elif r_border in borders:
            borders[r_border].append(tile)

print(borders)

border_tiles = [ borders[line][0] for line in borders if len(borders[line]) == 1 ]
print(border_tiles)
result = 1
corners = set()
for tile in set(border_tiles):
    if border_tiles.count(tile) == 2:
        result *= tile
        corners.add(tile)

print("part one")
print(corners)
print(result)
print("part two")



for tile in forest_tile:
    print(tile)
    for border in forest_tile[tile]['borders']:
        r_border = ''.join(reversed(border))
        if border in borders:
            print(borders[border])
        if r_border in borders:
            print(borders[r_border])
            


