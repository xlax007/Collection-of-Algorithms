# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 02:03:54 2020

@author: alexi
"""

#http://codeforces.com/problemset/problem/1133/A --- Alexis Galvan


def contest_time():
    time1 = input()
    time2 = input()
    
    timeA = (int(time1[0])*600) + (int(time1[1])*60) + (int(time1[3])*10) + (int(time1[4]))
    timeB = (int(time2[0])*600) + (int(time2[1])*60) + (int(time2[3])*10) + (int(time2[4]))
    
    hour_24 = int(time1[0])
    hour = int(time1[1])
    minute_60 = int(time1[3])
    minute = int(time1[4])
    
    for i in range(int((timeB-timeA)/2)):
        minute += 1
        if minute == 10:
            minute = 0
            minute_60 += 1
        if minute_60 == 6:
            minute_60 = 0
            hour += 1
        if hour == 10:
            hour = 0
            hour_24 += 1
    
    print(str(hour_24)+str(hour)+':'+str(minute_60)+str(minute))
    
contest_time()