# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:56:46 2020

@author: alexi
"""



#Minimizing the sum with this formula - |a1 − x|c +|a2 − x|c +··· +|an − x


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

def solve(array):
    
    array = merge_sort(array)
    
    if len(array) % 2 == 0:
        temp = (array[int(len(array)/2)]+array[int(len(array)/2)+1])/2 
        output = 0
        for i in range(len(array)):
            output += abs(array[i]-temp)
        return output
    else:
        temp = array[int(len(array)/2)]
        output = 0
        for i in range(len(array)):
            output += abs(array[i]-temp)
        return output
    

array = list(map(int, input().split()))
A = solve(array)
print(A)