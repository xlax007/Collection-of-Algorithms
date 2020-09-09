# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:22:37 2020

@author: Lenovo
"""


####https://codeforces.com/contest/1300/problem/A

def check_sum(array):
    total = 0
    for i in array:
        total += int(i)
    
    if total == 0:
        return False
    else:
        return True

def check_product(array):
    total = 1
    for i in array:
        total = total * int(i)
    
    if total == 0:
        return False
    else:
        return True

def non_zero():
    cases = int(input())
    matrix = []
    for i in range(cases):
        number_input = int(input())
        matrix.append(input().split())
        
    for i in range(len(matrix)):
        steps = 0
        while True:
            
            zero = False
            
            if check_sum(matrix[i]) and check_product(matrix[i]):
                print(steps)
                break
            
            for j in range(len(matrix[i])):
                if int(matrix[i][j]) == 0:
                    matrix[i][j] = int(matrix[i][j]) + 1
                    steps += 1
                    zero = True
            if zero:
                if check_sum(matrix[i]) and check_product(matrix[i]):
                    print(steps)
                    break
            else:
                if int(matrix[i][0]) > 0:
                    matrix[i][0] = int(matrix[i][0]) + 1
                    steps +=1
                else:
                    matrix[i][0] = int(matrix[i][0]) - 1
                    steps +=1
                
non_zero()
            
        