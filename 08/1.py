#!/usr/bin/python3

import sys
import re

proccessor = {
    'accumulator' : 0,
    'current_ins' : 0,
    'next_ins' : 1, 
}

def reset_processor():
    global proccessor
    proccessor = {
        'accumulator' : 0,
        'current_ins' : 0,
        'next_ins' : 1, 
    }
    
def op_acc(param):
    global proccessor
    proccessor['next_ins'] = proccessor['current_ins'] + 1
    proccessor['accumulator'] += int(param)

def op_jmp(param):
    global proccessor
    proccessor['next_ins'] = proccessor['current_ins'] + int(param)

def op_nop(param):
    global proccessor
    proccessor['next_ins'] = proccessor['current_ins'] + 1

operations = { 
    'acc': op_acc, 
    'jmp': op_jmp, 
    'nop': op_nop 
}

def loop_detector(processor, instructions):
    
    used_ins = set()
    while proccessor['current_ins'] != len(instructions):
        #print(proccessor)
        if proccessor['current_ins'] in used_ins:
            #print('bucle!')
            #print(proccessor['accumulator'])
            return False
        execute(instructions[proccessor['current_ins']])
        used_ins.add(proccessor['current_ins'])
        proccessor['current_ins'] = proccessor['next_ins']
        #proccessor['next_ins'] += 1
    #print(proccessor['accumulator'])
    return True

def execute(instruction):
    
    #print(instruction)
    func, param = instruction.split(' ')
    func = operations.get(func)
    func(param)
    




instructions = []

for line in sys.stdin:
    instructions.append(line.strip())
# Part one
print('Executing part one')
loop_detector(proccessor, instructions)
print(proccessor['accumulator'])

# Part two
print('Executing part two')

for idx, ins in enumerate(instructions):
    reset_processor()
    mod_instructions = instructions.copy()
    #print(str(idx) + ": " + ins )
    if ins.split(' ')[0] == 'jmp':
        mod_instructions[idx] = instructions[idx].replace('jmp','nop') 
        if loop_detector(proccessor, mod_instructions):
            break
    elif ins.split(' ')[0] == 'nop':
        mod_instructions[idx] = instructions[idx].replace('nop','jmp') 
        if loop_detector(proccessor, mod_instructions):
            break
    
    #print(mod_instructions)

print(proccessor['accumulator'])
