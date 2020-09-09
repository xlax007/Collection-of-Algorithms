# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 03:26:13 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/620/B --- Alexis Galvan


dic = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}

def old_calc():
    a = input().split()
    
    output = 0
    
    for i in range(int(a[0]),int(a[1])+1):
        if i > 9:
            temp = str(i)
            for j in range(len(temp)):
                output += dic[int(temp[j])]

        else:    
            output += dic[i]
            
    
    print(output)

old_calc()