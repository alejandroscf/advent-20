#!/usr/bin/python3

import sys
import re

bags = {}
inverse_bags = {}

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
            if container in inverse_bags:
                inverse_bags[container][color] = num
            else:
                inverse_bags[container] = { color: num }
    

#print(inverse_bags)
#print(len(inverse_bags))
#print()

#print(inverse_bags['shiny gold'])
#print(len(inverse_bags['shiny gold']))

#print()

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

def find_content(color):
    #print('-----find_content-----')
    #print(color)
    num_result = 1
    if color in inverse_bags:
        #print(inverse_bags[color])
        for bag in inverse_bags[color]:
            num_result += int(inverse_bags[color][bag]) * find_content(bag)
    return num_result

color = 'shiny gold'

# Remove 1 as we want the bags inside the first one!
print(find_content(color) - 1)
