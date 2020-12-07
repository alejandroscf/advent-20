#!/usr/bin/python3

import sys
import re

bags = {}

for line in sys.stdin:
    container, content_txt = line.strip().split(" bags contain ")
    contents = re.sub('( bag[s]*)','',content_txt[:-1]).split(", ")
    for bag in contents:
        if bag != 'no other':
            num, color = bag.split(" ", 1)
            if color in bags:
                bags[color].append((container, num))
            else:
                bags[color] = [(container, num)]
    
    #print(contents) 

print(bags)
#print(len(bags))
print()

print(bags['shiny gold'])
print(len(bags['shiny gold']))

print()

def find_container(color):
    print('-----find_container-----')
    print(color)
    if color not in bags:
        print('color not in bag')
        return set()
    else:
        print(bags[color])
        bag_set = set(color for color, num in bags[color])
        print(bag_set)
        for container in bag_set.copy():
            new_containers = find_container(container)
            for new_container in new_containers:
                bag_set.add(new_container)
        return bag_set

bag_set = set()
color = 'shiny gold'
bag_set = find_container(color)
print(bag_set)
print(len(bag_set))
