# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 01:23:34 2020

@author: Lenovo
"""
#You are given an interval of integers [A, B][A,B]. 
#For each number in this interval compute its greatest odd divisor. Output the sum of these divisors.

def greatest_odd_divisor(array):
    while len(array) != 0:
        aux = [i for i in range(int(array[0][0]),int(array[0][1])+1)] 
        output = 0
        for i in aux:
            if int(i) % 2 != 0:
                output += int(i)
            else:
                temp = int(i) / 2
                while temp % 2 == 0:
                    temp = temp/2
                output += int(temp)
        
        print (output)
        array.pop(0)
    return
    

cases = input()
lista = []
for i in range(int(cases)):
    lista.append(input().split())

greatest_odd_divisor(lista)

