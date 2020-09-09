# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 05:45:34 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/424/A --- Alexis Galvan


def hamster_squat():
    
    total = int(input())
    
    hamsters = input()
    
    dic = {'x':0,'X':0}
    
    for i in range(len(hamsters)):
        dic[hamsters[i]] += 1
    
    if dic['x'] == dic['X']:
        print(0)
        print(hamsters)
        return
    
    sat = dic['x']
    stood = dic['X']
    
    add_lower = False
    if sat < stood:
        add_lower = True
    
    maximum = max(sat, stood)
    add = maximum - (int((sat+stood)/2))
    print(add)
    if add_lower:
        output = ''
        hamsters = [i for i in hamsters]
        for i in range(len(hamsters)):
            if add > 0:
                if hamsters[i] == 'X':
                    hamsters[i] = 'x'
                    add -= 1
 
            output = output + hamsters[i]

    else:
        output = ''
        hamsters = [i for i in hamsters]
        for i in range(len(hamsters)):
            if add > 0:
                if hamsters[i] == 'x':
                    hamsters[i] = 'X'
                    add -= 1

            output = output + hamsters[i]

    
    print(output)

hamster_squat()
    
    

    
        

    
    