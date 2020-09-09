# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:54:10 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/462/A --- Alexis Galvan


def check(i, j, matrix):
    counter = 0
    for new_position in [(0, 1),(0, -1),(-1, 0),(1, 0)]:
        
        node_position = (i+new_position[0], j+new_position[1])
        
        if node_position[0] < 0 or node_position[0] > len(matrix)-1 or node_position[1] < 0 or node_position[1] > len(matrix[node_position[0]])-1:
            continue
        
        if matrix[node_position[0]][node_position[1]] == 'o':
            counter += 1

    return counter
    

def apple_man():
    
    size_matrix = int(input())
    matrix = []
    
    for i in range(size_matrix):
        matrix.append(input())
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp = check(i, j, matrix)
            if temp % 2 != 0:
                return 'NO'
    return 'YES'

A = apple_man()
print(A)