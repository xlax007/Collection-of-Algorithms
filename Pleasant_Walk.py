# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:03:47 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/1090/M


def pleasant_walk():
    
    houses = input()
    array = list(map(int, input().split()))
    
    
    best_atm = 0
    best_sofar = 0
    
    for i in range(1,len(array)):
        if array[i] != array[i-1]:
            best_atm += 1
        else:
            if best_atm > best_sofar:
                best_sofar = best_atm
            best_atm = 0
    
    if best_atm > best_sofar:
        best_sofar = best_atm
    
    return best_sofar + 1

A = pleasant_walk()
print(A)
    