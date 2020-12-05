#!/usr/bin/python3

import sys
import re

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
    #print(passport)
    #for key in ("byr","iyr","eyr","hgt","hcl","pid","cid"):
    for key in ("byr","iyr","eyr","hgt","hcl","ecl","pid"):
        if key in passport:
            if key == "byr":
                valid = valid and int(passport["byr"]) > 1920 and int(passport["byr"]) < 2002
                print(valid)
            elif key == "iyr":
                valid = valid and int(passport["iyr"]) > 2010 and int(passport["iyr"]) < 2020
                print(valid)
            elif key == "eyr":
                valid = valid and int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030
            elif key == "hgt":
                #print(passport["hgt"])
                num_cm=re.findall("^(\d+)cm$",passport["hgt"])
                num_in=re.findall("^(\d+)in$",passport["hgt"])
                #print(num_cm)
                #print(num_in)
                valid = valid and ((int(num_cm[0]) >= 150 and int(num_cm[0]) <= 193) or (int(num_in[0]) >= 59 and int(num_in[0]) <= 76))
                print(valid)
            elif key == "hcl":
                valid = valid and re.search("^#[0-9a-f]{6}$",passport["hcl"])
                print(valid)
            elif key == "ecl":
                valid = valid and passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
                print(valid)
            elif key == "pid":
                valid = valid and re.search("^\d{9}$", passport["pid"])
                print(valid)
            else:
                valid = False
                print(valid)
        else:
            valid = False
    if valid:
        print("valid")
        result += 1
    print("======================")
print(result)
