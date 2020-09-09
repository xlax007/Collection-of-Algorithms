# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 23:28:25 2020

@author: alexi
"""



#https://codeforces.com/contest/1288/problem/A --- Alexis Galvan

import math

def deadline():
    
    cases = int(input())
    program = []
    
    for i in range(cases):
        program.append(list(map(int, input().split())))
    
    for i in range(len(program)):
        if program[i][1] <= program[i][0]:
            print('YES')
            continue
        
        L = 1
        R = program[i][0]-1
        
        found = False
        while L <= R:
            mid = L + (int((R-L)/2))
            
            temp = program[i][0] - mid
            temp_opt = math.ceil(program[i][1]/(mid+1))
            
            if temp >= temp_opt:
                print('YES')
                found = True
                break
            elif temp < temp_opt:
                L = mid + 1
            else:
                R = mid - 1
        
        if not found:
            print('NO')
            
            
            
    
deadline()