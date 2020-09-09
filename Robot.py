# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 19:38:01 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/626/A --- Alexis Galvan


def check(string):
    start = [0, 0]
    copy = start.copy()
    
    for i in range(len(string)):
        if string[i] == 'U':
            copy[0] += 1
        elif string[i] == 'D':
            copy[0] -= 1
        elif string[i] == 'R':
            copy[1] += 1
        elif string[i] == 'L':
            copy[1] -= 1
    
    if copy == start:
        return True
    return False
    


def robot():
    length = int(input())
    string = input()
        
    output = 0
    for i in range(len(string)):
        j = 2
        while j != len(string)+1:
            if check(string[:j]):
                output += 1
            j += 1
        string = string[1:]
        
    
    return output

A = robot()
print(A)
            
            