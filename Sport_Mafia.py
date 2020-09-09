# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:43:22 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/1195/B --- Alexis Galvan


def sport_mafia():
    
    candys = list(map(int, input().split()))
    
    if candys[0] == 1:
        return 0
    
    in_box = 0
    
    for i in range(1, candys[0]+1):
        in_box += i
        if (in_box - (candys[0]-i)) == candys[1]:
            return candys[0]-i

A = sport_mafia()
print(A)

    
    
    
    
    
    
    