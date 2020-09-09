# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:45:07 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/792/A --- Alexis Galvan


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


def bus_route():
    
    cities = int(input())
    buses = list(map(int, input().split()))
    
    buses = merge_sort(buses)
    
    minimum = math.inf
    dic = {1:0}
    
    for i in range(1,len(buses)):
        if abs(buses[i])-(buses[i-1]) < minimum:
            minimum = abs(buses[i]-buses[i-1])
            dic[1] = 1
        elif abs(buses[i]-(buses[i-1])) == minimum:
            dic[1] += 1
    
    print(minimum, dic[1])

bus_route()
            
    
    
    
    
    
    
    
    