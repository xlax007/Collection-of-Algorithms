# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:02:21 2020

@author: alexi
"""



#Contest 1343 Codeforces


def candies():
    
    cases = int(input())
    
    candies = [int(input()) for i in range(cases)]
    
    for i in range(len(candies)):
        if candies[i] % 3 == 0:
            print(int(candies[i]/3))
        elif candies[i] % 7 == 0:
            print(int(candies[i]/7))
        else:
            divisor = 5
            while True:
                if candies[i] % divisor == 0:
                    if divisor % 2 != 0:
                        print(int(candies[i]/divisor))
                        break
                divisor += 1
                    
candies()
        
        