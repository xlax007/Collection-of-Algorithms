# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:49:52 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/1005/B - Alexis Galvan

def delete_left():
    stringA = input()
    stringB = input()
    
    if stringA == stringB:
        print(0)
    elif len(stringA) == 0:
        print(len(stringB))
    elif len(stringB) == 0:
        print(len(stringA))
    else:
        counter = 0
        if len(stringA) == len(stringB):
            while stringA != stringB:
                stringA = stringA[1:]
                stringB = stringB[1:]
                counter += 2
            print(counter)
        else:
            if len(stringA) > len(stringB):
                delete = max(len(stringA),len(stringB)) - min(len(stringA),len(stringB))
                stringA = stringA[delete::]
                counter += delete
                while stringA != stringB:
                    stringA = stringA[1:]
                    stringB = stringB[1:]
                    counter += 2
                print(counter)
            else:
                delete = max(len(stringA),len(stringB)) - min(len(stringA),len(stringB))
                stringB = stringB[delete::]
                counter += delete
                while stringA != stringB:
                    stringA = stringA[1:]
                    stringB = stringB[1:]
                    counter += 2
                print(counter)                
        
delete_left()  