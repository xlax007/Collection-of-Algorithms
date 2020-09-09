# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:12:37 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/733/A

def alligator():
    string = input()
    maximum = 0
    dic = {'A','E','I','O','U','Y'}
    counter = 0
    if len(string) == 1:
        if string[0] in dic:
            print(1)
            return
        else:
            print(2)
            return
    for i in range(len(string)):
        if string[i] not in dic:
            counter += 1
            if counter > maximum:
                maximum = counter
        else:
            counter = 1
            if counter > maximum:
                maximum = counter
            
    print(maximum)
    
    
alligator()
            
        
    
    