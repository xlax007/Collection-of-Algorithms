# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:33:48 2020

@author: Lenovo
"""


#https://codeforces.com/contest/1312/problem/A


def polygon():
    cases = int(input())
    size = []
    for i in range(cases):
        size.append(input().split())
    
    for i in range(len(size)):
        if int(size[i][1]) >= int(size[i][0])-1:
            print("NO")
        else:
            if int(size[i][0]) % int(size[i][1]) != 0:
                print("NO")
            else:
                print("YES")
    
polygon()
        
    