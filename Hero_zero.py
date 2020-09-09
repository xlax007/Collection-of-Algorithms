# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:20:17 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1175/A

def hero_zero():
    cases = int(input())
    numbers = []
    for i in range(cases):
        numbers.append(input().split())
        numbers[i][0] = int(numbers[i][0])
        numbers[i][1] = int(numbers[i][1])
    
    for i in range(len(numbers)):
        if numbers[i][0] < numbers[i][1] or numbers[i][1] == 1:
            print(numbers[i][0])
            continue
        steps = 0
        while True:
            if (numbers[i][0] % numbers[i][1]) == 0:
                numbers[i][0] = int(numbers[i][0] / numbers[i][1])
                steps += 1
                if numbers[i][0] < 1:
                    print(steps)
                    break
            else:
                temp = numbers[i][0] % numbers[i][1]
                steps += temp
                numbers[i][0] -= temp
                if numbers[i][0] < 1:
                    print(steps)
                    break
            

hero_zero()