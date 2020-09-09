# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 02:34:09 2020

@author: alexi
"""



#http://codeforces.com/problemset/problem/1027/A -- Alexis Galvan

dic_pos = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,
           'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,
           'v':21,'w':22,'x':23,'y':24,'z':25}
dic_let = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',
           11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',
           21:'v',22:'w',23:'x',24:'y',25:'z'}


def check(letterA, letterB):
    if letterA == letterB:
        return True
    else:
        if (dic_pos[letterB]+1) in dic_let:
            if (dic_pos[letterA]+1) in dic_let:
                if dic_let[(dic_pos[letterB])+1] == dic_let[(dic_pos[letterA])+1]:
                    return True
            if (dic_pos[letterA]-1) in dic_let:
                if dic_let[(dic_pos[letterB])+1] == dic_let[(dic_pos[letterA])-1]:
                    return True
        if (dic_pos[letterB]-1) in dic_let:

            if (dic_pos[letterA]+1) in dic_let:
                if dic_let[(dic_pos[letterB])-1] == dic_let[(dic_pos[letterA])+1]:
                    return True
            if (dic_pos[letterA]-1) in dic_let:
                if dic_let[(dic_pos[letterB])-1] == dic_let[(dic_pos[letterA])-1]:
                    return True

        
        
        
        return False
    

def palindromic_switch():

    
    cases = int(input())
    length = []
    arrays = []
    
    for i in range(cases):
        length.append(int(input()))
        arrays.append(input())
    
    
    for i in range(len(arrays)):
        if len(arrays[i]) == 2:
            if check(arrays[i][0],arrays[i][1]):
                print("YES")
            else:
                print("NO")
        else:
            x = 0
            yes = True
            while x < int(len(arrays[i])/2):
                if check(arrays[i][x], arrays[i][-(1+x)]):
                    x += 1
                else:
                    yes = False
                    break
            
            if yes:
                print("YES")
            else:
                print("NO")
            

palindromic_switch()
            
            
    
    
        
        

