# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:31:58 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/868/A --- Alexis Galvan


def bark_password():
    password = input()
    barks = int(input())
    posible = []
    for i in range(barks):
        posible.append(input())
        if posible[i] == password:
            return 'YES'
        elif posible[i][0] in password and posible[i][1] in password:
            if password[0] in posible[i] and password[1] in posible[i]:
                return 'YES'
    
    left = False
    right = False
    
    for i in range(len(posible)):
        if posible[i][0] == password[1]:
            left = True
        if posible[i][1] == password[0]:
            right = True
        
        if left and right:
            return 'YES'
    
    return 'NO'

A = bark_password()
print(A)
            
    
    