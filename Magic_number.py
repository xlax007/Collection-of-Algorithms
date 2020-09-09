# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:01:44 2020

@author: Lenovo
"""


#https://codeforces.com/problemset/problem/320/A

def magic_number():
    number = input()
    dic = {1,14,144}
    
    if number[0] != '1':
        print("NO")
        return
    
    i = 0
    while i < len(number):
        if number[i] == '1':
            if i+1 != len(number):
                if number[i+1] == '1':
                    i += 1
                    continue
                elif number[i+1] == '4':
                    if i+2 != len(number):
                        if number[i+2] != '4':
                            i += 2
                            continue
                        elif number[i+2] == '4':
                            i += 3
                            continue
                        else:
                            print("NO")
                            break
                    else:
                        break
                else:
                    print("NO")
                    return
            else:
                break
        else:
            print("NO")
            return
    
    print("YES")
    return

magic_number()
                        
                    
                
    
    
    