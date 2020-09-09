# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:13:32 2020

@author: alexi
"""



#https://codeforces.com/contest/1334/problem/A --- Alexis Galvan


def level_statistics():
    
    cases = int(input())
    level_stats = []
    clears = []
    
    for i in range(cases):
        level_stats.append(int(input()))
        for j in range(level_stats[i]):
            clears.append(list(map(int, input().split())))
            
    
    for i in range(len(level_stats)):
        players = clears[0][0]
        completed = clears[0][1]
        clears.pop(0)
        if level_stats[i] == 1:
            if players >= completed:
                print('YES')
            else:
                print('NO')
            continue
        if completed > players or players < 0 or completed < 0:
            print('NO')
            for j in range(level_stats[i]-1):
                clears.pop(0)
            continue
        
        found = True
        
        for j in range(level_stats[i]-1):
            temp_players = clears[0][0]
            temp_completed = clears[0][1]
            clears.pop(0)
            if found:
                if temp_players < players or temp_completed < completed:
                    print('NO')
                    found = False
                    continue
                if temp_players == players and temp_completed != completed:
                    print('NO')
                    found = False
                    continue
                if temp_completed > completed:
                    more = temp_completed - completed
                    if (players+more) > temp_players:
                        print('NO')
                        found = False
                        continue
                players = temp_players
                completed = temp_completed
                if completed > players:
                    print('NO')
                    found = False
        
        if found:
            print('YES')


level_statistics()
            
            
            
            
    
    
