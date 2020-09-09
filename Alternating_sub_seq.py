# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:26:35 2020

@author: alexi
"""



#https://codeforces.com/contest/1343/problem/C --- Alternating sequence


def alternating():
    
    cases = int(input())
    length = []
    array = []
    
    for i in range(cases):
        length.append(int(input()))
        array.append(list(map(int, input().split())))
    
    
    for i in range(len(array)):
        maximum = array[i][0]
        output = 0
        if array[i][0] < 0:
            positive = False
        else:
            positive = True
            
        for j in range(len(array[i])):
            if positive:
                if array[i][j] < 0:
                    positive = False
                    output += maximum
                    maximum = array[i][j]
                else:
                    if array[i][j] > maximum:
                        maximum = array[i][j]
            else:
                if array[i][j] > 0:
                    positive = True
                    output += maximum
                    maximum = array[i][j]
                else:
                    if array[i][j] > maximum:
                        maximum = array[i][j]
                        
        output += maximum
        print(output)
        
alternating()

