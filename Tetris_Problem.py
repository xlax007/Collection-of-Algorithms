# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:11:18 2020

@author: alexi
"""


#http://codeforces.com/contest/1324/problem/A - Alexis Galvan


def check_equal(array):
    maximum = max(array)
    dic = {}
    dic[maximum] = 1
    for i in range(len(array)):
        if array[i] == 0:
            continue
        if array[i] not in dic:
            return False
    
    if maximum % 2 == 0:
        return True
    else:
        return False
        
def take_out(array):
    minimum = min(array)
    if minimum == 0:
        return array
    else:
        for i in range(len(array)):
            array[i] = array[i] - minimum
        return array

def check_odd(array):
    for i in range(len(array)):
        if array[i] % 2 != 0:
            return True
    
    return False

def tetris_problem():
    
    cases = int(input())
    length = []
    tetris = []
    for i in range(cases):
        length.append(int(input()))
        tetris.append(list(map(int, input().split())))
    
    for i in range(len(length)):
        if length == 1:
            print('YES')
            continue
        
        tetris[i] = take_out(tetris[i])
        
        if check_equal(tetris[i]):
            print("YES")
        else:
            if check_odd(tetris[i]):
                print("NO")
            else:
                print("YES")


tetris_problem()
        

        
    