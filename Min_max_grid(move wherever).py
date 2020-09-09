# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 01:38:53 2020

@author: alexi
"""



##Minimize or Maximize path of a grid (u can where ever) --- Alexis Galvan


class Node():
    
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position
        self.cost = 0
    
    def __eq__(self, other):
        return self.position == other.position



def Astar_mincost(grid):
    
    start_node = Node(None, (0, 0))
    start_node.cost = grid[0][0]
    
    end_node = Node(None, (len(grid)-1,(len(grid[-1])-1)))
    end_node.cost = grid[-1][-1]
    
    open_list = []
    closed_list = []
    
    open_list.append(start_node)
    
    while True:
        
        current_node = open_list[0]
        current_index = 0
        
        for index, item in enumerate(open_list):
            if item.cost < current_node.cost:
                current_node = item
                current_index = index
        
        open_list.pop(current_index)
        closed_list.append(current_node)
        
        if current_node.position == end_node.position:
            path = []
            total = current_node.cost 
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return total, path[::-1]
        else:
            children = []
            
            for new_position in [(0, -1),(0, 1),(-1, 0),(1, 0)]:
                
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                
                if node_position[0] < 0 or node_position[0] > len(grid)-1 or node_position[1] < 0 or node_position[1] > len(grid[node_position[0]])-1:
                    continue
                
                new_node = Node(current_node, node_position)
                new_node.cost = current_node.cost + grid[node_position[0]][node_position[1]]
                
                children.append(new_node)
            
            visited = False
            for child in children:
                for open_child in open_list:
                    if child.position == open_child.position:
                        if child.cost < open_child.cost:
                            open_child = child
                        visited = True
                
                for closed_child in closed_list:
                    if child.position == closed_child.position:
                        if child.cost < closed_child.cost:
                            closed_child = child
                        visited = True
                
                if visited:
                    visited = False
                else:
                    open_list.append(child)
                        
    
grid = [[3,7,9,2,7], 
        [9,8,3,5,5], 
        [1,7,9,8,5],
        [3,8,6,4,10],
        [6,3,9,7,8]] 


A = Astar_mincost(grid)
print(A)