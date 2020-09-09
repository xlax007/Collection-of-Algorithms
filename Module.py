# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:30:23 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/913/A

def module():
    exponential = int(input())
    number = int(input())
     
    if exponential >= number:
        print(number)
        return
          
    print(number % (2**exponential))

module()
    