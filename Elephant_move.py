# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:39:57 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/617/A

def elephant_moves():
    move = int(input())
    if move == 0:
        print(0)
        return
    elif move <= 5:
        print(1)
        return
    
    if (move%5) == 0:
        print(int(move/5))
    else:
        print(int(move/5)+1)
    
    
elephant_moves()