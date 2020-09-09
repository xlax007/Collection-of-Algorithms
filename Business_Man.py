# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:33:10 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/981/B


def business_men():
    
    teamA = int(input())
    teamA_days = []
    teamA_dic = {}
    
    for i in range(teamA):
        teamA_days.append(list(map(int, input().split())))
        teamA_dic[teamA_days[i][0]] = teamA_days[i][1]
        
    teamB = int(input())
    teamB_days = []
    teamB_dic = {}
    
    for i in range(teamB):
        teamB_days.append(list(map(int, input().split())))
        teamB_dic[teamB_days[i][0]] = teamB_days[i][1]
        
    output = 0
    checked = {}
    for i in range(len(teamA_days)):
        if teamA_days[i][0] in teamB_dic:
            maximum = max(teamA_dic[teamA_days[i][0]],teamB_dic[teamA_days[i][0]])
            output += maximum
            teamA_dic.pop(teamA_days[i][0])
            teamB_dic.pop(teamA_days[i][0])
            checked[teamA_days[i][0]] = 1
        else:
            output += teamA_days[i][1]
    
    for i in range(len(teamB_days)):
        if teamB_days[i][0] not in checked:
            output += teamB_days[i][1]
    
    return output

A = business_men()
print(A)
        
        