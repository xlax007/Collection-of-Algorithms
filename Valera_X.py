# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 19:27:04 2020

@author: alexi
"""



#http://codeforces.com/problemset/problem/404/A?fbclid=IwAR22tveq4f5Ty30Y7uPrDjlZ1WfDL9JIOPjfyTSmilAynkQsiiEiwMw1PFU


def valera_x():
    rows = int(input())
    maze = []
    for i in range(rows):
        maze.append(input())
        maze[i] = [maze[i][j] for j in range(len(maze[i]))]
        
    L = 0
    R = len(maze)-1
    row = 0
    down_row = -1
    
    dic = {}
    dic[maze[0][0]] = 1
    while True:
        if maze[row][L] in dic and maze[row][R] in dic and maze[down_row][L] in dic and maze[down_row][R] in dic:
            maze[row].pop(R)
            maze[row].pop(L)
            maze[down_row].pop(R)
            maze[down_row].pop(L)
            L += 1
            R -= 1
            row += 1
            down_row -= 1
            if L == R:
                if maze[row][L] in dic:
                    maze[row].pop(L)
                    break
        else:
            return 'NO'
    
    if maze[0][0] in dic:
        return'NO'
    dic = {}
    dic[maze[0][0]] = 1
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] not in dic:
                return 'NO'
    
    return 'YES'


answer = valera_x()
print(answer)
            
        
            
        
    
    
    
    