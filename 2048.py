# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:53:15 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1221/A - Alexis Galvan Cardenas

def game_2048():
    cases = int(input())
    sizes = []
    arrays = []
    for i in range(cases):
        sizes.append(int(input()))
        arrays.append(input().split())
    
    for i in range(len(arrays)):
        array_aux = []
        dic = {}
        end = change = positive = False
        while True:
            for j in range(len(arrays[i])):
                if int(arrays[i][j]) not in dic:
                    dic[int(arrays[i][j])] = 1
                    if 2048 in dic:
                        end = True
                        break
                    elif 1024 in dic:
                        if dic[1024] >= 2:
                            end = True
                            positive = True
                            break
                    elif 512 in dic:
                        if dic[512] >= 4:
                            end = True
                            positive = True
                            break
                    elif 256 in dic:
                        if dic[256] >= 8:
                            end = True
                            positive = True
                            break
                else:
                    dic[int(arrays[i][j])] += 1
                    change = True
            
            if end or not change:
                break 
            
            x = 1
            while x != 4096:
                if x in dic:
                    aux = dic[x]
                    if aux == 1:
                        array_aux.append(x)
                    else:
                        temp = dic[x] % 2
                        double_time = int(dic[x]/2)
                        for m in range(double_time):
                            array_aux.append(x*2)
                        for n in range(temp):
                            array_aux.append(x)
                x *= 2
            arrays[i] = array_aux.copy()
            array_aux = []
            dic = {}
            
        if 2048 in dic or positive:
            print("YES")
        else:
            print("NO")
        
            
game_2048()          