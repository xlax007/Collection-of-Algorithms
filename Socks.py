# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:49:21 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/460/A


def socks():
    socks = input().split()
    socks = [int(i) for i in socks]
    output = 0
    while True:
        output += socks[0]
        if socks[0]/socks[1] < 1:
            break
        temp = int(socks[0]/socks[1])        
        socks[0] = temp + (socks[0] % temp)

    
    print(output)
    
socks()
        
        
        
        
        
        
    
    
    
    
    
    



