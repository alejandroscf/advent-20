#!/usr/bin/python3

import sys
#import copy
import re


result=0

for line in sys.stdin:
    new_line=[]
    new_line, num = re.subn(r'([*])',r')\1(','( ' + line.strip() + ' )' )

    #print( '( ' + line.strip() + ' )' )
    #print(new_line)
    #print(new_exp)
    #print(eval(new_line))
    result += eval(new_line)

print(result)
