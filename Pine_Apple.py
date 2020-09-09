# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:05:53 2020

@author: alexi
"""


#http://codeforces.com/problemset/problem/697/A - Alexis Galvan


def pine_apple():
    time = input().split()
    time = [int(i) for i in time]
    
    if time[0] == time[2]:
        print("YES")
    elif time[0] > time[2]:
        print("NO")
    else:
        integer = 0
        s = int(time[2]/time[1])
        while (time[0] + (s*time[1])) > time[2]:
            s -= 1
        if s == 0:
            s = 1
        while True:
            temp = time[0] + (s*time[1]) + integer
            if temp == time[2]:
                print('YES')
                return
            elif temp > time[2]:
                print('NO')
                return
            else:
                if integer == 0:
                    integer += 1
                elif integer == 1:
                    integer = 0
                    s += 1

pine_apple()
                
            
