#!/usr/bin/python3

import sys
import re

PREAMBLE = int(sys.argv[1])
num_input = []
weakness = 0

for line in sys.stdin:
     num_input.append(int(line.strip()))


# Part one
print('Executing part one')
idx = 0
numbers = []

for curr_number in num_input:
    #print(curr_number)
    if idx >= PREAMBLE:
        valid = False
        for i in numbers:
            for j in numbers:
                if i + j == curr_number and i != j:
                    #print("valid")
                    valid = True
                    break
        if not valid:
            print(curr_number)
            weakness = curr_number
            break
        numbers.pop(0)
    if weakness != 0:
        break
    idx += 1
    numbers.append(curr_number)

two_result = 0
# Part two
print('Executing part two')
for i, num in enumerate(num_input):
    for j in range(i+1, idx):
        suma = sum(num_input[slice(i,j)])
        if suma == weakness:
            print(min(num_input[slice(i,j)]) + max(num_input[slice(i,j)]))
            two_result = min(num_input[slice(i,j)]) + max(num_input[slice(i,j)])
            break
        elif suma > weakness:
            break
    if two_result != 0:
        break

