# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 17:43:53 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1180/A


def rombos():
    size = int(input())
    
    total= 1
    
    if size == 1:
        print(1)
        return
    
    for i in range(1,size):
        total += (4 * i)
        
    print(total)
    
rombos()
        
