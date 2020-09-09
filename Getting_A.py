# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 01:02:56 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/991/B --- Alexis Galvan


def merge_sort(array):
    
    if len(array) == 1:
        return array
    
    arrayOne = [array[i] for i in range(0, int(len(array)/2))]
    arrayTwo = [array[i] for i in range(int(len(array)/2),len(array))]
    
    arrayOne = merge_sort(arrayOne)
    arrayTwo = merge_sort(arrayTwo)
    
    return merge(arrayOne, arrayTwo)

def merge(arrayA, arrayB):
    output = []
    while len(arrayA) > 0 and len(arrayB) > 0:
        if arrayA[0] > arrayB[0]:
            output.append(arrayB[0])
            arrayB.pop(0)
        else:
            output.append(arrayA[0])
            arrayA.pop(0)
    
    while len(arrayA) > 0:
        output.append(arrayA[0])
        arrayA.pop(0)
    
    while len(arrayB) > 0:
        output.append(arrayB[0])
        arrayB.pop(0)
    
    return output


def correct_grades():
    
   length = int(input())
   grades = list(map(int, input().split()))
   
   up = 4.5
   
   temp = sum(grades)/length
   
   if temp >= up:
       return 0
   
   output = 0
    
   grades = merge_sort(grades)
   
   for i in range(len(grades)):
       output += 1
       grades[i] = 5
       temp = sum(grades)/length
       if temp >= up:
           return output
       
A = correct_grades()
print(A)