# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:31:19 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1300/B


def merge_sort(array):
    if len(array) == 1:
        return array
    
    half = round(len(array)/2)
    
    arrayOne = [int(array[i]) for i in range(0, half)]
    arrayTwo = [int(array[i]) for i in range(half, len(array))]
    
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

def absolute(array1, array2):
 
    half = int(len(array1)/2)
    half2 = int(len(array2)/2)
    
    return abs(array1[half] - array2[half2])

def assign_classes():
    cases = int(input())
    number_students = []
    students = []
    for i in range(cases):
        number_students.append(int(input()))
        students.append(input().split())
    
    for i in range(len(number_students)):
        students[i] = merge_sort(students[i])
        arrayA = []
        arrayB = []
        temp = len(students[i]) / 2
        oneless = False
        if (temp % 2) == 0:
            oneless = True
            
        A = True
        B = False
        only = 0
        if oneless:
            only = int(temp - 1)
        for x in range(len(students[i])):
            if A:
                if x-1 == only:
                    arrayB.append(students[i][x])
                else:
                    arrayA.append(students[i][x])
                B = True
                A = False
            elif B:
                arrayB.append(students[i][x])
                A = True
                B = False
        
        print(absolute(arrayA,arrayB))
            
assign_classes()


