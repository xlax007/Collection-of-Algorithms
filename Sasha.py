# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:40:18 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/832/A 


def sasha_game():
    sticks = input().split() #[0] = all sticks left, [1] = sticks allowed for each turn, sasha vs someone else
    
    sticks = [int(i) for i in sticks]

    temp = int(sticks[0] / sticks[1])
    
    if temp % 2 == 0:
        print("NO")
        return 
    else:
        print("YES")
        return 

sasha_game()

