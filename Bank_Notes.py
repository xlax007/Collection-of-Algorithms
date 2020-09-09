# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 01:57:01 2020

@author: alexi
"""


#https://csacademy.com/contest/interview-archive/task/banknotes/ --- Alexis Galvan



def banknotes(a, b, s, n):

    L = 0
    R = n
    
    
    if (a*n) == s:
        return n
    elif n == 1:
        if a == s:
            return 1
        elif b == s:
            return 0
        else:
            return -1
        
    
    while L < R:
        mid = L + int((R-L)/2)
        
        if ((mid*int(a)) + ((n-mid)*int(b))) == int(s):  
            return mid
        if ((mid*int(a)) + ((n-mid)*int(b))) < int(s): 
            if mid != 0:
                if (((mid-1)*int(a)) + ((n-(mid-1))*int(b))) > ((mid*int(a)) + ((n-mid)*int(b))) and (((mid-1)*int(a)) + ((n-(mid-1))*int(b))) <= int(s):
                    R = mid 
                else:
                    L = mid + 1
            else: 
                L = mid + 1
        elif(((mid+1)*int(a)) + ((n-(mid+1))*int(b))) < ((mid*int(a)) + ((n-mid)*int(b))):
            L = mid + 1
        elif(((mid+1)*int(a)) + ((n-(mid+1))*int(b))) == int(s):
            return mid+1
        else:
            R = mid 
        
        
    
    return -1
        
    
    
    
a, b, s, n = map(int, input().split(' '))
answer = banknotes(a, b, s, n)
print(answer)



