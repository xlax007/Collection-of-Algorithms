# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:39:30 2020

@author: alexi
"""



#http://codeforces.com/problemset/problem/990/A --- Alexis Galvan 

def sell_boxes(boxes):
    temp = boxes[0] * boxes[3]
    return temp

def buy_boxes(boxes):
    temp = boxes[1] - boxes[0]
    temp = temp * boxes[2]
    return temp
    

def sell(boxes):
    mult = int(boxes[0]/boxes[1])
    if mult == 0:
        mult = 1
    temp = boxes[1] * mult
    
    return (boxes[0] - temp) * boxes[3]


def buy(boxes):
    mult = int(boxes[0]/boxes[1]) + 1
    if mult == 0:
        mult = 1
        
    boxes[1] = boxes[1] * mult
    return (boxes[1]-boxes[0]) * boxes[2]



def boxes():
    boxes = list(map(int, input().split()))
    
    if boxes[0] % boxes[1] == 0:
        return 0
    
    if boxes[0] < boxes[1]:
        temp_sell = sell_boxes(boxes)
        temp_buy = buy_boxes(boxes)
        if temp_sell < temp_buy:
            return int(temp_sell)
        return int(temp_buy)
    elif boxes[0] > boxes[1]:
        temp_sell = sell(boxes)
        temp_buy = buy(boxes)
        if temp_sell < temp_buy:
            return int(temp_sell)
        return int(temp_buy)

A = boxes()
print(A)