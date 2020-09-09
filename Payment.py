# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:56:10 2020

@author: Lenovo
"""



def payment():
    total = int(input())
    
    cases = []
    
    for i in range(total):
        cases.append(input().split())
        
    for i in range(len(cases)):
        needed = 0
        while True:
            if needed == int(cases[i][-1]):
                print("YES")
                break
            
            if int(cases[i][-1]) <= int(cases[i][1]):
                print("YES")
                break
            
            if int(cases[i][0]) > 0:
                cases[i][0] = int(cases[i][0]) - 1
                needed += int(cases[i][2])
                if needed > int(cases[i][-1]):
                    needed -= int(cases[i][2])
                    cases[i][-1] = int(cases[i][-1]) - needed
                    if int(cases[i][-1]) <= int(cases[i][1]):
                        print("YES")
                        break
                    else:
                        print("NO")
                        break
            elif int(cases[i][0]) == 0:
                if (int(cases[i][1]) + needed) >= int(cases[i][-1]):
                    print("YES")
                    break
                print("NO")
                break
            
payment()        
