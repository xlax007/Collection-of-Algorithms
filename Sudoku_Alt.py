# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:25:40 2020

@author: Lenovo
"""



def get_zones(matrixAux):
    matrix = matrixAux.copy()
    zones = [[] for i in range(9)]
    zone = j = i = 0
    while len(matrix) != 0:
        zones[zone].append(matrix[i][j])
        j += 1
        if j % 3 == 0:
            j -= 3
            i += 1
        if i == 3:
            i = 0
            j += 3
            zone += 1
        if i == 0 and j == len(matrix[0]):
            matrix.pop(0)
            matrix.pop(0)
            matrix.pop(0)
            i = 0
            j = 0
    return zones

def missing_numbers(array):
    dic = {1:True,2:True,3:True,4:True,5:True,6:True,7:True,8:True,9:True}
    output = []
    for i in array:
        if i in dic:
            dic[i] = False
    for i in dic:
        if dic[i]:
            output.append(i)
    return output
            
def posible_positions(matrix, array, position):
    seen = False
    dic = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    if position == 0:
        i = j = 0
    elif position == 1:
        i = 0
        j = 3
    elif position == 2:
        i = 0 
        j = 6
    elif position == 3:
        i = 3
        j = 0
    elif position == 4 :
        i = 3
        j = 3
    elif position == 5:
        i = 3
        j = 6
    elif position == 6:
        i = 6
        j = 0
    elif position == 7:
        i = 6
        j = 3
    elif position == 8:
        i = 6
        j = 6
        
    for y in range(3):
        for z in range(3):
            if matrix[i][j] == 0:
                for x in array:
                    for number in matrix[i]:
                        if x == number:
                            seen = True
                            break
                    for number in range(len(matrix)):
                        if x == matrix[number][j]:
                            seen = True
                            break
                    if seen:
                        seen = False
                    else:
                        dic[x] += 1
            j += 1
        j -= 3
        i += 1
    i -= 3
    for times in dic:
        if dic[times] == 1:
            for y in range(3):
                for z in range(3):
                    if matrix[i][j] == 0:
                        for number in matrix[i]:
                            if times == number:
                                seen = True
                                break
                        for number in range(len(matrix)):
                            if times == matrix[number][j]:
                                seen = True
                                break
                        if seen:
                            seen = False
                        else:
                            matrix[i][j] = times
                            return matrix
                    j += 1
                j -= 3
                i += 1
    return matrix
                        
    
def sudoku(matrix): #9x9

    m = 0
    while True:
        zones = get_zones(matrix)
        completed = True
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    completed = False
                    break
            if not completed:
                break
        
        if completed:
            return matrix
        
        missing = missing_numbers(zones[m])
        matrix = posible_positions(matrix, missing, m)
        
        
        m += 1
        
        if m == 9:
            m = 0 
    



matrix = [[6,0,2,0,8,0,7,4,0],
          [7,0,0,2,9,0,6,0,1],
          [0,0,0,7,0,1,2,0,0],
          [0,0,8,4,0,0,3,0,0],
          [0,0,3,0,2,0,4,0,0],
          [0,0,1,0,0,3,9,0,0],
          [0,0,7,8,0,2,0,0,0],
          [3,0,6,0,4,9,0,0,7],
          [0,5,4,0,7,0,8,0,3]]

sudoku(matrix)