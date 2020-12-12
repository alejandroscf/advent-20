#!/usr/bin/python3

import sys
import copy
#import re

seats = []

for line in sys.stdin:
    seats.append([ pixel for pixel in line.strip()])

#print(seats)
print(len(seats))

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
            occ = occupied_around(seats,i, j)
            #print("i: " + str(i) + " j: " + str(j) + " seats[i][j]: " + str(seats[i][j]) + " occ: " + str(occ))
            if seat == 'L' and occ == 0:
                next_seats[i][j] = '#'
            elif seat == '#' and occ >= 4:
                next_seats[i][j] = 'L'
    return next_seats

# Part one
print('Executing part one')
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
