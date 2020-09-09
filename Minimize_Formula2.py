# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:36:27 2020

@author: alexi
"""



#Minimizing the sum with this formula - (a1 − x)^2 +(a2 − x)^2 +··· +(an − x)^2
# x = Sum all numbers / total of numbers

def minimize_formula2(array):
    
    added = sum(array)
    x = added/len(array)
    
    output = 0
    for i in range(len(array)):
        output += (array[i]-x)**2
    
    return output

array = list(map(int, input().split()))
A = minimize_formula2(array)
print(A)