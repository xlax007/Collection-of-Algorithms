# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:34:19 2020

@author: alexi
"""


#http://codeforces.com/problemset/problem/549/A --- Alexis Galvan


def face_detection():
    size = list(map(int, input().split()))
    
    if size[0] == 1:
        return 0
    
    maze = []
    dic = {'f':1,'a':2,'c':3,'e':4}
    
    
    for i in range(size[0]):
        maze.append(input())
        
    output = 0
    for i in range(1, len(maze)):
        for j in range(1, len(maze[i])):
            if maze[i][j] in dic:
                alt_dic = dic.copy()
                alt_dic.pop(maze[i][j])
                if maze[i-1][j-1] in alt_dic:
                    alt_dic.pop(maze[i-1][j-1])
                    if maze[i-1][j] in alt_dic:
                        alt_dic.pop(maze[i-1][j])
                        if maze[i][j-1] in alt_dic:
                            output += 1
    
    return output


A = face_detection()
print(A)
                            
            
        
    