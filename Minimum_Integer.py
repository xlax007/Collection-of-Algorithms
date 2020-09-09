# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 01:13:12 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/1101/A --- Alexis Galvan


def minimum_integer():
    
    cases = int(input())    
    integers = []
    
    for i in range(cases):
        integers.append(list(map(int, input().split())))
        
    for i in range(len(integers)):
        if integers[i][2] < integers[i][0] and integers[i][2] < integers[i][1]:
            print(integers[i][2])
            continue
        elif integers[i][2] > integers[i][0] and integers[i][2] > integers[i][1]:
            print(integers[i][2])
            continue
        
        temp = integers[i][2]
        
        L = 1
        R = integers[i][1]*2
        found = False
        while L <= R:
            mid = L + (int((R-L)/2))
            
            if int(temp*mid) > integers[i][1]:
                R = mid - 1
            elif int(temp*mid) < integers[i][1]:
                L = mid + 1
            elif int(temp*mid) == integers[i][1]:
                print(temp*(mid+1))
                found = True
                break
        
        if not found:
            if (temp*mid) < integers[i][1]:
                print(int(temp*(mid+1)))
            else:
                print(int(temp*mid))

minimum_integer()
        
        
                

            
        
        