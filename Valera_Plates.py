# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:48:43 2020

@author: alexi
"""



#http://codeforces.com/problemset/problem/369/A --- Alexis Galvan

def valera_plates():
    
    days = list(map(int, input().split()))
    dishes = list(map(int, input().split()))
    
    output = 0
    
    for i in range(len(dishes)):
        if days[1] == 0 and days[2] == 0:
            output += len(dishes)-i
            break
        
        if dishes[i] == 1:
            if days[1] > 0:
                days[1] -= 1
            else:
                output += 1
        elif dishes[i] == 2:
            if days[2] > 0:
                days[2] -= 1
            elif days[1] > 0:
                days[1] -= 1
            else:
                output += 1
    
    return output


A = valera_plates()
print(A)