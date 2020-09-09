# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 01:31:55 2020

@author: Lenovo
"""


def hulk():
    times = input()
    output = "I hate"
    if int(times) == 1:
        print(output + " it")
        return
     
    while True:
        for i in range(int(times)-1):
            if i == 0:
                output += " that I love"
                check = True
            elif i == 1:
                output += " that I hate"
                check = True
            elif i == 2:
                times = int(times) - 2
                check = False
                break
        if int(times) <= 3 and check:
            break
    
    output += " it"
    print(output)
    
    return
    


hulk()

