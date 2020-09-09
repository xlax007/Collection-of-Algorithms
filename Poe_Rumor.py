# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 06:06:46 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/893/C --- Alexis Galvan

import math

def poe_rumor():
    
    friends = list(map(int, input().split()))
    
    gold = list(map(int, input().split()))
    
    pairs = []
    
    for i in range(friends[1]):
        pairs.append(list(map(int, input().split())))
    
    if friends[1] == 0:
        output = 0
        for i in range(len(gold)):
            output += gold[i]
        return output
    
    conected = {}
    
    for i in range(len(pairs)):
        conected[pairs[i][0]] = pairs[i][1]
    
    lista = []
    
    while len(conected) > 0:
        temp = []
        temp.append(next(iter(conected)))
        temp.append(conected[next(iter(conected))])
        holder = conected[next(iter(conected))]
        conected.pop(next(iter(conected)))
        if len(conected) == 0:
            lista.append(temp)
            break
        while True:
            if holder in conected:
                temp.append(conected[holder])
                holder = conected[holder]
                conected.pop(temp[-2])
            else:
                lista.append(temp)
                break
    
    pop = []
    output = 0
    for i in range(len(lista)):
        minimum = math.inf
        for j in range(len(lista[i])):
            if gold[(lista[i][j])-1] < minimum:
                minimum = gold[lista[i][j]-1]
            pop.append((lista[i][j])-1)
        output += minimum
    
    for i in range(len(pop)):
        gold.pop(pop[(-i)-1])
    
    if len(gold) == 0:
        return output
    else:
        for i in range(len(gold)):
            output += gold[i]
        return output
    
A = poe_rumor()
print(A)    
    
                        
            

        
        
        
        