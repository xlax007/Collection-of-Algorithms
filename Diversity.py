# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 00:58:51 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/844/A --- Alexis Galvan


def check(string):
    output = 0
    dic = {}
    for i in range(len(string)):
        if string[i] not in dic:
            dic[string[i]] = 1
        else:
            output += 1
    return output

def diversity():
    
    string = input()
    length = int(input())
    
    if length > len(string):
        return 'impossible'
    
    temp = check(string)
    non_repeat = len(string) - temp
    if non_repeat >= length:
        return 0
    return length - non_repeat
    

A = diversity()
print(A)
    
    