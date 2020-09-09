# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:36:15 2020

@author: alexi
"""



#Two pointers in subarray sum --- Alexis Galvan


def subA_sum(array, target):
    
    pointL = 0
    pointR = 1
    
    if array[0] == target or array[1] == target or array[0] + array[1] == target:
        return True
    
    total = array[pointL] + array[pointR]
    
    while True:
        if pointR+1 == len(array):
            return False
        if total + array[pointR+1] > target:
            total -= array[pointL]
            pointL += 1
            if pointL == pointR:
                pointR += 1
                if pointR == len(array):
                    return False
        else:
            pointR += 1
            if pointR == len(array):
                return False
            
            total += array[pointR]
            if total == target:
                return True
    
    return False

array = [1,3,2,5,1,2,3]
A = subA_sum(array, 11)
print(A)         
    
    