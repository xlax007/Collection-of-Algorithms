# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 02:30:46 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/234/B --- Alexis Galvan


def quick_sort(array):
    
    l = []
    e = []
    r = []
    
    if len(array) > 1:
        pivot = array[0][0]
        for x in range(len(array)):
            if array[x][0] < pivot:
                l.append(array[x])
            elif array[x][0] == pivot:
                e.append(array[x])
            else:
                r.append(array[x])
        return quick_sort(l) + e + quick_sort(r)
    else:
        return array

def reading_bus(stops, array):
    

    for i in range(len(array)):
        array[i] = (array[i], i+1)
    
    array = quick_sort(array)
    
    maximum = array[len(array)-stops[1]][0]
    output = ''

    for i in range(stops[1]):
        output = output + str(array[(-i)-1][1]) + ' '
    
    return maximum, output
    
stops = list(map(int, input().split()))
array = list(map(int, input().split()))
maximum, output = reading_bus(stops, array)
print(maximum)
print(output)
        
        