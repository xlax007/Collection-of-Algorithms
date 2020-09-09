# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:07:49 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/805/A


def fake_np():
    numbers = input().split()
    numbers = [int(i) for i in numbers]
    
    if numbers[1] == numbers[0]:
        print(numbers[1])
        return
    print(2)
    return
 

fake_np()
            
 
            
    