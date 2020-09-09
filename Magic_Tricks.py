# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:32:36 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1257/B

def magic_tricks():
    cases = int(input())
    numbers = []
    for i in range(cases):
        numbers.append(input().split())
    
    for i in range(len(numbers)):
        if int(numbers[i][0]) >= int(numbers[i][1]):
            print("YES")
        elif int(numbers[i][0]) == 2 and int(numbers[i][1]) == 3:
            print("YES")
        elif int(numbers[i][0]) < 4 and int(numbers[i][0]) < int(numbers[i][1]):
            print("NO")
        else:
            print("YES")
            

magic_tricks()
            
            
