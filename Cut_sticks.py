# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:07:49 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/610/A

             
def cut():
    length = int(input())
    if length % 2 != 0 or length < 6:
        print(0)
        return
    else:
        if length % 4 == 0:
            print(int(length/4)-1)
        else:
            print(int(length/4))

cut()