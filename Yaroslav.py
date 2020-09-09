# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:54:40 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/296/A --- Alexis Galvan


def yaroslav():
    
    length = int(input())
    array = list(map(int, input().split()))
    
    if len(array) == 1:
        return 'YES'
    
    dic = {}
    
    if len(array) % 2 == 0:
        for i in range(len(array)):
            if array[i] not in dic:
                dic[array[i]] = 1
            else:
                dic[array[i]] += 1
                if dic[array[i]] > (len(array)/2):
                    return 'NO'
    else:
        for i in range(len(array)):
            if array[i] not in dic:
                dic[array[i]] = 1
            else:
                dic[array[i]] += 1
                if dic[array[i]] == (int(len(array)/2))+2:
                    return 'NO'
    
    return 'YES'

A = yaroslav()
print(A)
                    
                    
                