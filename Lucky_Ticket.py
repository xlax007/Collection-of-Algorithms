# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:03:13 2020

@author: alexi
"""



#http://codeforces.com/problemset/problem/146/A -- Alexis Galvan



def check_half_sum(array):
    half = int(len(array)/2)
    sum1 = 0
    sum2 = 0
    for i in range(0, half):
        sum1 += int(array[i])
    
    for i in range(half, len(array)):
        sum2 += int(array[i])
    
    if sum1 == sum2:
        return True
    return False
        

def check(array):
    dic = {'4','7'}
    for i in range(len(array)):
        if array[i] not in dic:
            return False
    return True

def lucky_ticket():
    length = int(input())
    ticket = input()
    
    if not check(ticket):
        return 'NO'
    
    if check_half_sum(ticket):
        return 'YES'
    else:
        return 'NO'
    

answer = lucky_ticket()
print(answer)