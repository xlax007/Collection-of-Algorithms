# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:12:40 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1206/A

def two_numbers():
    
    length1 = input()
    arrayA = input().split()
    length2 = input()
    arrayB = input().split()
    
    dic = {}
       
    for i in range(len(arrayA)):
        dic[int(arrayA[i])] = 1
        
    for j in range(len(arrayB)):
        if int(arrayB[j]) not in dic:
            dic[int(arrayB[j])] = 1
    
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            temp = int(arrayA[i]) + int(arrayB[j])
            if temp not in dic:
                print(int(arrayA[i]),int(arrayB[j]))
                return
        
    print('NO')
    return

two_numbers()