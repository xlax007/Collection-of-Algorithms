# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:06:22 2020

@author: alexi
"""



#Choose maximum number of events u can go based on a event-time line


def number_events(array):
    
    output = 0
    while len(array) > 0:
        minimum = array[0][2]
        index = 0
        for i in range(len(array)):
            if array[i][2] < minimum:
                minimum = array[i][2]
                index = i
                
        output += 1
        array.pop(index)
        
        if len(array) == 0:
            break
        
        pop = []
        for i in range(len(array)):
            if array[i][1] < minimum:
                pop.append(i)
        
        for i in range(len(pop)):
            array.pop(pop[-(i+1)])
    
    return output


array = [['A',1,3],['B',2,5],['C',3,5],['D',5,8]]
number_events(array)

   