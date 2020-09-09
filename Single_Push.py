# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:33:15 2020

@author: alexi
"""



#http://codeforces.com/problemset/problem/1253/A



def check_greater(arrayA, arrayB):
    for i in range(len(arrayA)):
        if int(arrayA[i]) > int(arrayB[i]):
            return False
    return True

def check(arrayA, arrayB):
    for i in range(len(arrayA)):
        if arrayA[i] != arrayB[i]:
            return False
    return True

def imposible(arrayA, arrayB):
    checker = []
    for i in range(len(arrayA)):
        if int(arrayA[i]) != int(arrayB[i]):
            checker.append(i)
    
    for i in range(len(checker)):
        if (i+1) < len(checker):
            if (checker[i]+1) != (checker[i+1]):
                return True
    
    return False
        
        

def single_push():
    cases = int(input())
    length = []
    arrayA = []
    arrayB = []
    
    for i in range(cases):
        length.append(int(input()))
        arrayA.append(input().split())
        arrayB.append(input().split())
    
    
    for i in range(len(arrayA)):
        if check(arrayA[i], arrayB[i]):
            print("YES")
        elif not check_greater(arrayA[i],arrayB[i]):
            print("NO")
        elif imposible(arrayA[i], arrayB[i]):
            print("NO")
        else:
            dic = {}
            change = True
            for j in range(len(arrayA[i])):
                if (int(arrayB[i][j]) - int(arrayA[i][j])) not in dic:
                    dic[(int(arrayB[i][j]) - int(arrayA[i][j]))] = 1
                    if len(dic) > 2:
                        print("NO")
                        change = False
                        break
            if change:
                if len(dic) == 2:
                    if 0 in dic:
                        print("YES")
                    else:
                        print("NO")
                elif len(dic) < 2:
                    print("YES")

single_push()

            
        