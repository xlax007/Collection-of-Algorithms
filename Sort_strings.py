# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 03:31:05 2020

@author: alexi
"""



dic_pos = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,
           'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,
           'v':21,'w':22,'x':23,'y':24,'z':25}



def quicksort_string(string):
    
    less = []
    equal = []
    greater = []
    
    if len(string) > 1:
        pivot = dic_pos[string[0]]
        for x in string:
            if dic_pos[x] < pivot:
                less.append(x)
            elif dic_pos[x] == pivot:
                equal.append(x)
            elif dic_pos[x] > pivot:
                greater.append(x)
        
        return quicksort_string(less) + equal + quicksort_string(greater)
    else:
        return string


string = 'awdawodjawojdoawjdowajdopwqjdoiqnoidnqwoindozclknqwkjbdpfouihaseidfbawehblzkouhaweijbnzq'

string = [string[i] for i in range(len(string))]

quicksort_string(string)