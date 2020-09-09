# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:06:15 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/812/C     

#3 11
#2 3 5
#output
#2 11
#input
#4 100
#1 2 5 6
#output
#4 54
#input
#1 7
#7
#output
#0 0


def market():
    budget = input().split()  #2 Inputs, [0] = number of products, [1] = budget
    products = input().split()
    h = 0
    while True:
        cost = 0
        for i in range(len(products)-h):
            cost += (int(products[i]) + (int(budget[0])*(i+1)))
        if cost <= int(budget[1]):
            print(budget[0], cost)
            return
        h += 1
        budget[0] = int(budget[0]) - 1
        if budget[0] == 0:
            print(0, 0)
            return
        
market()
        
    