# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:48:22 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/1008/B --- Alexis Galvan
        

def non_ascending_rect():
    
    total = int(input())
    rect = []
    
    for i in range(total):
        rect.append(list(map(int, input().split())))
        if rect[i][1] > rect[i][0]:
            rect[i][1], rect[i][0] = rect[i][0], rect[i][1]
            
    if len(rect) == 1:
        return 'YES'
    
    for i in range(len(rect)-1):
        if rect[i][0] >= rect[i+1][0]:
            continue
                
        rect[i+1][0], rect[i+1][1] = rect[i+1][1],rect[i+1][0]
        
        if rect[i][0] >= rect[i+1][0]:
            continue
        else:
            return 'NO'
        
    return 'YES'

            

A = non_ascending_rect()
print(A)