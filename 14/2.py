#!/usr/bin/python3

import sys
#import copy
import re

file_lines = []
memory = {}
mask = {}

def do_mask(mask, data):
    #masked = data & mask[1]
    masked = data | mask[0]
    return masked

def do_write(mask, addr, data):
    global memory
    addr = addr | mask[0]
    expand(mask['X'], format(addr, '36b'))

def expand(mask, addr, data):
    global memory
    if mask == int(0):
        memory[int(addr, 2)] = data
    else:
        pos = mask.find('1')
        addr[pos] = 0
        expand(mask, addr)
        addr[pos] = 1
        expand(mask, addr)



for line in sys.stdin:
    ins, data = line.strip().split(' = ')
    if ins == 'mask':
        #mask[1] = int(data.replace('X', str(1)),2)
        mask[0] = int(data.replace('X', str(0)),2)
        mask['X'] = data.replace('1', str(0)).replace('X', str(1))
        print(mask['X'])
    else:
        direction = int(re.findall('^mem\[(\d+)\]$', ins)[0])
        do_write(mask, direction, int(data))
    #file_lines.append(line.strip())

#print(memory)
print(sum(memory.values()))
