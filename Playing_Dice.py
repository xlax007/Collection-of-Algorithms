# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:55:56 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/378/A


def dices():
    players_choice = input().split()
    
    player1 = draw = player2 = 0
    
    if players_choice[0] == players_choice[1]:
        print(0, 6, 0)
        return
    
    for i in range(1,7):
        if abs(i-int(players_choice[0])) < abs(i-int(players_choice[1])):
            player1 += 1
        elif abs(i-int(players_choice[0])) > abs(i-int(players_choice[1])):
            player2 += 1
        else:
            draw += 1
    
    print(player1, draw, player2)
    
dices()
            