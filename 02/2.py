#!/usr/bin/python3

import sys


passwds = []
for line in sys.stdin:
    rang, char, passwd = line.split()
    passwds.append( { "rang": rang.split("-"), "char":char[0] , "passwd":passwd })

#print(passwds)

result = 0

for passwd in passwds:
    test1 = passwd["passwd"][int(passwd["rang"][0])-1] == passwd["char"]
    test2 = passwd["passwd"][int(passwd["rang"][1])-1] == passwd["char"]
    if test1 != test2:
        result = result + 1

print(result)
