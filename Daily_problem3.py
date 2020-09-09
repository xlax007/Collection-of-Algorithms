# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:22:42 2020

@author: Lenovo
"""

#Given a sorted array, A, with possibly duplicated elements, find the indices of the 
#first and last occurrences of a target element, x. Return -1 if the target is not found.

#Example:
#Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
#Output: [6,8]

#Input: A = [100, 150, 150, 153], target = 150
#Output: [1,2]

#Input: A = [1,2,3,4,5,6,10], target = 9
#Output: [-1, -1]


def most_duplicate(array):
    duplicates = 1
    maximum = 1
    indices = [0, 0]
    for i in range(1,len(array)):
        if array[i] == array[i-1]:
            duplicates += 1
            if i != len(array):
                if array[i] != array[i+1]:
                    if duplicates > maximum:
                        maximum = duplicates
                        indices[1] = i
                        indices[0] = i- maximum +1
        else:
            duplicates = 1
    
    if indices[0] == 0 and indices[1] == 0:
        return -1
    else:
        return indices
    

array = [1,2,3,4,5,6,10]

most_duplicate(array)


