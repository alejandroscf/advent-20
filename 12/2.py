#!/usr/bin/python3

import sys
from math import pi, sin, cos, radians, degrees
#import copy
#import re


#
#  y > 0
#
#  ^      * waypoint
#  |  ^
#  | |_| compass = 0
#  |
#  |_______> x > 0
#  
#

boat = {
    'x' : 0,
    'y' : 0,
    'wp_x' : 10,
    'wp_y' : 1
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
    #print(nav_ins)
    ins = nav_ins[0]
    units = int(nav_ins[1:])

    directions = {
        'N': (0, 0, 0, 1),
        'S': (0, 0, 0, -1),
        'E': (0, 0, 1, 0),
        'W': (0, 0, -1, 0),
        'L': (0, 0, 1, 1),
        'R': (0, 0, -1, -1),
        'F': (1, 1, 0, 0)
    } 

    deltas = directions[ins]
    if ins in {'N', 'S', 'E', 'W', 'F'}:
        boat['x'] += deltas[0]*boat['wp_x']*units
        boat['y'] += deltas[1]*boat['wp_y']*units
        boat['wp_x'] += deltas[2]*units
        boat['wp_y'] += deltas[3]*units
    elif ins in {'L', 'R'}:
        new_wp_x = round( boat['wp_x']*cos(radians(deltas[2]*units)) - boat['wp_y']*sin(radians(deltas[2]*units)) )
        new_wp_y = round( boat['wp_x']*sin(radians(deltas[2]*units)) + boat['wp_y']*cos(radians(deltas[2]*units)) )
        boat['wp_x'] = new_wp_x
        boat['wp_y'] = new_wp_y
    
    return boat

nav_instructions = []

for line in sys.stdin:
    nav_ins = line.strip()
    boat = update_boat(boat, nav_ins)
    #print(boat)

print(abs(boat['x']) + abs(boat['y']))
