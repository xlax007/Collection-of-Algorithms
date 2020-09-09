# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:51:39 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/709/A


def orange_juice():
    cases = input().split()
    cases = [int(i) for i in cases]
    oranges = input().split()
    
    detector = 0
    output = 0
    for i in range(len(oranges)):
        if int(oranges[i]) <= cases[1]:
            detector += int(oranges[i])
            if detector > cases[2]:
                output += 1
                detector -= cases[2]
    
    print(output)
    return

orange_juice()
            