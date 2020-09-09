# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:44:36 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1091/A


def chrismas_tree():
    lights = input().split()
    
    lights = [int(i) for i in lights]
    
    min_index = 0
    minimum = lights[0]
    
    for i in range(1,len(lights)):
        if lights[i] < minimum:
            minimum = i
            min_index = i
    
    if min_index == 0:
        while True:
            if lights[1] > lights[0] and lights[2] > (lights[0]+1):
                print(lights[0] + (lights[0]+1) + (lights[0]+2))
                return
            else:
                lights[0] -= 1
                   
    elif min_index == 1:
        while True:
            if lights[0] >= (lights[1]-1) and lights[2] > lights[1]:
                print((lights[1]-1) + (lights[1]) + (lights[1]+1))
                return
            else:
                lights[1] -= 1        
    else:
        while True:
            if (lights[2]-2) <= lights[0] and (lights[2]-1) <= lights[1]:
                print(lights[2] + (lights[2]-1) + (lights[2]-2))
                return
            else:
                lights[2] -= 1
                
        


chrismas_tree()