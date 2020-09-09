# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:39:31 2020

@author: alexi
"""


#http://codeforces.com/problemset/problem/1117/B --- Alexis Galvan


def emotes():
    emotes = list(map(int, input().split()))
    values = list(map(int, input().split()))
    
    maximum = max(values)
    table = {maximum:0}
    index = 0
    for i in range(len(values)):
        if values[i] in table:
            table[values[i]] += 1
            index = i
            if table[values[i]] == 2:
                return maximum * emotes[1]
    
    values.pop(index)
    maximum_2 = max(values)
    
    temp = int(emotes[1]/(emotes[2]+1))
    
    first = (temp*(maximum*emotes[2]))
    second = (temp*(maximum_2))
    output = first + second
    
    emotes[1] = emotes[1] - (temp*(emotes[2]+1))
    
    if emotes[1] > 0:
        output += (emotes[1] * maximum)
    
    return output


A = emotes()
print(A)
            
        
    