# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:03:17 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1249/B1

def book_echange():
    cases = int(input())
    kids_n = []
    kids = []
    for i in range(cases):
        kids_n.append(int(input()))
        kids.append(input().split())
    
    for i in range(len(kids)):
        output = []
        for j in range(len(kids[i])):
            counter = 0
            if int(kids[i][j]) == (j+1):
                counter += 1
                output.append(counter)
            else:
                temp = (int(kids[i][j]) - 1)
                while True:
                    counter += 1
                    if temp == j:
                        output.append(counter)
                        break
                    else:
                        temp = (int(kids[i][temp]) - 1)

        string = str(output[0])
        for x in range(1, len(output)):
            string += ' ' + str(output[x])
        print(string)
                     


book_echange()
                    
                    
                    
                