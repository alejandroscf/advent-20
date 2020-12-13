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
        freqs[int(freq)] = idx

#print(freqs)
lfreqs=list(freqs)
#print(lfreqs)

leap = lfreqs[0]
phase = 0
last_time = 0

for bus in lfreqs[1:]:
    #print("bus" + str(bus))
    phase = freqs[bus]
    while (last_time + freqs[bus])%bus != 0:
        #print(last_time)
        last_time += leap
    leap *= bus
print(last_time)
