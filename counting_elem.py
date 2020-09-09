# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:21:15 2020

@author: alexi
"""



#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/ --- Alexis Galvan


def counting_elem(array):
    
    table = {}
    
    for i in range(len(array)):
        table[array[i]] = 1
    
    output = 0
    for i in range(len(array)):
        if array[i]+1 in table:
            output +=1
            
    return output
            

array = [1,2,3]
counting_elem(array)
    
    