# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 21:50:25 2020

@author: alexi
"""

#http://codeforces.com/problemset/problem/1251/A - Alexis Galvan


def broken_keyboard():
    cases = int(input())
    strings = []
    for i in range(cases):
        strings.append(input())
    
    for i in range(len(strings)):
        if len(strings[i]) == 1:
            print(strings[i])
        else:
            dic = {}
            check = False
            for j in range(len(strings[i])):
                if check:
                    check = False
                    continue
                if j+1 < len(strings[i]):
                    if strings[i][j] not in dic:                      
                        if strings[i][j] != strings[i][j+1]:
                            dic[strings[i][j]] = 1
                        else:
                            check = True
                elif j == len(strings[i])-1:
                    if strings[i][j] not in dic:
                        dic[strings[i][j]] = 1
            
            print(dic)
        
broken_keyboard()
                            
                

                    
            
            
                
            
    