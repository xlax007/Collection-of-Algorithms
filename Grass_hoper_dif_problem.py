# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 01:45:14 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/641/A --- Alexis Galvan


def grass_hoper():
    
    length = int(input())
    cell = input()
    jumps = list(map(int, input().split()))
    
    already = [0]
    start = 0
    
    while True:
        if cell[start] == '>':
            start += jumps[start]
            if start in already:
                return 'INFINITE'
            elif start >= len(cell):
                return 'FINITE'
            else:
                already.append(start)
        else:
            start -= jumps[start]
            if start in already:
                return 'INFINITE'
            elif start < 0:
                return 'FINITE'
            else:
                already.append(start)

print(grass_hoper())
        
        
    
    
    