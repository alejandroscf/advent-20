#!/usr/bin/python3

import sys
import copy
#import re
import time

seats = []
list_seats = []

for line in sys.stdin:
    seats.append([ pixel for pixel in line.strip()])

#print(seats)
#print(len(seats))

directions = [
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1)
]

def complete_list_seats(seats, list_seats):
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seats[i][j] == 'L':
                in_view = []
                for delta_i, delta_j in directions:
                    idx = i + delta_i
                    jdx = j + delta_j
                    while idx >= 0 and idx < len(seats) and jdx >= 0 and jdx < len(seats[i]) and seats[idx][jdx] == '.':
                        #print("un poquico mas")
                        idx = idx + delta_i
                        jdx = jdx + delta_j

                    if idx < 0 or idx >= len(seats) or jdx < 0 or jdx >= len(seats[0]):
                        #print("que te sales")
                        continue

                    if seats[idx][jdx] in {'#', 'L'}:
                        #print("chunk")
                        in_view.append([idx, jdx])
                list_seats.append([i, j, in_view])
    return list_seats

def update_seats(seats):
    next_seats = copy.deepcopy(seats)
    for seatt in list_seats:
        occ = 0
        i = seatt[0]
        j = seatt[1]
        seat = seats[i][j]
        for idx, jdx in seatt[2]:
            if seats[idx][jdx] == '#':
                occ += 1
        if seat == 'L' and occ == 0:
            next_seats[i][j] = '#'
            changed = True
        elif seat == '#' and occ >= 5:
            next_seats[i][j] = 'L'
            changed = True
    return next_seats, changed


# Part one
print('Executing part two')
#print(occupied_in_view(seats, 0, 0))
list_seats = complete_list_seats(seats, list_seats)
#print(list_seats)
next_seats = seats
last_seats = []
changed = True
while changed:
    #print("empieza bucle")
    last_seats = next_seats
    next_seats, changed = update_seats(next_seats)
    #print("last_seat")
    #for i in last_seats:
    #    print(i)
    #print("next_seats")
    #for i in next_seats:
    #    print(i)
print(sum(row.count('#') for row in next_seats))

#print(occupied_around(1, 1))
