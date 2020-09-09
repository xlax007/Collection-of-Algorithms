# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 05:29:52 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/1055/A --- Alexis Galvan


def metro():
    
    home = list(map(int, input().split()))
    
    metroA = list(map(int, input().split()))
    metroB = list(map(int, input().split()))
    
    if home[1] == 1:
        return 'YES'
    elif metroA[0] == 0:
        return 'NO'
    elif metroA[home[1]-1] == 0 and metroB[home[1]-1] == 0:
        return 'NO'
    
    i = home[1]-1
    if metroA[i] == 1:
        return 'YES'
    i += 1
    while i != len(metroA):
        if metroA[i] == 1 and metroB[i] == 1:
            return 'YES'
        i += 1
        
    return 'NO'


A = metro()
print(A)
        
        

        
        

        
        
        