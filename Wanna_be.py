# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:50:06 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/469/A

def wanna_be():
    
    levels = int(input())
    littlex = input().split()
    littley = input().split()
    
    dic = {}
    
    for i in range(1,len(littlex)):
        if littlex[i] not in dic:
            dic[littlex[i]] = 1
    
    for i in range(1,len(littley)):
        if littley[i] not in dic:
            dic[littley[i]] = 1
    
    if len(dic) == levels:
        print('I become the guy.')
    else:
        print('Oh, my keyboard!')

    
wanna_be()



