# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:39:11 2020

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

def find_target(array, target):
    half = (round(len(array)/2))-1
    dic = {}
    while True:
        if array[half] > target:
            half = round(half/2)
            dic[half] = 1
        elif array[half] < target:
            half = half + round((len(array) - half)/2)
            dic[half] = 1
        elif array[half] == target:
            break
        elif half in dic:
            return -1, -1
    
    while True:
        if half != 0:
            if array[half-1] == target:
                half -= 1
            else:
                break
        else:
            break
        
    for i in range(half, len(array)):
        if array[i] != target:
            output = [half, i-1]
            break
    
    
    return output
    

    
array = [1,3,3,5,7,8,9,9,9,15]

find_target(array, 7)


