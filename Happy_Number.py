# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:29:35 2020

@author: alexi
"""



#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/ --- Alexis Galvan


def ishappy(number, dic):
    temp = str(number)
    dic[number] = 1
    array = []
    
    add = 0
    for i in range(len(temp)):
        array.append(temp[i])
        add += int(array[i])**2
    
    if add == 1:
        return True
    elif add in dic:
        return False
    
    return ishappy(add, dic)
    
A = ishappy(19, {})
print(A)
    
    
    