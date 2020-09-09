# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:07:31 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/507/A --- Alexis Galvan


def quick_sort(array):
    
    left = []
    equal = []
    right = []
    
    if len(array) > 1:
        pivot = array[0][1]
        for x in range(len(array)):
            if array[x][1] < pivot:
                left.append(array[x])
            elif array[x][1] == pivot:
                equal.append(array[x])
            elif array[x][1] > pivot:
                right.append(array[x])
        
        return quick_sort(left) + equal + quick_sort(right)
    else:
        return array
                
    

def learn_instruments():
    
    time = list(map(int, input().split()))
    instruments = list(map(int, input().split()))
    
    output = 0
    output_str = ''

    values = []
    for i in range(len(instruments)):
        values.append([i+1])
        values[i].append(instruments[i])
    
    values = quick_sort(values)
        
    
    for i in range(len(values)):
        if time[1] <= 0 or (time[1] - values[i][1]) < 0:
            break
        
        time[1] -= values[i][1]
        output += 1
        output_str = output_str + str(values[i][0]) + ' '
    
    if output == 0:
        print(output)
    else:
        print(output)
        print(output_str)
        
        
learn_instruments()

    
    
        
    
    
    