# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:36:18 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/706/B --- Alexis Galvan


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

def b_search(target, array):
    
    L = 0
    R = len(array)-1
    
    while L <= R:
        
        mid = L + (int((R-L)/2))
        
        if array[mid] <= target:
            L = mid + 1
        else:
            R = mid - 1
    
    if mid == 0:
        if target >= array[0]:
            return 1
        else:
            return 0
    
    if target >= array[mid]:
        return mid + 1
    else:
        return mid

def buy_drinks():
    
    n_shops = int(input())
    shops = list(map(int, input().split()))
    days = int(input())
    money = [int(input()) for i in range(days)]
    
    shops = merge_sort(shops)
    
    for i in range(len(money)):
        print(b_search(money[i], shops))

buy_drinks()