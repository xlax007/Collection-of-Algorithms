# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:42:39 2020

@author: alexi
"""



#Longest increasing sub_sequence --- Alexis Galvan


def longest_inc(array):
    
    long_array = [1 for i in range(len(array))]
   
    i = 0
    j = 1
    
    while True:
        if array[i] < array[j]:
            temp = long_array[i] + 1
            if temp > long_array[j]:
                long_array[j] = temp
                
        
        i += 1
        if i == len(array)-1 and j == len(array)-1:
            break
        elif i == j:
            j += 1
            if j == len(array) and i == len(array)-1:
                break
            i = 0
    
    return max(long_array)
            

array = [6,2,5,1,7,4,8,3]
A = longest_inc(array)
print(A)