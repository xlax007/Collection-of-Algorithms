# -*- coding: utf-8 -*-
"""
Created on Mon May  4 02:21:57 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/158/B

import math

def taxi():
    
    length = int(input())
    groups = list(map(int, input().split()))
    
    return math.ceil(sum(groups)/4)

A = taxi()
print(A)
    
    