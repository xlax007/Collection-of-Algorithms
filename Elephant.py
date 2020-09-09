# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:39:30 2020

@author: alexi
"""


#http://codeforces.com/problemset/problem/205/A


import math

def elephant():
    cities = int(input())
    towns = list(map(int, input().split()))
    
    table = {}
    duplicates = {}
    
    minimum = math.inf
    index = 0
    for i in range(len(towns)):
        if towns[i] not in table:
            table[towns[i]] = 1
            if towns[i] < minimum:
                minimum = towns[i]
                index = i+1
        else:
            duplicates[towns[i]] = 1
    
    if minimum not in duplicates:
        return index
    return 'Still Rozdil'


A = elephant()
print(A)