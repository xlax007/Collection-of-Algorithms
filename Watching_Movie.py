# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:39:14 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/499/A --- Alexis Galvan


def watch_movie():
    
    buttons = list(map(int, input().split()))
    channels = []

    output = 0
    temp = buttons[1]
    for i in range(buttons[0]):
        channels.append(list(map(int, input().split())))
        output += ((channels[i][1]+1)-channels[i][0])
        channels[i][0] = channels[i][0]-(temp+1)
        channels[i][0] = (channels[i][0] % buttons[1])
        output += channels[i][0]
        temp = channels[i][1]
        
    return output

A = watch_movie()
print(A)

    
    
    
    
     
    
    