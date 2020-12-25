#!/usr/bin/python3

import sys
#import copy
import re

init_numbers = []
numbers = []
inv_numbers = {}

for line in sys.stdin:
    init_numbers = line.strip().split(',')


turn = 1
for num in init_numbers:
    numbers.append(int(num))
    inv_numbers[int(num)] = turn
    turn += 1

#print(numbers)
#print(inv_numbers)
#print(turn)
while turn <= 2020:
#while turn <= 10:
    last_num = numbers[turn-2]
    #print('last_num',last_num)
    if last_num in inv_numbers:
        new_num = turn-1-inv_numbers[last_num]
        #print(inv_numbers)
    else:
        new_num = 0
    #print('turn', turn, 'new_num', new_num)
    numbers.append(new_num)
    inv_numbers[last_num] = turn - 1
    turn += 1
print(numbers[turn-2])
