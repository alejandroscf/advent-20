#!/usr/bin/python3

import sys

total = 2020

expenses = []
for line in sys.stdin:
    expenses.append(int(line))

expenses.sort()

i = 0
j = len(expenses) - 1
k = 1

#jj = expenses[j] + expenses[j-1]
#while jj >= total:
#    j=j-1
#    jj = expenses[j] + expenses[j-1]

tj = j

while i != j - 1:
    print("i: " + str(i) + " -> " + str(expenses[i]))
    print("j: " + str(j) + " -> " + str(expenses[j]))
    print("k: " + str(k) + " -> " + str(expenses[k]))
    ij = expenses[i] + expenses[j]
    print("ij: " + str(ij))
    if ij < total:
        ijk= ij + expenses[k]
        print("ijk: " + str(ijk))
        if ijk == total:
            print(expenses[i] * expenses[j] * expenses[k])
            print(expenses[i])
            print(expenses[j])
            print(expenses[k])
            break
        if i == j - 2:
            j=tj
            i=i+1
            k=i+1
        elif k + 1 == j or ijk > total:
            j=j-1
            k=i+1
        else:
            k=k+1
    else:
        j=j-1
        tj=j
        
    print("----------------------------------------")


#print(expenses)
