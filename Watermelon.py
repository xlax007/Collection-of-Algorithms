# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:53:59 2020

@author: Lenovo
"""


def Watermelon():
    kilos = input()
    if int(kilos) == 2:
        print ("NO")
        return
    elif int(kilos) % 2 == 0:
        print ("YES")
        return
    else:
        print ("NO")
        return
Watermelon()