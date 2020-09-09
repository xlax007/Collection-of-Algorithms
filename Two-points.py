# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:30:42 2020

@author: Lenovo
"""


# https://codeforces.com/problemset/problem/1108/A

def two_points():
    cases = int(input())
    matrix = []
    
    for i in range(cases):
        matrix.append(input().split())
        
    while len(matrix) != 0:
        if matrix[0][0] != matrix[0][2]:
            print(matrix[0][0], matrix[0][2])
            matrix.pop(0)
        else:
            print(matrix[0][0], matrix[0][3])
            matrix.pop(0)
    
    return

two_points()
    