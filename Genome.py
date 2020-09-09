# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 05:39:00 2020

@author: alexi
"""



#https://codeforces.com/problemset/problem/747/B --- Alexis Galvan


def check(string):
    dic = {'A':0,'C':0,'G':0,'T':0}
    for i in range(len(string)):
        if string[i] in dic:
            dic[string[i]] += 1
            
    if dic['A'] == dic['C'] and dic['A'] == dic['G'] and dic['A'] == dic['T']:
        return False
    else:
        return True
    
    

def genome():
    
    length = int(input())
    string = input()
    
    dic = {'A':0,'C':0,'G':0,'T':0,'?':0}
    
    for i in range(len(string)):
        if string[i] in dic:
            dic[string[i]] += 1
    
    if dic['A'] == dic['C'] and dic['A'] == dic['G'] and dic['A'] == dic['T'] and dic['?'] == 0:
        if dic['A'] != 0:
            return string
    
    need = []
    maximum = dic['A']
    add_one = False
    if dic['C'] > maximum:
        maximum = dic['C']
    if dic['G'] > maximum:
        maximum = dic['G']
    if dic['T'] > maximum:
        maximum = dic['T']
        
    if dic['A'] == 0 and dic['C'] == 0 and dic['G'] == 0 and dic['T'] == 0:
        maximum = 1
        add_one = True
        
    if add_one:
        need = ['A','C','G','T']
    else:
        while dic['A'] != dic['C'] or dic['A'] != dic['G'] or dic['A'] != dic['T']:
            if dic['A'] < maximum:
                need.append('A')
                dic['A'] += 1
            if dic['C'] < maximum:
                need.append('C')
                dic['C'] += 1
            if dic['G'] < maximum:
                need.append('G')
                dic['G'] += 1
            if dic['T'] < maximum:
                need.append('T')
                dic['T'] += 1   
    
    if (len(string)-(dic['A']+dic['C']+dic['G']+dic['T'])) % 4 != 0:
        return '==='
    
    out = ['A','C','G','T']
    string = [string[i] for i in range(len(string))]
    for i in range(len(string)):
        if string[i] == '?':
            if len(need) == 0:
                need = out.copy()
            string[i] = need[0]
            need.pop(0)
    
    if check(string) or len(need) > 0:
        return '==='
    
    output = ''
    for i in range(len(string)):
        output = output + string[i]
    
    return output

A = genome()
print(A)



    
            