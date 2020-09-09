# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:34:03 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1187/A

def kinder_eggs():
    cases = int(input())
    eggs = []
    
    for i in range(cases):
        eggs.append(input().split())
        
    for i in range(len(eggs)):
        if eggs[i][0] == eggs[i][1] == eggs[i][2]:
            print(1)
            continue
        
        maximum = min(int(eggs[i][1]),int(eggs[i][2]))
        
        buy = (int(eggs[i][0]) - maximum) + 1
        
        print(buy)
        

kinder_eggs()


