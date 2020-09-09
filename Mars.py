# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:23:05 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/670/A


def work_mars():
    days = int(input())
    
    if days == 1:
        print(0, 1)
    elif days == 0:
        print(0, 0)
    elif days < 6:
        print(0, 2)
    elif days == 6:
        print(1, 2)
    elif days < 8:
        print(2, 2)
    else:
        takeoff = 0
        while True:
            if days % 7 != 0:
                days -= 1
                takeoff += 1
            else:
                break
        weeks = int(days/7)
        if takeoff == 6:
            minimum = int(weeks*2) + 1
        else:
            minimum = int(weeks*2)
           
        if takeoff == 0:
            maximum = minimum
        elif takeoff == 1:
            maximum = minimum + 1
        elif takeoff != 6:
            maximum = minimum + 2
        else:
            maximum = minimum + 1
        
        print(minimum, maximum)


work_mars()
    