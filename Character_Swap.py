# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 23:49:13 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/1243/B1 --- Alexis Galvan


def check(string):
    if len(string[0]) == 2:
        if string[0][0] == string[1][0] and string[0][1] == string[1][1]:
            return True
        if string[0][0] == string[0][1] and string[1][0] == string[1][1]:
            return True
        return False
    
    counter = 0
    
    for i in range(len(string[0])):
        if string[0][i] != string[1][i]:
            counter += 1
            if counter == 3:
                return False
    return True
        
    

def character_swap():
    
    cases = int(input())
    length = []
    strings = []
    for i in range(cases):
        length.append(int(input()))
        strings.append([])
        strings[i].append(input())
        strings[i].append(input())
    
    for i in range(len(strings)):
        if len(strings[i][0]) != len(strings[i][1]):
            print('NO')
            continue
        if check(strings[i]):
            print('YES')
        else:
            print('NO')
    
    
character_swap()