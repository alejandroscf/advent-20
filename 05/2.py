#!/usr/bin/python3

import sys

def seat_to_bin(string):
    string = string.replace("F","0")
    string = string.replace("B","1")
    string = string.replace("L","0")
    string = string.replace("R","1")
    return int(string, 2)


seats = set(())
for line in sys.stdin:
    seats.add(seat_to_bin(line.strip()))

print(seats)
print(len(seats))

allseats = set(range(max(seats)))
free = allseats.difference(seats)
#print(free)

for seat in free:
    if seat + 1 in seats and seat - 1 in seats:
        print(seat)
