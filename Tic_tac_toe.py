# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:24:18 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/754/B --- Alexis Galvan





def check(matrix, i, j):
    
    for new_position in [(0, 1),(0, -1),(1, 0),(-1, 0),(-1, -1),(-1, 1),(1, -1),(1, 1)]:
        
        node_position = (i + new_position[0], j + new_position[1])
        node_position2 = (i + (new_position[0]*2), j + (new_position[1]*2))
        
        if node_position[0] < 0 or node_position2[0] < 0 or node_position[1] > len(matrix)-1 or node_position2[1] > len(matrix)-1:
            continue
        
        if node_position[0] > len(matrix)-1 or node_position2[0] > len(matrix)-1 or node_position[1] < 0 or node_position2[1] < 0:
            continue
        
        if matrix[node_position[0]][node_position[1]] == 'x' and matrix[node_position2[0]][node_position2[1]] == '.':
            return True
        elif matrix[node_position2[0]][node_position2[1]] == 'x' and matrix[node_position[0]][node_position[1]] == '.':
            return True


            

def tic_tac_move():
    
    matrix = [input() for i in range(4)]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'x':
                if check(matrix, i, j):
                    return 'YES'
    return 'NO'

print(tic_tac_move())