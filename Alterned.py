# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:45:37 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1144/B - Alexis Galvan

def get_even(array):
    maximum = 0
    position = 0
    counter_even = 0
    counter_odd = 0
    for i in range(len(array)):
        if int(array[i]) % 2 == 0:
            counter_even += 1
        else:
            counter_odd += 1
        if int(array[i]) > maximum:
            maximum = int(array[i])
            position = i
    
    return counter_even, counter_odd, position

def add_array(array):
    output = 0
    for i in range(len(array)):
        output += int(array[i])
    
    return output

def delete(array, even, odd):
    while True:
        change = False
        i = 0
        while i < len(array):
            if even:
                if int(array[i]) % 2 == 0:
                    array.pop(i)
                    even = False
                    odd = True
                    change = True
                else:
                    i += 1
            elif odd:
                if int(array[i]) % 2 != 0:
                    array.pop(i)
                    even = True
                    odd = False
                    change = True
                else:
                    i += 1
                    
        if not change:
            break
    
    print(add_array(array))   
    
    
def alterned():
    length = int(input())
    array = input().split()
    even_odd = get_even(array)
    if even_odd[0] > even_odd[1]:
        even = True
        odd = False
        delete(array, even, odd)
    elif even_odd[0] == even_odd[1]:
        if int(array[even_odd[2]]) % 2 == 0:
            array.pop(even_odd[2])
            odd = True
            even = False
        else:
            array.pop(even_odd[2])
            odd = False
            even = True
        
        delete(array, even, odd)
        
    else:
        odd = True
        even = False
        delete(array, even, odd)


alterned()                
                        
                
            