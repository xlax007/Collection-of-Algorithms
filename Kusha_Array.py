# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:07:41 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/299/A --- Alexis Galvan


def Kusha():
    
    
    length = int(input())
    array = list(map(int, input().split()))
    
    for i in range(len(array)):
        pivot = array[i]
        if pivot == 1:
            return 1
        for j in range(len(array)):
            if array[j] % pivot != 0:
                break
            if j == len(array)-1:
                return pivot
    return -1

A = Kusha()
print(A)
            
            