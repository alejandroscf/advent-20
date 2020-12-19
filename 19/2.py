#!/usr/bin/python3

import sys
#import copy
import regex

rules = {}
messages = []

def evaluate(rule_num, text):
    pass

def proccess_rule(num):
    if num == '8':
        return "(" + proccess_rule('42') + ")+"
    if num == '11':
        return "(?P<g11>(?P<g111>(" + proccess_rule('42') + ")){X}(?P<g112>(" + proccess_rule('31') + ")){X})"
        #return "(?P<g11>(?P<g111>(" + proccess_rule('42') + "))(?&g11)(?P<g112>(" + proccess_rule('31') + ")))"
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

rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'

#print(rules)
#print(messages)
regex_s = '^' + proccess_rule('0') + '$'
print(regex_s)
reg_c = []
for i in range(1, 10):
    reg_c.append(regex.compile(regex_s.replace('X',str(i)), regex.VERSION1))

valid = 0
for message in messages:
    for reg in reg_c:
        m = reg.match(message)
        if reg.match(message):
            #print(m.groupdict())
            valid += 1
print(valid)
