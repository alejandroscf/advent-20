#!/usr/bin/python3

import sys
#import copy
import re
#import time

file_lines = []
memory = {}
mask = {}

def do_write(mask, addr, data):
    global memory
    addr = addr | mask[0]
    #print(format(addr, '036b'))
    #print(mask['X'])
    expand(mask['X'], format(addr, '036b'), data)

def expand(mask, addr, data):
    global memory
    #print('expand')
    #print(mask)
    #time.sleep(1)
    if int(mask) == 0:
        #print('fin')
        memory[int(addr, 2)] = data
    else:
        pos = mask.find('1')
        mask = mask[:pos] + str(0) + mask[pos + 1:]
        #print(mask)
        addr = addr[:pos] + str(0) + addr[pos + 1:]
        #print(addr)
        expand(mask, addr, data)
        addr = addr[:pos] + str(1) + addr[pos + 1:]
        expand(mask, addr, data)



for line in sys.stdin:
    ins, data = line.strip().split(' = ')
    if ins == 'mask':
        #mask[1] = int(data.replace('X', str(1)),2)
        mask[0] = int(data.replace('X', str(0)),2)
        mask['X'] = data.replace('1', str(0)).replace('X', str(1))
        #print(mask['X'])
    else:
        direction = int(re.findall('^mem\[(\d+)\]$', ins)[0])
        do_write(mask, direction, int(data))
    #file_lines.append(line.strip())

#print(memory)
print(sum(memory.values()))
