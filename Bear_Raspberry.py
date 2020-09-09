# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:28:51 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/385/A --- Alexis Galvan


def raspberry():
    
    total = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    
    
    output = 0
    for i in range(len(prices)):
        if i == len(prices)-1:
            break
        
        bought = prices[i+1]
        sold = prices[i]
        temp = (sold-bought-total[1])
        if temp > output:
            output = temp
    
    return output

A = raspberry()
print(A)
        