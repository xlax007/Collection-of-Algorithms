# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:59:14 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/978/A

def eliminate_duplicates():
    inputs = int(input())
    tests = input().split()
    
    dic = {}
    i = -1
    while True:
        if tests[i] not in dic:
            dic[tests[i]] = 0
            i -= 1
        else:
            tests.pop(i)
        
        if -i == len(tests)+1:
            output = ""
            print(len(tests))
            for i in tests:
                if len(output) == 0:
                    output = i
                else:
                    output = output + " " + i
            print(output)
            return
            
        
eliminate_duplicates()
