# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:29:00 2020

@author: alexi
"""



#Minimize or Maximize path of a grid (u can only move right/down) --- Alexis Galvan


def minCost(grid): 
  

    values_grid = [[0 for x in range(len(grid))] for x in range(len(grid[0]))] 
  
    values_grid[0][0] = grid[0][0] 
  
    for i in range(1, len(grid)): 
        values_grid[i][0] = values_grid[i-1][0] + grid[i][0] 
  
    for j in range(1, len(grid)): 
        values_grid[0][j] = values_grid[0][j-1] + grid[0][j] 
  
    for i in range(1, len(grid)): 
        for j in range(1, len(grid)): 
            values_grid[i][j] = max( values_grid[i-1][j], values_grid[i][j-1]) + grid[i][j]  ## change max for min in case of minimize instead of maximize
   
    print(values_grid)
    return values_grid[-1][-1] 
  
grid = [[3,7,9,2,7], 
        [9,8,3,5,5], 
        [1,7,9,8,5],
        [3,8,6,4,10],
        [6,3,9,7,8]] 

A = minCost(grid)
print(A)