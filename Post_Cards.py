# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 02:29:32 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/137/A --- Alexis Galvan


def post_cards():
    
    string = input()
    
    dic = {'C':0,'P':0}
    
    if len(string) == 1:
        return 1
    
    aux = string[0]
    output = 0
    for i in range(len(string)):
        if string[i] != aux:
            output += 1
            dic[aux] = 0
            aux = string[i]
            dic[aux] = 1
        else:
            dic[string[i]] += 1
            if dic[string[i]] == 5:
                dic[string[i]] = 0
                aux = '?'
                    
    output += 1
    return output
             
A = post_cards()
print(A)
