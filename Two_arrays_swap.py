# -*- coding: utf-8 -*-
"""
Created on Fri May 15 03:51:39 2020

@author: alexi
"""



#http://codeforces.com/contest/1353/problem/B --- Alexis Galvan


def quick_sort(array):
    
    left = []
    equal = []
    right = []
    
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                right.append(x)
        
        return quick_sort(left) + equal + quick_sort(right)
    else:
        return array

def Two_arrays_swap():
    
    cases = int(input())
    
    k = []
    arrayA = []
    arrayB = []
    
    for i in range(cases):
        k.append(list(map(int, input().split())))
        arrayA.append(list(map(int, input().split())))
        arrayB.append(list(map(int, input().split())))
        arrayA[i] = quick_sort(arrayA[i])
        arrayB[i] = quick_sort(arrayB[i])
        
    for i in range(len(arrayA)):
        if arrayA[i][0] > arrayB[i][-1] or k[i][1] == 0:
            print(sum(arrayA[i]))
            continue
        
        done = False
        while not done:
            for j in range(len(arrayA[i])):
                if arrayA[i][j] > arrayB[i][(-j)-1]:
                    print(sum(arrayA[i]))
                    done = True
                    break
                arrayA[i][j] = arrayB[i][(-j)-1]
                k[i][1] -= 1
                if k[i][1] == 0:
                    print(sum(arrayA[i]))
                    done = True
                    break

Two_arrays_swap()
                
    
    