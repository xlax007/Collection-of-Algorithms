# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:15:27 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1077/B - Alexis Galvan

def disturbed_people():
    people = int(input())
    lights = input().split()
    
    counter = 0
    for i in range(1,len(lights)-1):
        if int(lights[i]) == 0:
            if int(lights[i-1]) == 1 and int(lights[i+1]) == 1:
                lights[i+1] = 0
                counter += 1
    
    print(counter)
    
disturbed_people()
                

                        