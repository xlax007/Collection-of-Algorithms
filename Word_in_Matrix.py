# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:54:37 2020

@author: Lenovo
"""

def check_right(matrix, word, position):
    for i in range(len(matrix[position])):
        if matrix[position][i] != word[i]:
            return False
    return True

def check_top(matrix, word, position):
    for i in range(len(matrix)):
        if matrix[i][position] != word[i]:
            return False
    return True

def word_search(matrix, word):
    for i in range(len(matrix)):
        if matrix[i][0] == word[0]:
            if check_right(matrix, word, i):
                return True
    for i in range(len(matrix[0])):
        if matrix[0][i] == word[0]:
            if check_top(matrix, word, i):
                return True
    
    return False


matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print (word_search(matrix, 'FACI'))