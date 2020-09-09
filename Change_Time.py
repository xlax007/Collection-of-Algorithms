# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:10:36 2020

@author: alexi
"""



#https://www.hackerrank.com/challenges/time-conversion/problem?h_r=next-challenge&h_v=zen


def time_militar(time):
    
    if time[-2] == 'A':
        if time[0] == '1' and time[1] == '2':
            time = time[2:]
            print('00'+time[:len(time)-2])
        else:
            print(time[:len(time)-2])
    else:
        if time[0] == '0':
            temp = int(time[1])
            temp += 12
            time = time[2:]
            print(str(temp)+time[:len(time)-2])
        else:
            temp = int(time[0]+time[1])
            if temp != 12:                
                temp += 12
            if temp == 24:
                temp = '00'
            time = time[2:]
            print(str(temp)+time[:len(time)-2])

time = input()
time_militar(time)