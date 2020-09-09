# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:13:10 2020

@author: Lenovo
"""


##https://codeforces.com/problemset/problem/686/A

def free_icecream():
    distress = 0
    icecream = input().split() # 2 inputs, [0] = cases, [1] = currentIcecream
    
    for i in range(int(icecream[0])):
        new_kid = input().split() # 2 inputs, [0] = + or -, [1] = icecream
        if new_kid[0] == '-':
            if int(new_kid[1]) > int(icecream[1]):
                distress += 1
            else:
                icecream[1] = int(icecream[1]) - int(new_kid[1])
        else:
            icecream[1] = int(icecream[1]) + int(new_kid[1])
    
    print(icecream[1], distress)
        


free_icecream()