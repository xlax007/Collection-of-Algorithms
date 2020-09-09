# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:24:35 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1176/A

def divide_it():
    
    cases = int(input())
    individual = []
    for i in range(cases):
        individual.append(int(input()))
    
    for i in range(len(individual)):
        temp = 0
        while individual[i] != 1:
            if individual[i] % 2 == 0:
                temp += 1
                individual[i] = individual[i] / 2
            elif individual[i] % 3 == 0:
                temp += 1
                individual[i] = (individual[i]*2)/3
            elif individual[i] % 5 == 0:
                temp += 1
                individual[i] = (individual[i]*4)/5
            else:
                print(-1)
                break
        
        if individual[i] == 1:
            print(temp)
        
    return
            
divide_it()