# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:30:07 2020

@author: alexi
"""



#http://codeforces.com/problemset/problem/1174/A -- Alexis Galvan

from itertools import permutations 


def check(array):
    sum_left = 0
    sum_right = 0
    for i in range(int(len(array)/2)):
        sum_left += int(array[i])
        sum_right += int(array[-(i+1)])
    
    if sum_left == sum_right:
        return True
    else:
        return False

def fails_thanos():
    n = int(input())
    array = input().split()
    
    if min(array) == max(array):
        print(-1)
    elif not check(array):
        output = ''
        for x in array:
            output += x + ' '
        
        print(output)
        return        
    else:
        for i in permutations(array):
            if not check(i):
                output = ''
                for x in i:
                    output += x + ' '
                
                print(output)
                return
        
        print(-1)
        
fails_thanos()



    


