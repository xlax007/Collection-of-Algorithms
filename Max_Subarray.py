# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:25:44 2020

@author: alexi
"""



#Max subarray --- Alexis Galvan


def max_subarray(array):
    max_atm = array[0]
    
    max_array = 0
    
    for i in range(len(array)):
        max_array = max_array + array[i]
        if max_array < 0:
            max_array = 0
        elif max_array > max_atm:
            max_atm = max_array
    
    return max_atm

array = [-2,1,-2,-8,2,-2,-2,4,-2,-1,5,1]

max_subarray(array)

