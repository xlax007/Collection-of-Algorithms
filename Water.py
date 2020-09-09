# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:37:18 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1118/A



def water():
    
    cases = int(input())
    ind = []
    
    for i in range(cases):
        ind.append(input().split()) #3 inputs. [0] = L water he need, [1] = price of 1L bottle, [2] price of 2L bottle
    
    for i in range(len(ind)):
        if (int(ind[i][0])) == 1:
            print(int(ind[i][1]))
            continue
        
        if (int(ind[i][1])*2) <= int(ind[i][2]):
            print((int(ind[i][1]))*(int(ind[i][0])))
        else:
            if int(ind[i][0]) % 2 == 0:
                print(int(((int(ind[i][0]))*(int(ind[i][2])))/2))
            else:
                ind[i][0] = int(ind[i][0]) - 1
                print(int((((int(ind[i][0]))*(int(ind[i][2])))/2)+ int(ind[i][1])))
                
            
water()



        
            
        
    