# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:50:02 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/981/A --- Alexis Galvan


def check(string):
    L = 0
    R = len(string)-1
    
    while L <= R:
        if string[L] == string[R]:
            L += 1
            R -= 1
        else:
            return False
    
    return True

def check_equal(string):
    dic = {}
    for i in range(len(string)):
        if string[i] not in dic:
            dic[string[i]] = 1
            if len(dic) == 2:
                return False
    return True

def antipalindrome():
    
    word = input()
    
    if not check(word):
        return len(word)
    else:
        if check_equal(word):
            return 0
        
        i = 1
        maximum = 0
        while True:
            temp = word[i:]
            if not check(temp):
                length = len(temp)
                if length > maximum:
                    maximum = length
            i += 1
            if i == len(word):
                break
        
        i = 1
        while True:
            temp = word[:i]
            if not check(temp):
                length = len(temp)
                if length > maximum:
                    maximum = length
            i += 1
            if i == len(word):
                break
        
        return maximum

A = antipalindrome()
print(A)