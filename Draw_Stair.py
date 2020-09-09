# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:00:57 2020

@author: alexi
"""



#https://www.hackerrank.com/challenges/staircase/problem?h_r=next-challenge&h_v=zen --- Alexis Galvan


def draw_stair(length):

    for i in range(length):
        print((' '*(length-(i+1)))+('#'*(i+1)))

length = int(input())
draw_stair(length)