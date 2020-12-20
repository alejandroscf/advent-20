#!/usr/bin/python3

import sys
#import copy
import re


result=0

for line in sys.stdin:
    par = {}
    new_line=[]
    idx = 0
    par[idx] = ''
    #line_p, num = re.subn(r'([*+])',r')\1',line.strip())
    string = '( ' + line.strip() + ' )'
    for c in range(len(string)-1, -1, -1):
        if string[c] == ')':
            idx += 1
            par[idx] = ''
        if string[c] == '+' or string[c] == '*':
            new_line.append( ')' + string[c])
            par[idx] += '('
        elif string[c] == '(':
            new_line.append( string[c] + par[idx])
            par[idx] = ''
            idx += -1
        else:
            new_line.append( string[c] )

    #print( '( ' + line.strip() + ' )' )
    #print(new_line)
    new_line.reverse()
    new_exp = ''
    for i in new_line:
        new_exp += i
    #print(new_exp)
    #print(eval(new_exp))
    result += eval(new_exp)

print(result)
