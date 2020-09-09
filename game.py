# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:24:54 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/513/A


def game():
    array = input().split()
    
    array = [int(i) for i in array]
    
    while array[0] > 0 and array[1] > 0:
        array[0] -= 1
        if array[0] == 0:
            print("Second")
            return
        array[1] -= 1
        if array[1] == 0:
            print("First")
            return
        
        
game()
    