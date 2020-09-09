# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 03:36:55 2020

@author: alexi
"""




#http://codeforces.com/problemset/problem/1106/C -- Alexis Galvan


def quick_sort(array):
    
    less = []
    equal = []
    greater = []
    
    if len(array) > 1:
        pivot = int(array[0])
        for x in array:
            if int(x) < pivot:
                less.append(int(x))

            elif int(x) == pivot:
                equal.append(int(x))

            elif int(x) > pivot:
                greater.append(int(x))

        
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array

def sum_square(array, group):
    array = array.copy()
    if group == 3:
        sum_array = [[] for i in range(int(len(array)/3))]
    else:
        sum_array = [[] for i in range(int(len(array)/2))]
        
    output = 0

    for i in range(len(sum_array)):
        if group == 3:
            sum_array[i].append(array[0])
            array.pop(0)
            sum_array[i].append(array[-1])
            array.pop()
            sum_array[i].append(array[0])
            array.pop(0)
            output += (sum_array[i][0] + sum_array[i][1] + sum_array[i][2])**2
        elif group == 2:
            sum_array[i].append(array[0])
            array.pop(0)
            sum_array[i].append(array[-1])
            array.pop()
            output += (sum_array[i][0] + sum_array[i][1])**2
    
    return output
        
    
        
    

def number_division():
    length = int(input())
    numbers = input().split()
    numbers = quick_sort(numbers)
    
    if len(numbers) % 3 == 0:
        if sum_square(numbers,2) < sum_square(numbers, 3):
            print(sum_square(numbers, 2))
        else:
            print(sum_square(numbers, 3))
    else:
        print(sum_square(numbers, 2))

number_division()
        
    
    