# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 00:55:32 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/706/A --- Alexis Galvan


import math

def beru_taxi():
    
    position = list(map(int, input().split()))
    taxis = int(input())
    taxi_position = []
    for i in range(taxis):
        taxi_position.append(list(map(int, input().split())))
    
    best = math.sqrt(abs(taxi_position[0][1]-position[1])**2+(abs(taxi_position[0][0]-position[0]))**2)/taxi_position[0][2]
    
    for i in range(1, len(taxi_position)):
        temp = math.sqrt(abs(taxi_position[i][1]-position[1])**2+(abs(taxi_position[i][0]-position[0]))**2)/taxi_position[i][2]
        if temp < best:
            best = temp
    
    return best

A = beru_taxi()
print(A)
