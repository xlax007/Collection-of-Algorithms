# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:41:23 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1061/A


def coins():
    coins = input().split() ##[0] = coins i can use, [1] = coins we need to cap
    
    coins = [int(i) for i in coins]
    
    if coins[0] == 1:
        print(coins[1])
        return
    
    if (coins[1] % coins[0]) == 0:
        print(int(coins[1]/coins[0]))
        return
    else:
        print(int(coins[1]/coins[0])+1)
        return
        
    
    
coins()