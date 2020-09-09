# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:11:16 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/276/A

def rabbits():
    cases = input().split() # [0] = restaurants, [1] = posible time
    restaurants = []
    maximum = 0
    for i in range(int(cases[0])):
        restaurants.append(input().split())
        if int(restaurants[i][1]) <= int(cases[1]):
            if int(restaurants[i][0]) > maximum:
                maximum = int(restaurants[i][0])
    
    if maximum > 0:
        print(maximum)
    else:
        print(-1)


rabbits()
        
    
    
        
    
    