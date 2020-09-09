# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 23:55:19 2020

@author: alexi
"""



def binary_search(array, target):
    L = 0
    R = len(array)-1
    
    while L <= R:
        mid = L + int((R-L)/2)
        
        if array[mid] == target:
            return (target,'at position:',mid)
        
        if array[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    
    return -1



array = [0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,5,5,5,5,5,5,6,6,6,6,7,7,7,8,8,8,8,9,9,9,9,10,10,1512]

binary_search(array, 0)


#binary search, find a target that is >= than target

def binary_search_2(array, target):
    L = 0
    R = len(array)-1
    
    ans = -1
    while L <= R:
        mid = L + int(((R-L)/2))
        
        if array[mid] == target:
            return array[mid], mid
        elif array[mid] >= target:
            ans = mid
            R = mid - 1
        else:
            L = mid + 1
    
    return array[ans], ans


array2 = [1,2,3,4,5,7,8,9,10,11,12,13,14,15,19]

binary_search_2(array2, 20)


#binary search, find maximum in a increasing-decreasing array

def binary_search_3(array):
    L = 0
    R = len(array)-1
    
    ans = -1
    while L <= R:
        mid = L + int((R-L)/2)
        if mid == 0:
            if array[mid] > ans:
                ans = array[mid]
            L = mid+1
            
        elif (mid-1) >=0:
            if array[mid] > array[mid-1]:
                ans = array[mid]
                L = mid+1
            else:
                R = mid -1
                
    return ans



array =[1,2,3,4,5,6,7,8,4,3,2,1]
binary_search_3(array)
                
        