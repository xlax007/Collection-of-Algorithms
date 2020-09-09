# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:38:14 2020

@author: Lenovo
"""



def angry_students():
    cases = input()
    number_letters = []
    output = 0
    contador = 0
    checked = False
    letters = [[] for i in range(int(cases))]
    for i in range(int(cases)):
        number_letters.append(input())
        aux = input()
        for j in aux:
            letters[i].append(j)
    for i in range(len(letters)):
        while contador == 0:
            for letter in range(len(letters[i])-1):
                if checked:
                    checked = False
                elif letters[i][letter] == "A":
                    if letters[i][letter+1] == "P":
                        letters[i][letter+1] = "A"
                        contador += 1      
                        checked = True
            if contador != 0 :
                contador = 0
                output += 1
            else:
                print(output)
                output = 0
                contador = 0
                break
    return
                
            
angry_students()


