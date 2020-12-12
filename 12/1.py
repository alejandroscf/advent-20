#!/usr/bin/python3

import sys
#import copy
#import re


#
#  y > 0
#
#  ^
#  |  ^
#  | |_| compass = 0
#  |
#  |_______> x > 0
#  
#

boat = {
    'x' : 0,
    'y' : 0,
    'compass' : 270
}

def forward(compass):
    if compass == 0:
        return (0, 1, 0)
    elif compass == 90:
        return (-1, 0, 0)
    elif compass == 180:
        return (0, -1, 0)
    elif compass == 270:
        return (1, 0, 0)


def update_boat(boat, nav_ins):
    directions = {
        'N': (0, 1, 0),
        'S': (0, -1, 0),
        'E': (1, 0, 0),
        'W': (-1, 0, 0),
        'L': (0, 0, 1),
        'R': (0, 0, -1),
        'F': forward(boat['compass'])
    } 

    #print(nav_ins)
    ins = nav_ins[0]
    units = int(nav_ins[1:])

    deltas = directions[ins]
    boat['x'] += deltas[0]*units
    boat['y'] += deltas[1]*units
    boat['compass'] = (boat['compass'] + deltas[2]*units) % 360

    return boat

nav_instructions = []

for line in sys.stdin:
    nav_ins = line.strip()
    boat = update_boat(boat, nav_ins)
    #print(boat)

print(abs(boat['x']) + abs(boat['y']))
