# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:57:18 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1020/B

def hole_students():
    total = int(input())
    students = input().split()
    
    output = ''
    for i in range(len(students)):      
        dic = {}
        dic[i+1] = 1
        temp = int(students[i])
        while True:
            nex = int(students[temp-1])
            if temp not in dic:
                dic[temp] = 1
                temp = nex
            else:
                output += str(temp) + ' '
                break
                
    print(output)

            
hole_students()