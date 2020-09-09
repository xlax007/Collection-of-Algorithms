# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:20:32 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/152/A --- Alexis Galvan


def students():
    
    students = list(map(int, input().split()))
    grades = [] 
    for i in range(students[0]):
        grades.append(input())
    
    checked = [False for i in range(students[0])]
    
    output = 0
    
    while len(grades[0]) > 0:
        maximum = int(grades[0][0])
        for i in range(len(grades)):
            if int(grades[i][0]) > maximum:
                maximum = int(grades[i][0])
        
        for i in range(len(grades)):
            if int(grades[i][0]) == maximum and not checked[i]:
                checked[i] = True
                output += 1
                if output == students[0]:
                    return output
            grades[i] = grades[i][1:]
    
    return output

A = students()
print(A)


            
        
        
