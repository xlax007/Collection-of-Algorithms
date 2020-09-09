# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 02:48:33 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/837/A --- Alexis Galvan


dic = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

def check(string):
    output = 0
    for i in range(len(string)):
        if string[i] in dic:
            output += 1
    return output
    

def text_volume():
    length = int(input())
    
    text = input()
    alt = ''
    for i in range(len(text)):
        if text[i] != ' ':
            alt = alt + text[i]
        else:
            break
    
    maximum = check(alt)
    
    temp = ''
    for i in range(len(text)):
        if text[i] != ' ':
            temp = temp + text[i]
            if i == len(text)-1:
                temp_max = check(temp)
                if temp_max > maximum:
                    maximum = temp_max
        else:
            temp_max = check(temp)
            if temp_max > maximum:
                maximum = temp_max
            temp_max = 0
            temp = ''
        
    
    return maximum

A = text_volume()
print(A)    