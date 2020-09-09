# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:34:56 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/1177/A --- Alexis Galvan


def digits_sequence():
    
    number = int(input())
    
    if number < 10:
        return number
    
    string = ''
    temp = 1
    
    while len(string) < number:
        string += str(temp)
        temp += 1
    
    return string[number-1]

A = digits_sequence()
print(A)
    