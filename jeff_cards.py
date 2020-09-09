# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 01:49:15 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/352/A --- Alexis Galvan


def jeff_digits():
    
    total = int(input())
    cards = list(map(int, input().split()))
    
    table = {5:0,0:0}
    
    for i in range(len(cards)):
        table[cards[i]] += 1
    
    if table[5] < 9 and table[0] > 0:
        return 0
    elif table[5] < 9 and table[0] == 0:
        return -1
    elif table[0] == 0:
        return -1
    
    times = int(table[5]/9)
    
    temp = ('5'*9)*times
    
    temp_cero = ('0'*table[0])
    
    return int(temp+temp_cero)


A = jeff_digits()
print(A)
    
    