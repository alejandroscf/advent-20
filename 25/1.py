#!/usr/bin/python3

import sys
#import copy
import re

#transforms = []

def transform(subj, num):
    global transforms
    result = (num*subj)%20201227
    #transforms.append(result)
    return result

keys = []

for line in sys.stdin:
    keys.append(int(line.strip()))

card = keys[1]
door = keys[0]

loop_card = 0
loop_door = 0
loop_size = 0
pub_key = 1

while loop_door == 0 or loop_card == 0:
    loop_size += 1
    #print('loop_size', loop_size)
    pub_key = transform(7, pub_key)
    if card == pub_key:
        loop_card = loop_size
        card_key = pub_key
        print('card', loop_size, pub_key)
    if door == pub_key:
        loop_door = loop_size
        door_key = pub_key
        print('door', loop_size, pub_key)

enc_key = 1
for i in range(loop_card):
    enc_key = transform(door_key, enc_key)
    #print(enc_key)
print('enc_key', enc_key)
