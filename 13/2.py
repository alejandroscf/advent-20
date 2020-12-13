#!/usr/bin/python3

import sys
#import copy
#import re

file_lines = []
arrival = 0
freqs = {}

for line in sys.stdin:
    file_lines.append(line.strip())

#arrival = int(file_lines[0])

for idx, freq in enumerate(file_lines[1].split(',')):
    if freq != 'x':
        freqs[idx] = int(freq)

print(freqs)
