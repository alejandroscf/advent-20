#!/usr/bin/python3

import sys

# sys.argv[1]: horizontal movement (rigth > 0)
# sys.argv[2]: vertical movement (down > 0)

passports = []
passport = {}
for line in sys.stdin:
    if line == '\n':
        passports.append(passport)
        passport = {}
    else:
        #print(line)
        for field in line[:-1].split(' '):
            key, value = field.split(':')
            passport[key] = value

print(passports)
print(len(passports))

result = 0

for passport in passports:
    valid = True
    #for key in ("byr","iyr","eyr","hgt","hcl","pid","cid"):
    for key in ("byr","iyr","eyr","hgt","hcl","pid"):
        if key in passport:
            valid = valid and True
        else:
            valid = False
    if valid:
        result = result + 1
print(result)
