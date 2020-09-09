# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 04:51:28 2020

@author: alexi
"""



def lucky_year():
    year = int(input())
    
    if year < 10:
        return 1
    
    temp = str(year)
    
    lucky = ''

    lucky = lucky + str(int(temp[0])+1)
    for i in range(len(temp)-1):
        lucky = lucky + '0'
    
   
    return int(lucky) - year

    
    
            

A = lucky_year()
print(A)