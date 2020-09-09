# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 23:57:30 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/102/B --- Alexis Galvan


def sum_digits():
    
    digit = int(input())
    
    if len(str(digit)) == 1:
        return 0
    
    output = 0
    
    while len(str(digit)) != 1:
        temp = str(digit)
        new_digit = 0
        for i in range(len(temp)):
            new_digit += int(temp[i])

        output += 1
        digit = new_digit
    
    return output

A = sum_digits()
print(A)