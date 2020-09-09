# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 01:05:16 2020

@author: alexi
"""

#http://codeforces.com/problemset/problem/676/A -- Alexis Galvan

    

def nicolas_swap():
    lenght = int(input())
    array = input().split()
    array = [int(i) for i in array]
    un_swap = False
    
    if int(min(array)) == int(array[-1]):
        if int(max(array)) == int(array[0]):
            un_swap = True
    elif int(min(array)) == int(array[0]):
        if int(max(array)) == int(array[-1]):
            un_swap = True
            
    if un_swap:
        print(abs(int(len(array)-1)-int(0)))
    else:
        if int(min(array)) == int(array[0]) or int(min(array)) == int(array[-1]):
            print(abs(int(len(array)-1)-int(0)))
        elif int(max(array)) == int(array[0]) or int(max(array)) == int(array[-1]):
            print(abs(int(len(array)-1)-int(0)))
        else:
            dic = {}
            dic[int(max(array))] = 0
            dic[int(min(array))] = 0
            o = 0
            for x in range(len(array)):
                if int(array[x]) in dic:
                    dic[int(array[x])] = x
                    o += 1
                if o == 2:
                    break
            maximum = abs(dic[min(dic)]-0)
            if (abs(dic[min(dic)]-int(len(array)-1))) > maximum:
                maximum = abs(dic[min(dic)]-int(len(array)-1))
            if (abs(dic[max(dic)]-0)) > maximum:
                maximum = abs(dic[max(dic)]-0)
            if (abs(dic[max(dic)]-int(len(array)-1))) > maximum:
                maximum = abs(dic[max(dic)]-int(len(array)-1))
            
            print(maximum)
                
            

nicolas_swap()

                

            
            
    
    