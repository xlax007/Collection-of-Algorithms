# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 00:33:23 2020

@author: Lenovo
"""






def merge_sorted_lists(arrayA, arrayB):
    output = []
    
    while len(arrayA) > 0 and len(arrayB)> 0:
        if arrayA[0] < arrayB[0]:
            output.append(arrayA[0])
            arrayA.pop(0)
        else:
            output.append(arrayB[0])
            arrayB.pop(0)
    
    while len(arrayA) > 0:
        output.append(arrayA[0])
        arrayA.pop(0)
        
    while len(arrayB) > 0:
        output.append(arrayB[0])
        arrayB.pop(0)
        
    return output




lista = [1,2,3,4,5,6,7,8,9]

lista2 = [5,7,12,13,14,15,16,20]

merge_sorted_lists(lista,lista2)