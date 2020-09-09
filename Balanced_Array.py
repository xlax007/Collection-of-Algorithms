# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:35:34 2020

@author: alexi
"""



#https://codeforces.com/contest/1343/problem/B --- Alexis Galvan


def balanced_array():
    
    cases = int(input())
    
    arrays = [int(input()) for i in range(cases)]
    
    for i in range(len(arrays)):
        temp = int(arrays[i]/2)
        if temp % 2 != 0:
            print('NO')
            continue
        
      
  
        print('YES')
        
        output = ''
        output_2 = ''
        sum1 = 0
        sum2 = 0
        
        for i in range(temp):
            output += str(int(2*(i+1))) + ' '
            sum1 += int(2*(i+1))
            
            if i != (temp-1):
                output_2 += str(1 + (2*(i))) + ' '
                sum2 += int(1 + (2*(i)))


        last = sum1-sum2
        
        output_2 = output_2 + str(last) + ' '

        
        print(output+output_2)
        
balanced_array()