# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:08:51 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/29/A --- Alexis Galvan


def spit_camels():
    
    camels = int(input())
    spit = [list(map(int, input().split())) for i in range(camels)]
    
    spited = {}
    
    for i in range(len(spit)):
        spited[spit[i][0]] = spit[i][0] + spit[i][1]
    
    for i in range(len(spited)):

        temp = spit[i][1] + spit[i][0]
        
        if temp in spited:
            if spited[temp] == spit[i][0]:
                return 'YES'
    
    return 'NO'

A = spit_camels()
print(A)
        