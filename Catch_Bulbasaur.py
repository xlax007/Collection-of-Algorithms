# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:45:58 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/757/A --- Alexis Galvan


def bulbasaur():
    
    dic = {'B':0,'u':0,'l':0,'b':0,'a':0,'s':0,'u':0,'r':0}
    
    word = input()
    
    for i in range(len(word)):
        if word[i] in dic:
            dic[word[i]] += 1
    
    dic['a'] = int(dic['a']/2)
    
    minimum = dic['B']
    
    for i in dic:
        if dic[i] < minimum:
            minimum = dic[i]
    
    return minimum

A = bulbasaur()
print(A)
    