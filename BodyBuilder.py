# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:19:37 2020

@author: Lenovo
"""


##https://codeforces.com/problemset/problem/255/A

def bodybuilder():
    
    exercises = int(input())
    
    routine = input().split()
    
    dic = {"Chest":0,"Biceps":0,"Back":0}
    
    while len(routine) != 0:
        for i in dic:
            if len(routine) == 0:
                break
            dic[i] += int(routine[0])
            routine.pop(0)
    
    if dic["Chest"] > dic["Biceps"] and dic["Chest"] > dic["Back"]:
        print("chest")
        return
    elif dic["Biceps"] > dic["Chest"] and dic["Biceps"] > dic["Back"]:
        print("biceps")
        return
    else:
        print("back")
        return
    
bodybuilder()
    