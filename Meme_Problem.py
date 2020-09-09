# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 00:31:47 2020

@author: alexi
"""



#https://codeforces.com/contest/1288/problem/B --- Alexis Galvan


def meme_problem():
    
    cases = int(input())
    numbers = []
    for i in range(cases):
        numbers.append(list(map(int, input().split())))
    
    for x in range(len(numbers)):
        b = []
        
        while True:
            length = len(str(numbers[x][1]))
            if ('9'*length) == numbers[x][1]:
                for i in range(length):
                    b.append(int(str(9)*i))
                break
            elif length == 1:
                if numbers[x][1] == 9:
                    b.append(9)
                break
            else:
                for i in range(1, length):
                    b.append(int('9'*i))
                break
        
        output = 0
        
        output = int(len(b)*numbers[x][0])
        #for i in range(1, numbers[x][0]+1):
        #    for j in range(len(b)):
        #        temp = (i*b[j])+(i+b[j])
        #        temp_str = int(str(i) + str(b[j]))
        #        
        #        if temp == temp_str:
        #            output += 1
                    
        print (output)
            

meme_problem()        
