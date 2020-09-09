# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:27:27 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/675/A --- Alexis Galvan


def infinite_sequence():
    
    numbers = list(map(int, input().split()))
    
    if numbers[0] == numbers[1] or (numbers[0]+numbers[2]) == numbers[1]:
        return 'YES'
    elif numbers[2] == 0 or (numbers[0] < numbers[1] and numbers[2] <= 1) or (numbers[0] > numbers[1]) and numbers[2] > 1:
        return 'NO'
    else:
        actual = numbers[0] + numbers[2]
        
        divisor = numbers[1]-actual
        
        if divisor % numbers[2] == 0:
            return 'YES'
        return 'NO'
    

A = infinite_sequence()
print(A)