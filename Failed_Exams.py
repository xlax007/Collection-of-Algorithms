# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:57:00 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/991/A --- Alexis Galvan


def failed_exams():
    
    places = list(map(int, input().split()))
    
    if places[0] > places[3] or places[1] > places[3] or places[2] > places[3]:
        return -1
    
    temp = places[2]
    
    places[0] -= temp
    places[1] -= temp
    places[3] -= temp
    
    if places[0] < 0 or places[1] < 0:
        return -1
    
    places[3] -= places[0]
    places[3] -= places[1]
    
    if places[3] < 0:
        return -1
    else:
        if places[3] == 0:
            return -1
        return places[3]
    
A = failed_exams()
print(A)