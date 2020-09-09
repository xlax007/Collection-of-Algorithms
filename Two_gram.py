# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:31:27 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/977/B


def two_gram():
    total_letters = int(input())
    string = input()
    dic = {}
    
    for i in range(1,len(string)):
        temp = string[i-1] + string[i]
        if temp not in dic:
            dic[temp] = 1
        else:
            dic[temp] += 1
    
    maximum = 0
    
    for i in dic:
        if dic[i] > maximum:
            maximum = dic[i]
            best = i
    
    print(best)
    return
            
        
two_gram()