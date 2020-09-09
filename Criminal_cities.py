# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:32:40 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/680/B

def criminal_city():
    cities = input().split()
    criminals = input().split()
    cities[1] = int(cities[1]) - 1
    cities.append(int(cities[1]))
    
    if cities[1] == 0:
        output = 0
        for i in range(len(criminals)):
            if int(criminals[i]) == 1:
                output += 1
        print(output)
        return
    else:
        output = 0
        left = right = True
        if int(criminals[cities[1]]) == 1:
            output += 1
        while left or right:
            detector = 0
            if (cities[1]-1) < 0:
                left = False
            else:
                if int((criminals[cities[1]-1])) == 1:
                    detector += 1
            if (cities[2]+1) >= len(criminals):
                right = False
            else:
                if int((criminals[cities[2]+1])) == 1:
                    detector += 1
            
            cities[1] -= 1
            cities[2] += 1
            
            if detector != 0:
                if detector == 2 and left and right:
                    output += 2
                elif detector == 1 and left and not right:
                    output += 1
                elif detector == 1 and not left and right:
                    output += 1
        print(output)
        return

criminal_city()
                    
                
                
        
                
        