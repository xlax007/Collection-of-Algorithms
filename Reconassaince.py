# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:39:32 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/34/A --- Alexis Galvan


    
        
def reconaissance():
    
    total = int(input())
    soldiers = list(map(int, input().split()))
    
    minimum = abs(soldiers[0]-soldiers[-1])
    index = [0+1, len(soldiers)]
    
    for i in range(1, len(soldiers)):
        if abs(soldiers[i]-soldiers[i-1]) < minimum:
            minimum = abs(soldiers[i]-soldiers[i-1])
            index = [i, i+1]
        
        if i != len(soldiers)-1:
            if abs(soldiers[i]-soldiers[i+1]) < minimum:
                minimum = abs(soldiers[i]-soldiers[i+1])
                index = [i+1, i+2]
    
    print(index[0],index[1])
        
    

reconaissance()