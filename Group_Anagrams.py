# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:14:42 2020

@author: alexi
"""



#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/ --- Alexis Galvan

dic = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18
       ,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

def quick_sort(array):
    
    left = []
    equal = []
    right = []
    
    if len(array) > 1:
        pivot = dic[array[0]]
        for x in array:
            if dic[x] < pivot:
                left.append(x)
            elif dic[x] == pivot:
                equal.append(x)
            elif dic[x] > pivot:
                right.append(x)
        
        return quick_sort(left) + equal + quick_sort(right)
    else:
        
        return array
        
def group_anagrams():
    
    t_words = int(input())
    words = []
    lists = []
    groups = [[] for i in range(t_words)]
    table = {}
    
    for i in range(t_words):
        words.append(input())
        temp = [words[i][j] for j in range(len(words[i]))]
        temp = quick_sort(temp)
        output = ''
        for x in range(len(temp)):
            output = output + temp[x]
        if output not in table:
            table[output] = i
            groups[i].append(words[i])
        else:
            groups[table[output]].append(words[i])
            
            
    pop = []
    
    for i in range(len(groups)):
        if len(groups[i]) == 0:
            pop.append(i)
    
    for i in range(len(pop)):
        groups.pop(pop[(-i)-1])
            

    
    
    return groups

A = group_anagrams()
print(A)
    
    
        
    
    
    
    