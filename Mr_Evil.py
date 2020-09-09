# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 01:03:04 2020

@author: alexi
"""



#http://codeforces.com/problemset/problem/862/A --- Alexis Galvan


def mr_evil():
    target = list(map(int, input().split()))
    array = list(map(int, input().split()))
    
    
    output = 0
    

    
    if target[1] == 0:
        if 0 in array:
            return 1
        return 0
    
    if target[1] in array:
        output += 1
    target[1] -= 1
    while True:
        if target[1] not in array:
            output += 1
        target[1] -= 1
        if target[1] == -1:
            break
            
    

    return output
            
        

A = mr_evil()
print(A)