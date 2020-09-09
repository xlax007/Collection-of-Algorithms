# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:53:11 2020

@author: alexi
"""



#Let us now consider a problem where we are given n tasks with durations and
#deadlines and our task is to choose an order to perform the tasks. For each task,
#we earn d − x points where d is the task’s deadline and x is the moment when we
#finish the task. What is the largest possible total score we can obtain?


def quick_sort(array):
    
    left = []
    equal = []
    right = []
    
    if len(array) > 1:
        pivot = array[0][1]
        for x in range(len(array)):
            if array[x][1] < pivot:
                left.append(array[x])
            elif array[x][1] == pivot:
                equal.append(array[x])
            else:
                right.append(array[x])
        
        return quick_sort(left) + equal + quick_sort(right)
    else:
        return array
    

def total_score(array):
    
    array = quick_sort(array)
    output = 0
    time = 0
    
    for i in range(len(array)):
        time += array[i][1]
        output += (array[i][2]-time)

    return output        
    

array = [['A',4,2],['B',3,5],['C',2,7],['D',4,5]] #[1] = duration, [2] = deadline
total_score(array)