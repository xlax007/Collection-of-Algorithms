# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:03:28 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/839/A


def arya_candles():
    total = input().split() # [0] = days [1] = how many he needs
    days = input().split()
    
    posible_days = 0
    accumulated = 0
    saved = 0
    
    for i in range(len(days)):
        days[i] = int(days[i]) + saved
        saved = 0
        if int(days[i]) <= 8:
            posible_days += 1
            total[1] = (int(total[1]) - int(days[i]))
            if total[1] < 1:
                print(posible_days)
                return
        else:
            posible_days += 1
            total[1] = (int(total[1]) - 8)
            if total[1] < 1:
                print(posible_days)
                return
            saved = (int(days[i]) - 8)
    
    print(-1)
            
arya_candles()
            
        
    
    
    
            