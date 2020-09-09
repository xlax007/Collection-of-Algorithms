# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 02:16:13 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/984/B --- Alexis Galvan


def check_bombs(matrix, i, j):
     counter = 0
     for new_position in [(0, 1),(0, -1),(1, 0),(-1, 0),(-1, -1),(-1, 1),(1, -1),(1, 1)]:
        
        node_position = (i + new_position[0], j + new_position[1])
        
        if node_position[0] < 0 or node_position[0] > len(matrix)-1 or node_position[1] < 0 or node_position[1] > len(matrix[node_position[0]])-1:
            continue
        
        if matrix[node_position[0]][node_position[1]] == '*':
            counter += 1
    
     if int(matrix[i][j]) != counter:
         return True
        
        
    

def check_empty(matrix, i, j):
    
    for new_position in [(0, 1),(0, -1),(1, 0),(-1, 0),(-1, -1),(-1, 1),(1, -1),(1, 1)]:
        
        node_position = (i + new_position[0], j + new_position[1])
        
        if node_position[0] < 0 or node_position[0] > len(matrix)-1 or node_position[1] < 0 or node_position[1] > len(matrix[node_position[0]])-1:
            continue
        
        if matrix[node_position[0]][node_position[1]] == '*':
            return True
        


def mine_sweper():
    
    length = list(map(int, input().split()))
    
    matrix = [input() for i in range(length[0])]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '.':
                if check_empty(matrix, i, j):
                    return 'NO'
            elif matrix[i][j] == '*':
                continue
            else:
                if check_bombs(matrix, i, j):
                    return 'NO'
    
    return 'YES'
                

print(mine_sweper())