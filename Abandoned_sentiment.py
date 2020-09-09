# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:39:31 2020

@author: alexi
"""


#http://codeforces.com/problemset/problem/814/A --- Alexis Galvan


def merge_sort(array):
    if len(array) == 1:
        return array
    
    half = round(len(array)/2)
    
    arrayOne = [array[i] for i in range(0, half)]
    arrayTwo = [array[i] for i in range(half, len(array))]
    
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

def check(array):
    for i in range(len(array)):
        if i+1 != len(array):
            if array[i] <= array[i+1]:
                continue
            return False
    return True

def check_a(array):
    copy = array.copy()
    while copy[0] != 0:
        copy.pop(0)
    if len(copy) == 0:
        return False
    else:
        temp = copy[0]
        
    for i in range(len(array)):
        if array[i] < temp:
            return True
        elif array[i] > temp:
            temp = array[i]
    return False
     
def check_equal_b(array):
    table = {array[0]:1}
    for i in range(1, len(array)):
        if array[i] not in table:
            return True
    return False
    

def abandoned_sentiment():
    ab = list(map(int, input().split()))
    a =  list(map(int, input().split()))
    b =  list(map(int, input().split()))
    
    if len(b) == 1:
        for i in range(len(a)):
            if a[i] == 0:
                a[i] = b[0]
                break
        if not check(a):
            return 'YES'
        return 'NO'
    
    if check_a(a):
        return 'YES'
    
    
    b = merge_sort(b)
    
    if check_equal_b(b):
        return 'YES'
    
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = b[0]
            b.pop(0)
    
    if not check(a):
        return 'YES'
    return 'NO'

A = abandoned_sentiment()
print(A)