# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:36:40 2020

@author: alexi
"""



#Strongly Connected Components - Alexis Galvan Cardenas


def check_connection(letter, visited, stack, array):
    pop = []
    for i in range(len(array)):
        if letter == array[i][0] and array[i][1] not in visited:
            visited.append(array[i][1])
            check_connection(array[i][1], visited, stack, array)
            
    stack.append(letter)
    return visited, stack


def DFS(letter, visited, stack, array, component):
    for i in range(len(array)):
        if letter == array[i][1] and array[i][0] not in visited:
            visited.append(array[i][0])
            component.append(array[i][0])
            DFS(array[i][0], visited, stack, array, component)
    return component


def connected_components(array):
    
    visited = []
    stack = []
    reverse = array.copy()
    
    for i in range(len(array)):
        if array[i][0] not in visited:
            visited.append(array[i][0])
            check_connection(array[i][0], visited, stack, array) 
       
    visited = []
    components = []
    
    for i in range(len(stack)):
        if stack[(-i)-1] not in visited:
            components.append([stack[(-i)-1]])
            visited.append(stack[(-i)-1])
            temp = DFS(stack[(-i)-1], visited, stack, array, [])
            for j in range(len(temp)):
                if temp[j] not in components[-1]:
                    components[-1].append(temp[j])
    
    return components
            


test1 = [('A','B'),('B','C'),('C','A'),('B','D'),('D','E'),('E','F'),('F','D'),('G','H'),('H','I'),('G','F'),('I','J'),('J','G'),('J','K')]
conected_com = connected_components(test1)
print(conected_com)

test2 = [('A','B'),('B','E'),('B','F'),('E','A'),('E','F'),('F','G'),('G','F'),('B','C'),('C','G'),('C','D'),('D','C'),('D','H'),('H','D'),('H','G')]
conected_com = connected_components(test2)
print(conected_com)

test3 = [('A','D'),('D','A'),('E','D'),('E','I'),('G','H'),('H','G'),('H','E'),('B','E'),('B','C'),('C','F'),('F','B')]
conected_com = connected_components(test3)
print(conected_com)