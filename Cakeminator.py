# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 00:09:39 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/330/A

def cake_eater():
    size = input().split()
    size = [int(i) for i in size]
    
    matrix = []
    
    for i in range(size[0]):
        matrix.append(input())
        
    output = 0
    
    rows = {}
    columns = {}
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S':
                rows[i] = 1
                columns[j] = 1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '.':
                if i not in rows or j not in columns:
                    output += 1
                    continue
            
        
    print(output)
    return
            
            
    
cake_eater()