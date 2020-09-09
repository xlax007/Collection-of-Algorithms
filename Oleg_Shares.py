# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:26:13 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/793/A --- Alexis Galvan

def check_disible(divisor, array):
    aux = array[0] % divisor
    
    for i in range(len(array)):
        if array[i] % divisor != aux:
            return True
    return False


def checks():
    
    total = list(map(int, input().split()))
    checks = list(map(int, input().split()))
    
    if check_disible(total[1], checks):
        return -1
    
    output = 0
    
    minimum = min(checks)
    for i in range(len(checks)):
        if checks[i] != minimum:
            output += int((checks[i] - minimum) / total[1])
    
    return output

A = checks()
print(A)