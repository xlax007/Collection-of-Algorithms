# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 02:03:14 2020

@author: Lenovo
"""


###MINUTES TO NEW YEAR

def minutes_year():
    cases = input()
    times = []
    maximum = 1440
    for i in range(int(cases)):
        times.append(input().split())
    
    for i in range(len(times)):
        output = 0
        output += int((times[i][0]))*60
        output += int(times[i][1])
        print(maximum-output)
    
    return

minutes_year()