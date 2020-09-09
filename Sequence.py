# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:50:33 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1102/A

def sequence():
    number = int(input())
    a = []
    b = []
    A = 0
    B = 0
    if number == 1:
        print(0)
        return
    half = int(number/2)
    a.append(1)
    A += 1
    b.append(number)
    B += number
    for i in range(half, number-1):
        a.append(i+1)
        A += (i+1)
    
    for i in range(1,half):
        b.append(i+1)
        B += (i+1)
        
    print(abs(A-B))
    return
        
        
sequence()
    
    
    