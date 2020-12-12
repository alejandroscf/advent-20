#!/usr/bin/python3

import sys
import copy
#import re

seats = []
seats_in_view = []

for line in sys.stdin:
    seats.append([ pixel for pixel in line.strip()])
    seats_in_view.append([ [] for pixel in line.strip()])

#print(seats)
print(len(seats))

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

def complete_seats_in_view(seats, seats_in_view):
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
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
                    #seats_occ += 1
                    seats_in_view[i][j].append([idx, jdx])
    return seats_in_view


def occupied_in_view(seats, i, j):
    seats_occ = 0
    for idx, jdx in seats_in_view[i][j]:
        if seats[idx][jdx] == '#':
            #print("chunk")
            seats_occ += 1
    return seats_occ
        
def occupied_around(seats,i, j):
    down_i = i-1
    down_j = j-1
    seats_occ = 0
    
    if down_i < 0:
        down_i = 0
    if down_j < 0:
        down_j = 0

    for idx, row in enumerate(seats[slice(down_i, i+1+1)]):
        #print(row)
        for jdx, elem in enumerate(row[slice(down_j,j+1+1)]):
            #print("i: " + str(idx) + " j: " + str(jdx))
            #print(elem)
            if (down_i + idx != i or down_j + jdx != j) and seats[down_i + idx][down_j + jdx] == '#':
                #print("chunk")
                #print(elem)
                seats_occ += 1
    return seats_occ

def update_seats(seats):
    next_seats = copy.deepcopy(seats)
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            #print(seats[i][j])
            #occupy = False
            #occ = occupied_around(seats,i, j)
            occ = occupied_in_view(seats,i, j)
            #print("i: " + str(i) + " j: " + str(j) + " seats[i][j]: " + str(seats[i][j]) + " occ: " + str(occ))
            if seat == 'L' and occ == 0:
                next_seats[i][j] = '#'
            #elif seat == '#' and occ >= 4:
            elif seat == '#' and occ >= 5:
                next_seats[i][j] = 'L'
    return next_seats

# Part one
print('Executing part two')
#print(occupied_in_view(seats, 0, 0))
seats_in_view = complete_seats_in_view(seats, seats_in_view)
next_seats = seats
last_seats = []
while next_seats != last_seats:
    #print("empieza bucle")
    last_seats = next_seats
    next_seats = update_seats(next_seats)
    #print("last_seat")
    #for i in last_seats:
    #    print(i)
    #print("next_seats")
    #for i in next_seats:
    #    print(i)
print(sum(row.count('#') for row in next_seats))

#print(occupied_around(1, 1))
