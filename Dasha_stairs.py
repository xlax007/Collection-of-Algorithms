# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 00:48:57 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/761/A --- Alexis Galvan


def dasha_stairs():
    
    stairs = list(map(int, input().split()))
    
    if stairs[0] == 0 and stairs[1] == 0:
        return 'NO'
    elif stairs[0] == stairs[1]:
        return 'YES'
    elif stairs[0] < 0 or stairs[1] < 0:
        return 'NO'
    elif (stairs[1]-stairs[0]) == 1 or (stairs[0]-stairs[1]) == 1:
        return 'YES'
    else:
        return 'NO'
    
A = dasha_stairs()
print(A)