# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:32:28 2020

@author: alexi
"""



#http://codeforces.com/problemset/problem/678/A --- Alexis Galvan


def jonny_numbers():
    
    numbers = list(map(int, input().split()))
    
    if numbers[1] == 1:
        return numbers[0]+1
    elif numbers[1] > numbers[0]:
        return numbers[1]
    elif numbers[1] == numbers[0]:
        return int(numbers[1]*2)
    
    i = int(numbers[0]/numbers[1])
    while True:
        temp = numbers[1]*i
        if temp > numbers[0]:
            return temp
        i += 1
    
        
A = jonny_numbers()
print(A)