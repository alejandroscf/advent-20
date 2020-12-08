#!/usr/bin/python3

import sys
import re

proccesor = {
    'accumulator' : 0,
    'current_ins' : 0,
    'next_ins' : 1, 
}

def op_acc(param):
    global proccesor
    proccesor['next_ins'] = proccesor['current_ins'] + 1
    proccesor['accumulator'] += int(param)

def op_jmp(param):
    global proccesor
    proccesor['next_ins'] = proccesor['current_ins'] + int(param)

def op_nop(param):
    global proccesor
    proccesor['next_ins'] = proccesor['current_ins'] + 1

operations = { 
    'acc': op_acc, 
    'jmp': op_jmp, 
    'nop': op_nop 
}

def loop_detector(processor, instructions):
    
    used_ins = set()
    while True:
        #print(proccesor)
        if proccesor['current_ins'] in used_ins:
            print('bucle!')
            return proccesor['accumulator']
        execute(instructions[proccesor['current_ins']])
        used_ins.add(proccesor['current_ins'])
        proccesor['current_ins'] = proccesor['next_ins']
        #proccesor['next_ins'] += 1

def execute(instruction):
    
    #print(instruction)
    func, param = instruction.split(' ')
    func = operations.get(func)
    func(param)
    




instructions = []

for line in sys.stdin:
    instructions.append(line.strip())

print(loop_detector(proccesor, instructions))
