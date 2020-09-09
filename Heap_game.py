# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:34:25 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/119/A

def heap_game():
    players = input().split()
    players = [int(i) for i in players]
    i = 0
    while True:
        temp = int(players[2] / players[i])
        if temp >= players[i]:
            players[2] -= temp

        else:
            if i == 0:
                print(1)
                return
            else:
                print(0)
                return
        i += 1
        if i == 2:
            i = 0

            

heap_game()