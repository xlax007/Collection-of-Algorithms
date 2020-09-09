# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:51:59 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1047/A


def love_3():
    number = int(input())
    
    if number == 3:
        print(1, 1, 1)
        return
    
    temp = number
    others = 0
    
    while True:
        temp -= 2
        others += 1
        if temp % 3 != 0:
            print(temp, others, others)
            return
    
love_3()