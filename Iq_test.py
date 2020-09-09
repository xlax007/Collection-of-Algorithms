# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:25:40 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/287/A --- Alexis Galvan


def iq_test():
    
    maze = []
    
    for i in range(4):
        maze.append(input())
    
    for i in range(len(maze)-1):
        for j in range(len(maze[i])-1):
            dic = {'#':0,'.':0}
            dic[maze[i][j]] += 1
            dic[maze[i+1][j]] += 1
            dic[maze[i+1][j+1]] += 1
            dic[maze[i][j+1]] += 1
            
            if dic['#'] >= 3:
                return 'YES'
            elif dic['.'] >= 3:
                return 'YES'
    
    return 'NO'

print(iq_test())
            