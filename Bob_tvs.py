# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:20:14 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/34/B
def quick(array):
    
    less = []
    equal = []
    greater = []
    
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        
        return quick(less) + equal + quick(greater)
    else:
        return array
    
    
def bob_tvs():
    cases = input().split()
    cases = [int(i) for i in cases]
    prices = input().split()
    
    prices = quick(prices)
    
    maximum = 0
    for i in range(cases[1]):
        maximum += int(prices[i])
    
    if maximum == 0:
        print(0)
        return
    elif maximum < 0:
        print(-maximum)
        return
    elif maximum > 0:
        print(-maximum)
        return
    
bob_tvs()
    
    
    
    
    