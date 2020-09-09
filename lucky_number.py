# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:13:12 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/122/A

def lucky_number():
    number = [input()]
    
    if int(number[0]) % 4 == 0 or int(number[0]) % 7 == 0:
        print("YES")
        return
    
    if len(number[0]) != 1:
        if int(number[0][1]) == 4 or int(number[0][1]) == 7:
            print("YES")
            return
    print("NO")
    return
    
lucky_number()
    
    
    