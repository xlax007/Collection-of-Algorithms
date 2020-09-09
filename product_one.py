# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:39:32 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1206/B

def check_positive(array):
    temp = 1
    for i in array:
        if i != 0:
            temp *= i
    
    if temp > 0:
        return True
    else:
        return False


def product_one():
    
    total = int(input())
    
    coins = input().split()
    
    coins = [int(i) for i in coins]
    
    counter = 0
    
    for i in range(len(coins)):
        if coins[i] == 0:
            if check_positive(coins):
                counter += 1
                coins[i] += 1
            else:
                counter += 1
                coins[i] -= 1
        elif coins[i] > 1:
            counter += (coins[i] - 1)
            coins[i] -= (coins[i] - 1)
        elif coins[i] < -1:
            counter += (-(coins[i]) - 1)
            coins[i] += (-(coins[i])- 1)
    
    if check_positive(coins):
        print(counter)
        return
    else:
        print(counter+2)
        return

product_one()