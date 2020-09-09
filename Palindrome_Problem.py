# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:45:34 2020

@author: alexi
"""


#http://codeforces.com/contest/1324/problem/B - Alexis Galvan


def check(array):
    R = len(array)-1
    
    for i in range(len(array)):
        if R < i:
            return True
        elif i == R:
            if array[i] == array[R]:
                return True
            return False
        if array[i] == array[R]:
            R -= 1
        else:
            return False
            

def palindrome_problem():
    cases = int(input())
    length = []
    arrays = []
    
    for i in range(cases):
        length.append(int(input()))
        arrays.append(list(map(int, input().split())))
    
    for i in range(len(length)):
        if length[i] == 3:
            if check(arrays[i]):
                print("YES")
            else:
                print("NO")
        elif length[i] < 3:
            print("NO")
        else:
            dic = {}
            found = False
            for j in range(len(arrays[i])):
                if arrays[i][j] in dic:
                    if int(j - dic[arrays[i][j]]) >= 2:
                        print("YES")
                        found = True
                        break                      
                    else:
                        arrays[i][j] = j
                else:
                    dic[arrays[i][j]] = j
            
            if not found:
                print("NO")
    
    
palindrome_problem()
            