# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:54:40 2020

@author: Lenovo
"""


#https://codeforces.com/contest/1312/problem/B

def quicksort(array):
    
    left = []
    equal = []
    right = []
    
    if len(array) > 1:
        pivot = int(array[0])
        for x in array:
            if int(x) < pivot:
                left.append(int(x))
            elif int(x) == pivot:
                equal.append(int(x))
            elif int(x) > pivot:
                right.append(int(x))
        
        return quicksort(left) + equal + quicksort(right)
    
    else:
        return array
        

def pair_array():
    cases = int(input())
    length = []
    arrays = []
    for i in range(cases):
        length.append(int(input()))
        arrays.append(input().split())
        
    for i in range(len(arrays)):
        if len(arrays[i]) == 1:
            print(int(arrays[i][0]))
        else:
            arrays[i] = quicksort(arrays[i])
            half = int(len(arrays[i])/2)
            output = str(arrays[i][0])
            j = 2
            while half > 0:
                if j >= len(arrays[i]):
                    break
                output += ' ' + str(arrays[i][j])
                half -= 1
                j += 2

            half = int(len(arrays[i])/2)
            j = 1
            while half > 0:
                output += ' ' + str(arrays[i][j])
                half -= 1
                j += 2
                if j >= len(arrays[i]):
                    break
            
            print(output)

            
                
pair_array()
            
        