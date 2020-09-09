# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:21:22 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/914/A --- Alexis Galvan

import math

def perfect_square():
    
    total = int(input())
    
    numbers = list(map(int, input().split()))
    
    output = min(numbers)
    
    for i in range(len(numbers)):
        if numbers[i] < 0:
            if numbers[i] > output:
                output = numbers[i]
        else: 
            temp = int(math.sqrt(numbers[i]))
            if temp*temp != numbers[i]:
                if numbers[i] > output:
                    output = numbers[i]

                
    return output

A = perfect_square()
print(A)
    