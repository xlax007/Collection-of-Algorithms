# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:43:43 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/847/G --- Alexis Galvan


def university_classes():
    
    length = int(input())
    
    classes = []
    
    dic = {}
    classes.append(input())
    output = 0
    
    for i in range(len(classes[0])):
        if classes[0][i] == '1':
            dic[i] = 1
            if dic[i] > output:
                output = dic[i]
        else:
            dic[i] = 0
    
    for i in range(length-1):
        classes.append(input())
        
    for i in range(1, len(classes)):
        for j in range(len(classes[i])):
            if classes[i][j] == '1':
                dic[j] += 1
                if dic[j] > output:
                    output = dic[j]
    
    return output


A = university_classes()
print(A)
        
    
            
    
    
        