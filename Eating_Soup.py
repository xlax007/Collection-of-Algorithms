# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:35:42 2020

@author: alexi
"""



#http://codeforces.com/problemset/problem/1163/A -- Alexis Galvan


def eating_soup():
    cats = list(map(int, input().split()))
    
    if cats[0] == cats[1] or cats[0] == 0:
        return 0
    
    table = [i for i in range(1, cats[0]+1)]
    i = 0
    while cats[1] > 0:
        table.pop(i)
        i += 1
        cats[1] -= 1
        if i >= len(table):
            i = 0

        
    output = 0
    
    for i in range(len(table)):
        if i+1 < len(table):
            if table[i+1]-1 != table[i]:
                output += 1
    
    return output+1

    
A = eating_soup()
print(A)
    