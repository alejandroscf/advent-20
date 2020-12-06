#!/usr/bin/python3

import sys

groups = []
result = 0

first = True
group = set()
for line in sys.stdin:
    if line == '\n':
        #print(group)
        #print("----------")
        #groups.append(group)
        result += len(group)
        group = set()
        first = True
    else:
        #print(line)
        passenger = set()
        for answer in line.strip():
            passenger.add(answer)
        if first:
            group = passenger
            first = False
        else:
            group = group.intersection(passenger)

#print(groups)
#print(len(groups))

print(result)


