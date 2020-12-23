#!/usr/bin/python3

import sys
#import copy
import re


decks = {}
player = 0

for line in sys.stdin:
    if line == '\n':
        pass
    elif line[0] == 'P':
        #decks[player].reverse()
        player = int(line.strip()[:-1].split(' ')[1])
        decks[player] = []
    else:
        decks[player].append(int(line.strip()))
        
print(decks)
while len(decks[1]) != 0 and len(decks[2]) != 0:
    card1 = decks[1].pop(0)
    card2 = decks[2].pop(0)
    if card1 > card2:
        decks[1].append(card1)
        decks[1].append(card2)
    else:
        decks[2].append(card2)
        decks[2].append(card1)

for deck in decks.values():
    score = 0
    for idx, card in enumerate(deck):
        score += (len(deck)-idx) * card
    print(score)
