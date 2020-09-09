# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:59:37 2020

@author: alexi
"""



#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/ --- Alexis Galvan


import math

def max_profit(array):
    
    
    best_without = 0
    best_with = -math.inf
    
    for i in range(len(array)):
        best_with = max(best_with, best_without - array[i])
        best_without = max(best_without, best_with + array[i])
    
    return best_without


array = [7,1,5,3,6,4]

max_profit(array)
    