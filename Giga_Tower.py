# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:32:06 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/488/A --- Alexis Galvan


def giga_tower():
    
    floor = int(input())
    
    output = 0
    while True:
        output += 1
        floor += 1
        temp = str(floor)
        for i in temp:
            if i == '8':
                return output
            

A = giga_tower()
print(A)
                
    
    