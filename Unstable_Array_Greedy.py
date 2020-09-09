# -*- coding: utf-8 -*-
"""
Created on Fri May 15 03:41:06 2020

@author: alexi
"""



#http://codeforces.com/contest/1353/problem/A --- Alexis Galvan Cardenas

def most_unstable():
    
    cases = int(input())
    
    numbers = [list(map(int, input().split())) for i in range(cases)]
    
    for i in range(len(numbers)):
        if numbers[i][0] == 1:
            print(0)
            continue
        elif numbers[i][0] == 2:
            print(numbers[i][1])
            continue
        
        print(int(numbers[i][1]*2))
        

most_unstable()