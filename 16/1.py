#!/usr/bin/python3

import sys
#import copy
import re


def valid_field(field, pos):
    values = set([ int(ticket[pos]) for ticket in tickets ])
    #print(values)
    return values.issubset(fields[field])

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
        ranges_s = set()
        for ran in ranges.split(' or '):
            min_n, max_n = ran.split('-')
            ranges_s.update(set(range(int(min_n),int(max_n)+1)))
            valid_numbers.update(set(range(int(min_n),int(max_n)+1)))
        fields[field] = ranges_s
    elif read_phase == 1:
        if line[0] != 'y':
            my_ticket = line.strip().split(',')
            tickets.append(line.strip().split(','))
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
        invalid = False
print('part one')
print(result)
print('part two')

field_option = {}
field_num = {}
answer_fields = []

for field in fields:
    #print(field)
    field_option[field] = []
    if field[0:9] == 'departure':
        answer_fields.append(field)
    for i in range(len(my_ticket)):
        #if i not in field_num.values():
        if True:
            if valid_field(field, i):
                field_option[field].append(i)
                #break

while len(field_num) < len(my_ticket):
    for field in field_option.copy():
        if len(field_option[field]) == 1:
            # Añadirlo a field_num
            field_num[field] = field_option[field][0]
            # Quitar esa opcion
            for all_field in field_option:
                field_option[all_field].remove(field_num[field])
            field_option.pop(field)
            break


#print(field_num)
#print(answer_fields)

answer = 1
for field in answer_fields:
    pass
    answer *= int(my_ticket[field_num[field]])
print(answer)
