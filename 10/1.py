#!/usr/bin/python3

import sys
from functools import lru_cache

adapters = []
for line in sys.stdin:
    adapters.append(int(line.strip()))

adapters.append(0)
adapters.sort()
device = adapters[len(adapters) - 1] + 3
adapters.append(device)

#print(adapters)
print(len(adapters))

joltages = {}
joltages[1] = 0
joltages[2] = 0
joltages[3] = 0

@lru_cache(maxsize=len(adapters))
def search_next(i):
    global good_branches
    #print("search_next; joltaje: " + str(adapters[i]))
    if adapters[i] > device:
        #print("rama mala")
        return 0
    elif adapters[i] == device:
        #print("rama buena!")
        return 1
    else:
        result = 0
        #print(adapters[slice(i+1,i+3+1)])
        for idx, next_adapter in enumerate(adapters[slice(i+1,i+3+1)]):
            #print("i: " + str(i) + " adapters[i]: " + str(adapters[i]) + " idx: " + str(idx) + " next_adapter: " + str(next_adapter) + " diff: " + str(next_adapter - adapters[i]) + " good_branches: " + str(good_branches) +" result: " + str(result))
            if next_adapter - adapters[i] in range(1, 3+1):
                #print("siguiente vale... entramos!")
                result += search_next(i+idx+1)
                #print("salimos")
        return result

print("Part one")
for idx in range(len(adapters) - 1):
    joltages[adapters[idx + 1] - adapters[idx]] += 1

print(joltages[1] * joltages[3])

print("Part two")
print(search_next(0))
