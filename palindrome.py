# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 00:58:44 2020

@author: Lenovo
"""
#You should implement a function that takes as argument a string SS. You can append any characters in the front or at the end of SS. Return the minimum number of characters you should append in order to make SS a palindrome.
#aba = 0
#xzz = 1 = xzzx
#abc = 2 = cbabc or abcba
#abaabaab = 1 = abaabaaba

def check_palindrome(string):
    for i in range(len(string)):
        if string[i] != string[(-1)-i]:
            break
        if i >= (len(string)/2):
            return True

def palindrome_creation(string):
    if check_palindrome(string):
        return 0   
    if check_palindrome(string + string[0]) or check_palindrome(string[-1] + string):
        return 1
    characters = 1 
    while True:
        string2 = ""
        string3 = string
        for i in range(characters+1):
            string2 += string3[(-1)-i]
        string2 += string3
        for i in range(characters+1):
            string3 += string[(characters)-i]
        characters += 1
        if check_palindrome(string2) or check_palindrome(string3):
            return characters

    
###
string = input()
answer = palindrome_creation(string)
print(answer)

