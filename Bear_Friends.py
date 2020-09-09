# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 03:55:20 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/653/A --- Alexis Galvan


def bear_friends():
    
    total = int(input())
    
    balls = list(map(int, input().split()))
    
    dic = {}
    
    for i in range(len(balls)):
        dic[balls[i]] = 1
        
        if (balls[i]+1) in dic and (balls[i]+2) in dic:
            return 'YES'
        elif (balls[i]+1) in dic and (balls[i]-1) in dic:
            return 'YES'
        elif (balls[i]-1) in dic and (balls[i]-2) in dic:
            return 'YES'
        
    return 'NO'

A = bear_friends()
print(A)