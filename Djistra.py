# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 21:10:04 2020

@author: Lenovo
"""

class Node():


    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.d = 0

    def __eq__(self, other):
        return self.position == other.position

        

def dijkstra(maze, start, end):

    start_node = Node(None, start)
    start_node.d = 0
    end_node = Node(None, end)
    end_node.d = 0

    priority = []
    checked = []

    priority.append(start_node)

    while True:
        
        visited = False
        
        if len(priority)  == 0:
            print('Error, No Route')
            break
        
        current_node = priority[0]
        current_index = 0
        for index, item in enumerate(priority):
            if item.d < current_node.d:
                current_node = item
                current_index = index
        priority.pop(current_index)
        checked.append(current_node)

        if current_node == end_node:
            path = []
            counter=0
            for i in checked:
                counter+=1
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] 
        else:
            
            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: 

                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue

                if maze[node_position[0]][node_position[1]] != 0:
                    continue
                
                new_node = Node(current_node, node_position)
                
                new_node.d = current_node.d + 1
                
                children.append(new_node)
                
            for child in children:
                for closed_child in checked:
                    if closed_child.position == child.position:
                        if child.d < closed_child.d:
                            closed_child.d = child.d
                        visited = True
                
                for open_node in priority:
                    if open_node.position == child.position:
                        if child.d < open_node.d:
                            open_node.d = child.d
                        visited = True
                    
                if visited:
                    visited = False
                    continue
                else:
                    priority.append(child)
                    
                


def main():


    maze = [[0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0]]
    
    
    start = (0, 0)
    end = (14, 14)
    
  
    
    path = dijkstra(maze, start, end)
    print('Una ruta buena que encontre es de',path)
    print(len(path))
   

    
main()     
                

