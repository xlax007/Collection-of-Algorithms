# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:56:29 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/1144/C --- Alexis Galvan


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


def shuffled_sequence():
    
    
    length = int(input())
    array = list(map(int, input().split()))
    array = merge_sort(array)
    
    dic = {}
    
    change = False
    for i in range(len(array)):
        if array[i] not in dic:
            dic[array[i]] = 1
        else:
            dic[array[i]] += 1
            change = True
            if dic[array[i]] == 3:
                print('NO')
                return
    
    if not change:
        print('YES')
        print(len(array))
        output = ''
        for i in range(len(array)):
            output = output + str(array[i]) + ' '
        print(output)
        print(0)
        print('')
    else:
        array_inc = []
        array_dec = []
        output_inc = ''
        output_dec = ''
        for i in dic:
            if dic[i] == 1:
                array_inc.append(i)
                output_inc = output_inc + str(i) + ' '
            else:
                array_inc.append(i)
                array_dec.append(i)
                output_inc = output_inc + str(i) + ' '
                output_dec = str(i) + ' ' + output_dec
        print('YES')
        print(len(array_inc))
        print(output_inc)
        print(len(array_dec))
        print(output_dec)
        
    
shuffled_sequence()
    
        