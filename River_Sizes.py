# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:13:04 2020

@author: alexi
"""



#MAXIMUM RIVER SIZES IN MATRIX --- Alexis Galvan


def check(i, j, matrix, bol_matrix):
    
    output = 1
    found = []
    
    for new_position in [(0, 1),(0, -1),(1, 0),(-1, 0)]:
        
        node_position = (i + new_position[0], j + new_position[1])
        
        if node_position[0] < 0 or node_position[0] > len(matrix)-1 or node_position[1] < 0 or node_position[1] > len(matrix[node_position[0]])-1:
            continue
        
        if matrix[node_position[0]][node_position[1]] == 1 and not bol_matrix[node_position[0]][node_position[1]][0]:
            bol_matrix[node_position[0]][node_position[1]][0] = True
            found.append([node_position[0],node_position[1]])
    
    for i in range(len(found)):
        temp, bol_matrix = check(found[i][0],found[i][1], matrix, bol_matrix)
        output = output + temp
    
    return output, bol_matrix
        


def river_size(matrix):
    
    bol_matrix = [[[False] for j in range(len(matrix[i]))] for i in range(len(matrix))]
    
    
    output = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 and not bol_matrix[i][j][0]:
                bol_matrix[i][j][0] = True
                temp, bol_matrix = check(i, j, matrix, bol_matrix)
                if temp > output:
                    output = temp
    
    return output
                


matrix = [[0,1,0],
          [0,1,0],
          [1,1,1],
          [0,0,0],
          [1,1,1],
          [1,1,1],
          [1,1,1]]

river_size(matrix)