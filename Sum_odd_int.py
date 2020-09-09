# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:26:57 2020

@author: alexi
"""



#https://codeforces.com/contest/1327/problem/A --- Alexis Galvan


def sum_odd():
    
    cases = int(input())
    numbers = [list(map(int, input().split())) for i in range(cases)]
    
    for i in range(len(numbers)):
        
        if numbers[i][0] >= (numbers[i][1]*numbers[i][1]) and (numbers[i][0]+numbers[i][1]) % 2 == 0:
            print('YES')
        else:
            print('NO')


sum_odd()