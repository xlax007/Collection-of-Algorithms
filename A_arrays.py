# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:45:14 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/572/A

def A_arrays():
    sizes = input().split()
    k = input().split()
    arrayA = input().split()
    arrayB = input().split()
    
    checkA = [] 
    for i in range(int(k[0])):
        checkA.append(arrayA[i])
        
    while True:
        if int(arrayB[0]) > int(checkA[-1]):
            if len(arrayB) >= int(k[1]):
                print('YES')
                return
        else:
            arrayB.pop(0)
            if len(arrayB) < int(k[1]):
                print("NO")
                return
            
A_arrays()
        
    