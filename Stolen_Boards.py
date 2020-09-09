# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:25:34 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1041/A


def stolen_boards():
    
    remaining = int(input())
    keyboards = input().split()
    output = 0
    dic = {}
    minimum = int(keyboards[0])
    maximum = minimum
    dic[int(keyboards[0])] = 1
    
    for i in range(1,len(keyboards)):
        dic[int(keyboards[i])] = 1
        if int(keyboards[i]) < minimum:
            minimum = int(keyboards[i])
        if int(keyboards[i]) > maximum:
            maximum = int(keyboards[i])
    
    output = (maximum - minimum) - (len(keyboards)-1)
    
    print(output)
    return

stolen_boards()