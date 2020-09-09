# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 05:40:04 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/168/A --- Alexis Galvan

import math 

def wizards_city():
    wizards = list(map(int, input().split()))
    
    temp = math.ceil((wizards[0]/100)*(wizards[2]))
    
    if wizards[1] >= temp:
        return 0
    else:
        return temp - wizards[1]
    
A = wizards_city()
print(A)
    