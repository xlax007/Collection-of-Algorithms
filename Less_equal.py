# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:34:41 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/977/C --- Alexis Galvan


import math

def merge_sort(array):
    if len(array) == 1:
        return array
    
    arrayOne = [array[i] for i in range(0, int(len(array)/2))]
    arrayTwo = [array[i] for i in range(int(len(array)/2), len(array))]
    
    arrayOne = merge_sort(arrayOne)
    arrayTwo = merge_sort(arrayTwo)
    
    return merge(arrayOne, arrayTwo)

def merge(arrayA, arrayB):
    output = []
    while len(arrayA) > 0 and len(arrayB) > 0:
        if arrayA[0] < arrayB[0]:
            output.append(arrayA[0])
            arrayA.pop(0)
        else:
            output.append(arrayB[0])
            arrayB.pop(0)
    
    while len(arrayA) > 0:
        output.append(arrayA[0])
        arrayA.pop(0)
    
    while len(arrayB) > 0:
        output.append(arrayB[0])
        arrayB.pop(0)
    
    return output
    


def less_equal():
    
    length = list(map(int, input().split()))
    array = list(map(int, input().split()))
    
    if length[1] == 0:
        minimum = math.inf
        for i in range(len(array)):
            if array[i] < minimum:
                minimum = array[i]
        if minimum == 1:
            return -1
        else:
            return 1
    
    array = merge_sort(array)
    
    if len(array) == 1:
        return array[0]
    else:
        temp = array[length[1]-1]
        if array[length[1]] <= temp:
            return -1
        else:
            return temp
            

print(less_equal())