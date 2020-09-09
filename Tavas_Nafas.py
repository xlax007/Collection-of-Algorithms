# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:02:27 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/535/A --- Alexis Galvan


def tavas_nafas():
    
    dic = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
           14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
           80:'eighty',90:'ninety'}
    dic_21 = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
    
    
    number = int(input())
    
    if number in dic:
        print(dic[number])
    else:
        temp = str(number)
        print(dic_21[int(temp[0])] + '-' + dic[int(temp[1])])
        
tavas_nafas()
    