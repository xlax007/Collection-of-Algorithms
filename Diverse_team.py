# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:26:06 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/988/A


def diverse_team():
    
    students = input().split() ##[0] = number of students. [1] = number of students u need in a team
    grades = input().split()
    
    students = [int(i) for i in students]
    dic = {}
    temp = 0
    
    output = ""
    
    for i in range(len(grades)):
        if grades[i] not in dic:
            dic[grades[i]] = i + 1
            temp += 1
        if temp == students[1]:
            print("YES")
            for i in dic:
                if len(output) == 0:
                    output = output + str(dic[i])
                else:
                    output = output + ' ' + str(dic[i])
            print(output)
            return
    
    print("NO")
    return
    

diverse_team()
                
    
    