# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:22:26 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/230/A

def kirito_dragons():
    kirito = input().split()
    kirito = [int(i) for i in kirito]
    
    dragons = []
    
    for i in range(kirito[1]):
        dragons.append(input().split())
    
    i = 0 
    while len(dragons) > 0:
        if kirito[0] >= int(dragons[i][0]):
            kirito[0] += int(dragons[i][1])
            dragons.pop(i)
            i = 0
        else:
            i += 1
            if i >= len(dragons):
                print("NO")
                return
    
    print("YES")
    
kirito_dragons()
    
    
                
            
                
        