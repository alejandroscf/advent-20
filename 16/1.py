#!/usr/bin/python3

import sys
#import copy
import re


fields = {}
my_ticket = []
tickets = []
valid_numbers = set()

read_phase = 0

for line in sys.stdin:
    if line == '\n':
        read_phase += 1
    elif read_phase == 0:
        field, ranges = line.strip().split(': ')
        ranges_l = []
        for ran in ranges.split(' or '):
            min_n, max_n = ran.split('-')
            ranges_l.append((int(min_n), int(max_n)))
            valid_numbers.update(set(range(int(min_n),int(max_n)+1)))
        fields[field] = ranges_l
    elif read_phase == 1:
        if line[0] != 'y':
            my_ticket = line.strip().split(',')
    else:
        if line[0] != 'n':
            tickets.append(line.strip().split(','))

#print(fields)
#print(my_ticket)
#print(tickets)
#print(valid_numbers)
#print(len(tickets))

result = 0
invalid = False
for ticket in tickets.copy():
    for field in ticket:
        if int(field) not in valid_numbers:
            #print('invalid')
            result += int(field)
            invalid = True
    if invalid:
        tickets.remove(ticket)
print('part one')
print(result)
