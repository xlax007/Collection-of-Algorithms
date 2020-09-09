# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:56:05 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/318/A

def even_odds():
    numbers = input().split()
    numbers = [int(i) for i in numbers]
    
    if numbers[1] == 1:
        print(1)
        return
    
    array = []
    odd = 1
    even = 2
    
    for i in range(numbers[0]):
        if odd <= numbers[0]:
            array.append(odd)
            if len(array) == (numbers[1]+2):
                break
            odd += 2
        else:
            array.append(even)
            if len(array) == (numbers[1]+2):
                break
            even += 2
    
    print(array[numbers[1]-1])
    
even_odds()