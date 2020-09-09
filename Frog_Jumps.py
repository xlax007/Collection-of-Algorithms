# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:13:42 2020

@author: alexi
"""


#http://codeforces.com/contest/1324/problem/C -- Alexis Galvan


def check_l(string):
    output = 0
    con = 0
    for i in range(len(string)):
        if con > 0:
            con -= 1
            continue
        if string[i] == 'L':
            maximum = 1
            for j in range(i+1, len(string)):
                if string[j] == 'L':
                    maximum += 1
                    con += 1
                else:
                    break
            if maximum > output:
                output = maximum
    if output == 0:
        return output + 1
    return output + 1
            
        


def frog_jumps():
    
    cases = int(input())
    strings = []
    for i in range(cases):
        strings.append(input())
        
    for i in range(len(strings)):
        jump = check_l(strings[i])
        print(jump)
        

frog_jumps()