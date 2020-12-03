#!/usr/bin/python3

import sys


passwds = []
for line in sys.stdin:
    rang, char, passwd = line.split()
    passwds.append( { "rang": rang.split("-"), "char":char[0] , "passwd":passwd })

#print(passwds)

result = 0

for passwd in passwds:
    chars = passwd["passwd"].count(passwd["char"])
    if chars >= int(passwd["rang"][0]) and chars <= int(passwd["rang"][1]):
        result = result + 1

print(result)
