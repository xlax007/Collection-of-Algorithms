# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:06:50 2020

@author: Lenovo
"""



def even_odds():
    numbers = input().split()
    numbers = [int(i) for i in numbers]
    
    if numbers[1] == 1:
        print(1)
        return
    
    if numbers[0] % 2 == 0:
        if numbers[1] > (numbers[0]/2):
            numbers[1] = int(numbers[1] - numbers[0]/2)
            print(2 + (2*(numbers[1]-1)))
        else:
            print(1 + (2*(numbers[1]-1)))
    else:
        if numbers[1] > ((numbers[0]+1)/2):
            numbers[1] = int(numbers[1] - ((numbers[0]+1)/2))
            print(2 + (2*(numbers[1]-1)))
        else:
            print(1 + (2*(numbers[1]-1)))
            
        
    
even_odds()