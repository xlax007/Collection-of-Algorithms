# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:45:22 2020

@author: Lenovo
"""



#https://codeforces.com/problemset/problem/334/A


def candy_bags():
    brothers = int(input())
    bags = [i for i in range(1,(brothers**2)+1)]
    
    all_brothers = [[] for i in range(brothers)]
    
    for i in range(len(all_brothers)):
        for j in range(int(brothers/2)):
            all_brothers[i].append(bags[0])
            all_brothers[i].append(bags[-1])
            bags.pop()
            bags.pop(0)
        
        output = str(all_brothers[i][0])
        for x in range(1,len(all_brothers[i])):
            output += ' ' + str(all_brothers[i][x])
        
        print(output)
    
    
candy_bags()