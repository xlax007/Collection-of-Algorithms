# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:29:55 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/405/A

def gravity_boxes():
    total = int(input())
    
    boxes = input().split()
       
    while True:
        change = False
        for i in range(1,len(boxes)):
            if int(boxes[i]) < int(boxes[i-1]):
                temp = int(boxes[i-1]) - int(boxes[i])
                boxes[i] = int(boxes[i]) + temp
                boxes[i-1] = int(boxes[i-1]) - temp
                change = True
        if not change:
            break
    
    output = ''
    output = output + str(boxes[0])
    for i in range(1,len(boxes)):
        output = output + ' ' + str(boxes[i])
    
    print(output)
     
     
               
gravity_boxes()