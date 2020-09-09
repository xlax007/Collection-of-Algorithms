# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:10:08 2020

@author: alexi
"""



#https://www.hackerrank.com/challenges/birthday-cake-candles/problem --- Alexis Galvan


def blow_candles(array):

    maximum = max(array)
    output = 0
    
    for i in range(len(array)):
        if array[i] == maximum:
            output += 1
    
    return output

length = int(input())
array = list(map(int, input().split()))
A = blow_candles(array)
print(A)