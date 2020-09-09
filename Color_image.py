# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:28:20 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/707/A


def color_ornot():
    pixel = input().split()
    colors = []
    dic = {'C','M','Y'}
    
    for i in range(int(pixel[0])):
        colors.append(input().split())
        
    for i in range(len(colors)):
        for j in range(len(colors[i])):
            if colors[i][j] in dic:
                print('#Color')
                return
    
    print('#Black&White')
    


color_ornot()
