# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:48:38 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/214/A

def pair_equation():
    numbers = input().split()
    numbers = [int(i) for i in numbers]
    
    minimum = min(numbers[0],numbers[1])
    
    check = [0,0]
    output = 0
    for i in range(minimum):
        check[0] += 1
        check[1] = 0
        for i in range(minimum):
            if ((check[0])**2 + check[1]) == numbers[0] and (check[0] + (check[1])**2) == numbers[1]:
                output += 1
            check[1] += 1
    
    if numbers[0] == numbers[1] and numbers[0] == 1:
        print(output*2)
        return
    elif numbers[0] == numbers[1] and numbers[0] == 2:
        print(output)
        return
    print(output)
    return

pair_equation()



    
    
        
            
        
        
        
        