# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 00:23:00 2020

@author: Lenovo
"""


def max_money():
    oponents = input()
    output = 0
    for i in range(int(oponents)):
        output += 1/(int(oponents)-i)
    print(output)
    return


max_money()



