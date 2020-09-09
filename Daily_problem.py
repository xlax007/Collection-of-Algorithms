# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:52:52 2020

@author: Lenovo
"""


######Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
######Output: 7 -> 0 -> 8
##############Explanation: 342 + 465 = 807.


def add_backwards(arrayOne , arrayTwo):
    first_num = ""
    second_num = ""
    output = ""
    for i in range(len(arrayOne)):
        first_num = str(arrayOne[i]) + first_num
    for i in range(len(arrayTwo)):
        second_num = str(arrayTwo[i]) + second_num
    total = str(int(first_num) + int(second_num))
    for i in total:
        output = i + output
    return output
        



arrayA = [2,4,3]
arrayB = [5,6,4]

add_backwards(arrayA,arrayB)