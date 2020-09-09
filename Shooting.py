# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 20:54:40 2020

@author: alexi
"""

#http://codeforces.com/problemset/problem/1216/B - Alexis Galvan



def shooting():
    total = int(input())
    cans = input().split()
    
    checker = [False for i in range(len(cans))]
    
    output = 0
    output2 = ''
    
    for i in range(len(cans)):
        maximum = 0
        position = 0
        for j in range(len(cans)):
            if not checker[j]:
                if int(cans[j]) > maximum:
                    maximum = int(cans[j])
                    position = j
                    
        checker[position] = True
        output += (maximum*(i))+1
        output2 += str(position+1) + ' '
    
    print(output)
    print(output2)
    

shooting()
        
                
