# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:26:00 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1047/B

def cover_points():
    total = int(input())
    points = []
    
    for i in range(total):
        points.append(input().split())
        
    output = 1
    
    for i in range(len(points)):
        temp = int(points[i][0]) + int(points[i][1])
        if temp > output:
            output = temp
    
    print(output)
    return


cover_points()
    