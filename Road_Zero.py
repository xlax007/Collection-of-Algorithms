# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:49:13 2020

@author: alexi
"""



#http://codeforces.com/contest/1342/problem/A --- Alexis Galvan 


def road_zero():
    
    cases = int(input())
    numbers = []
    prices = []
    
    for i in range(cases):
        numbers.append(list(map(int, input().split())))
        prices.append(list(map(int, input().split())))
    
    for i in range(len(numbers)):
        if prices[i][0] == 0:
            print(0)
            continue
        
        output = 0
        minimum = min(abs(numbers[i][0]),abs(numbers[i][1]))
        best = min((minimum*prices[i][0])*2,minimum*prices[i][1])
        
        if abs(numbers[i][0]) == minimum:
            numbers[i][0] = 0
        else:
            numbers[i][0] -= minimum
            
        if abs(numbers[i][1]) == minimum:
            numbers[i][1] = 0
        else:
            numbers[i][1] -= minimum
        
        output += best
        
        if numbers[i][0] == 0 and numbers[i][1] == 0:
            print(output)
            continue
        
        maximum = max(numbers[i][0],numbers[i][1])
        output += (maximum*(prices[i][0]))
        
        print(output)
        
road_zero()
        