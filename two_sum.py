# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 00:52:59 2020

@author: alexi
"""



#https://leetcode.com/problems/two-sum/ --- Alexis Galvan


def two_sum():
    
    lista = list(map(int, input().split()))
    target = int(input())
    
    dic = {}
    dic[lista[0]] = 0
    
    for i in range(1, len(lista)):
        temp = target - lista[i]
        if temp in dic:
            return [i, dic[temp]]
        else:
            dic[lista[i]] = i
    
    return -1

A = two_sum()
print(A)



    
    