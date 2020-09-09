# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:45:42 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/894/A


def Qaq():
    text = input()
    output = 0
    for i in range(len(text)):
        if text[i] == "Q":
            for j in range(i+1, len(text)):
                if text[j] == "A":
                    for x in range(j+1, len(text)):
                        if text[x] == "Q":
                            output += 1
    
    print(output)
    return

Qaq()


