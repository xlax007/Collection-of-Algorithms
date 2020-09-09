# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:57:00 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/714/A --- Alexis Galvan


def meet_friends():
    
    times = list(map(int, input().split()))
    
    if times[2] > times[1] or times[3] < times[0]:
        return 0
    
    output = 0
    if times[2] > times[0]:
        if times[3] > times[1]:
            output += abs(times[1]-times[2])+1
            if times[4] >= times[2] and times[4] <= times[1]:
                output -= 1
        else:
            output += abs(times[3]-times[2])+1
            if times[4] >= times[2] and times[4] <= times[3]:
                output -= 1
    else:
        if times[3] > times[1]:
            output += abs(times[1]-times[0])+1
            if times[4] >= times[0] and times[4] <= times[1]:
                output -= 1
        else:
            output += abs(times[3]-times[0])+1
            if times[4] >= times[0] and times[4] <= times[3]:
                output -= 1
            
    return output
    


A = meet_friends()
print(A)
            
            
    
    