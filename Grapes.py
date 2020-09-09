# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:57:56 2020

@author: Lenovo
"""


### https://codeforces.com/problemset/problem/1114/A

def grapes():
    
    hungry = input().split() #Andrew, Dimitri and Michal
    grapes = input().split()
    
    hungry = [int(i) for i in hungry]
    grapes = [int(i) for i in grapes]
    
    if hungry[0] > 0:
        if grapes[0] >= hungry[0]:
            grapes[0] -= hungry[0]
            hungry[0] = 0
        else:
            print("NO")
            return
    
    grapes[0] = grapes[0] + grapes[1]
    grapes.pop(1)

    if hungry[1] > 0:
        if grapes[0] >= hungry[1]:
            grapes[0] -= hungry[1]
            hungry[1] = 0
        else:
            print("NO")
            return
        
    grapes[0] = grapes[0] + grapes[1]
    grapes.pop(1)
    
    if hungry[2] > 0:
        if grapes[0] >= hungry[2]:
            hungry[1] = 0
        else:
            print("NO")
            return
        
    print("YES")
    return
            
grapes()
 