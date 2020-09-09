# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 01:33:55 2020

@author: alexi
"""



#https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen --- Alexis Galvan



def diagonal_dif(matrix):

    a = 0
    b = 0
    
    left = 0
    right = -1
    for i in range(len(matrix)):
        a += matrix[i][left]
        b += matrix[i][right]
        left += 1
        right -= 1
    
    return abs(a-b)


length = int(input())
matrix = [list(map(int, input().split())) for i in range(length)]

A = diagonal_dif(matrix)
print(A)