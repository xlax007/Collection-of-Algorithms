# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 02:27:38 2020

@author: alexi
"""



#http://codeforces.com/problemset/problem/1169/A -- Alexis Galvan


def circle_metro():
    subway = list(map(int, input().split()))

    if subway[1] == subway[3]:
        return 'YES'
    if subway[1] % 2 == 0:
        if subway[3] % 2 != 0:
            return 'NO'
    else:
        if subway[3] % 2 == 0:
            return 'NO'
    
    while True:
        subway[1] = subway[1] + 1
        subway[3] = subway[3] - 1
        
        if subway[1] == subway[3]:
            return 'YES'
        
        if subway[1] > subway[0]:
            subway[1] = 1
        if subway[3] < 1:
            subway[3] = subway[0]
        
        if subway[1] == subway[2]:
            return 'NO'
        elif subway[3] == subway[4]:
            return 'NO'
        
        
answer = circle_metro()
print(answer)
            