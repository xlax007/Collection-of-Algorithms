# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 02:09:24 2020

@author: alexi
"""



#http://codeforces.com/problemset/problem/948/A --- Alexis Galvan

def check(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S':
                for new_position in [(0, 1),(0, -1),(1, 0),(1, 0)]:
                    
                    maze_position = (i+new_position[0], j+new_position[1])
                    
                    if maze_position[0] > len(matrix)-1 or maze_position[0] < 0 or maze_position[1] > len(matrix[i])-1 or maze_position[1] < 0:
                        continue
                    
                    if matrix[maze_position[0]][maze_position[1]] == 'W':
                        return False
    
    return True
                        
 
def add_dogs(matrix):
    for i in range(len(matrix)):
         matrix[i] = [matrix[i][j] for j in range(len(matrix[i]))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S':
                for new_position in [(0, 1),(0, -1),(-1, 0),(1, 0)]:
                    
                    maze_position = (i+new_position[0], j+new_position[1])
                    
                    if maze_position[0] > len(matrix)-1 or maze_position[0] < 0 or maze_position[1] > len(matrix[i])-1 or maze_position[1] < 0:
                        continue
                    
                    if matrix[maze_position[0]][maze_position[1]] == 'S':
                        continue
                    
                    matrix[maze_position[0]][maze_position[1]] = 'D'
    
    return matrix
                

def sheep_help():
    
    size = list(map(int, input().split()))
    
    maze = []
    
    for i in range(size[0]):
        maze.append(input())
    
    
    if check(maze):
        print('YES')
        maze = add_dogs(maze)
        for i in range(len(maze)):
            output = ''
            for j in range(len(maze[i])):
                output = output + str(maze[i][j]) 
            print(output)

    else:
        print ('NO')
        return

sheep_help()


    