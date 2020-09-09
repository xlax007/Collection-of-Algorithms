# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:32:41 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1141/B


def rest_days():
    total = int(input())
    days = input().split()
    
    maximum = 0

    if int(days[0]) == 1 and int(days[-1]) == 1:
        i = 0
        temp = 0
        while int(days[i]) == 1:
            temp += 1
            days.pop(i)
            if len(days) == 0:
                print(temp)
                return
        i = -1
        while int(days[i]) == 1:
            temp += 1
            days.pop(i)
            if len(days) == 0:
                print(temp)
                return
            
        maximum = temp
    
    temp = 0
    for i in range(len(days)):
        if int(days[i]) == 1:
            temp += 1   
            if temp > maximum:
                maximum = temp
        else:
            temp = 0
    
    print(maximum)
    return

rest_days()
            