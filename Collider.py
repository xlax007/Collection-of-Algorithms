# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:49:08 2020

@author: alexi
"""


#http://codeforces.com/problemset/problem/699/A -- Alexis Galvan

import math

def particles():
    total = int(input())
    particles = input()
    particles = [i for i in particles]
    position = list(map(int, input().split()))
    
    output = math.inf
    change = False
    
    for i in range(len(particles)):
        if particles[i] == 'R':
            if i+1 < len(particles):
                if particles[i+1] == 'L':
                    temp = int((position[i+1]-position[i])/2)
                    if temp < output:
                        output = temp
                        change = True
    
    if not change:
        return -1
    else:
        return output


answer = particles()
print(answer)
                
        
    