# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 19:50:17 2020

@author: Lenovo
"""


#https://codeforces.com/contest/1316/problem/A

def add_total(array):
    output = 0
    for i in range(len(array)):
        output += int(array[i])
    return output

def maximize_grade():
    cases = int(input())
    students = [] #[0] = students, [1] = max grade
    grades = []
    for i in range(cases):
        students.append(input().split())
        grades.append(input().split())
    
    for i in range(len(students)):
        if int(students[i][1]) == int(grades[i][0]):
            print(int(grades[i][0]))
        else:
            total = add_total(grades[i])
            if total >= int(students[i][1]):
                print(int(students[i][1]))
            else:
                print(total)

                
maximize_grade()
            