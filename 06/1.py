#!/usr/bin/python3

import sys

groups = []
result = 0

group = set()
for line in sys.stdin:
    if line == '\n':
        groups.append(group)
        result += len(group)
        group = set()
    else:
        #print(line)
        for answer in line.strip():
            group.add(answer)

#print(groups)
#print(len(groups))

print(result)


