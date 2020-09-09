# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:52:42 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/32/B

def borze_code():
    string = input()
    output = ''
    
    if len(string) == 1:
        print(0)
        return
    
    i = 0
    while True:
        if string[i] == '.':
            output = output + str(0)
            i += 1
            if i >= len(string):
                break
        elif string[i] == '-':
            if string[i+1] == '.':
                output = output + str(1)
                i += 2
                if i >= len(string):
                    break
            elif string[i+1] == '-':
                output = output + str(2)
                i += 2
                if i >= len(string):
                    break
    
    print(output)
    return
                

borze_code()
            
                
        