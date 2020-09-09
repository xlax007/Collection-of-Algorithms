# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 18:24:51 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/746/A

def recipe():
    lemons = int(input())
    apples = int(input())
    grapes = int(input())
    
    while True:
        if lemons*2 <= apples and lemons*4 <= grapes:
            print(lemons + (lemons*2) + (lemons*4))
            return
        lemons -= 1
        if lemons == 0:
            print(0)
            return
    
recipe()
    