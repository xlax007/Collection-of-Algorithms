# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:14:38 2020

@author: Lenovo
"""


#https://codeforces.com/contest/1305/problem/A

import itertools

def check(array):
    dic = {}
    for i in range(len(array)):
        temp = int(array[i][0]) + int(array[i][1])
        if temp not in dic:
            dic[temp] = 1
        else:
            return False
    return True
        

def necklace():
    cases = int(input())
    total = []
    daughters = []
    for i in range(cases):
        daughters.append(int(input()))
        for i in range(2):
            total.append(input().split())


    for i in range(len(daughters)):
        lista3 = itertools.permutations(total[0], len(total[1]))    
        all_combinations = []
        for each_permutation in lista3:
            zipped = zip(each_permutation, total[1])
            all_combinations.append(list(zipped))
            if check(all_combinations[0]):
                output = all_combinations[0][0][0]
                output2 = all_combinations[0][0][1]
                for y in range(1, len(all_combinations[0])):
                    output += ' ' + all_combinations[0][y][0]
                    output2 += ' ' + all_combinations[0][y][1]
                print(output)
                print(output2)
                total.pop(0)
                total.pop(0)
                break
            else:
                all_combinations.pop(0)



necklace()
            

            

        
    
    