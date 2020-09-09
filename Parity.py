# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:25:36 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1110/A - Alexis Galvan

def parity():
    k = input().split()
    k = [int(i) for i in k]
    numbers = input().split()
    
    answer = 0
    for i in range(len(numbers)):
        answer += (int(numbers[i])) * ((k[0])**((k[1])-(i+1)))
        
    if answer % 2 == 0:
        print("even")
    else:
        print("odd")
    
parity()
        