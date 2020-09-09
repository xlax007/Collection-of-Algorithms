# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:38:58 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/194/A --- Alexis Galvan


def A_exams():
    
    exams = list(map(int, input().split()))
    
    if exams[1] / exams[0] == 2:
        return exams[0]
    
    tests = exams[0]  
    need = int(exams[0]*2)
    
    while True:
        tests -= 1
        need += 1
        if need == exams[1]:
            return tests
        if tests == 0:
            return 0
        
A = A_exams()
print(A)
        
        