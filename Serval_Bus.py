# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 03:00:29 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/1153/A --- Alexis Galvan

import math

def serval_bus():
    
    buses = list(map(int, input().split()))
    times = []
    
    minimum = math.inf
    index = 0
    for i in range(buses[0]):
        times.append(list(map(int, input().split())))
        if times[i][0] == buses[1]:
            return i+1
        elif times[i][0] > buses[1]:
            if (times[i][0]-buses[1]) < minimum:
                minimum = (times[i][0]-buses[1])
                index = i+1
    
    for i in range(len(times)):
        if times[i][0] > buses[1]:
            if (times[i][0]-buses[1]) < minimum:
                minimum = (times[i][0]-buses[1])
                index = i + 1
            continue
    
        add = times[i][1]
        times[i][1] = times[i][0] + add
        temp = buses[1] - times[i][1]
        times[i][1] += (math.ceil(temp/add)*add)
        if times[i][1] == buses[1]:
            return i + 1
        elif times[i][1] > buses[1]:
            if times[i][1] - buses[1] < minimum:
                minimum = (times[i][1] - buses[1])
                index = i + 1
        
        
    return index

    
A = serval_bus()    
print(A)
    