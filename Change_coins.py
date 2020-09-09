# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:53:55 2020

@author: Lenovo
"""


#change for shop

def num_coins(number):
    if number < 1:
        return 0
    coins = [25,10,5,1]
    output = 0
    for i in range(len(coins)):
        temp = int(number/coins[i])
        output += temp
        number -= (coins[i] * temp)
        if number == 0:
            return output


num_coins(19)

