#!/usr/bin/python3

import sys

total = 2020

expenses = []
for line in sys.stdin:
    expenses.append(int(line))

expenses.sort()

i = 0
j = len(expenses) - 1

while i != j:
    suma = expenses[i] + expenses[j]
    if suma == total:
        print(expenses[i] * expenses[j])
        break
    elif suma > total:
        j=j-1
    else:
        i=i+1


#print(expenses)
