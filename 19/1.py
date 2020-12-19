#!/usr/bin/python3

import sys
#import copy
import re

rules = {}
messages = []

def evaluate(rule_num, text):
    pass

def proccess_rule(num):
    if rules[num][0] == '"':
        return rules[num][1]
    else:
        options = rules[num].split(' | ')
        if len(options) == 2:
            result = "("
            for in_rule in options[0].split(' '):
                result += proccess_rule(in_rule)
            result += '|'
            for in_rule in options[1].split(' '):
                result += proccess_rule(in_rule)
            result += ')'
            return result
        else:
            result = ""
            for in_rule in options[0].split(' '):
                result += proccess_rule(in_rule)
            return result


first_part = True
for line in sys.stdin:
    if line == '\n':
        first_part = False
    elif first_part:
        num, rule = line.strip().split(': ')
        #options = rule.split(' | ')
        rules[num] = rule
    else:
        messages.append(line.strip())
        
print(rules)
#print(messages)
regex = '^' + proccess_rule('0') + '$'
print(regex)

reg_c = re.compile(regex)

valid = 0
for message in messages:
    if reg_c.match(message):
        valid += 1
print(valid)
