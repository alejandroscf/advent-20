#!/usr/bin/python3

import sys
#import copy
import re

file_lines = []
memory = {}
mask = {}

def do_mask(mask, data):
    masked = data & mask[1]
    masked = masked | mask[0]
    return masked


for line in sys.stdin:
    ins, data = line.strip().split(' = ')
    if ins == 'mask':
        mask[1] = int(data.replace('X', str(1)),2)
        mask[0] = int(data.replace('X', str(0)),2)
    else:
        direction = int(re.findall('^mem\[(\d+)\]$', ins)[0])
        memory[direction] = do_mask(mask, int(data))
    #file_lines.append(line.strip())

#print(memory)
print(sum(memory.values()))
