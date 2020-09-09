# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:15:34 2020

@author: alexi
"""



#Biggest 1 square in matrix


def biggest_square(maze):
    alt_maze = []
    
    for i in range(len(maze)):
        alt_maze.append([])
    
    for j in range(len(maze[0])):
        alt_maze[0].append(maze[0][i])
    
    for i in range(1, len(maze)):
        alt_maze[i].append(maze[i][0])
    
    maximum = 0
    for i in range(1, len(maze)):
        for j in range(1, len(maze[i])):
            if maze[i][j] == 1 and maze[i-1][j] == 1 and maze[i][j-1] == 1 and maze[i-1][j-1] == 1:
                alt_maze[i].append(min(alt_maze[i-1][j],alt_maze[i][j-1],alt_maze[i-1][j-1])+1)
                if alt_maze[i][j] > maximum:
                    maximum = alt_maze[i][j]
            else:
                alt_maze[i].append(maze[i][j])
    print(alt_maze)
    return maximum
            

matrix = [[1,1,1,1,1],
        [1,1,1,0,0],
        [1,1,1,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0]]

biggest_square(matrix)