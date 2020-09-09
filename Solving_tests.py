# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:41:19 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/999/A


def solving_tests():
    cases = input().split() #[0] = tests, [1] = time to do it
    tests = input().split()
    
    cases = [int(i) for i in cases]
    
    output = 0
    
    while True:
        if len(tests) > 0:
            if cases[1] >= int(tests[0]):
                output += 1
                tests.pop(0)
            elif cases[1] >= int(tests[-1]):
                output += 1
                tests.pop()
            else:
                print(output)
                return
        else:
            break
    print(output)
    return
                
    
solving_tests()