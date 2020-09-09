# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:55:53 2020

@author: Lenovo
"""
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#- Open brackets are closed by the same type of brackets.
#- Open brackets are closed in the correct order.
#- Note that an empty string is also considered valid.

#Example:
#Input: "((()))"
#Output: True

#Input: "[()]{}"
#Output: True

#Input: "({[)]"
#Output: False


def correct_parenthesis(string):
    if len(string) == 0:
        return True
    opendic = {'(':1,'[':2,'{':3}
    closeddic = {')':1,']':2,'}':3}
    opend = []
    closed = []
    for i in string:
        if i in opendic:
            opend.append(opendic[i])
        elif i in closeddic:
            if len(opend) == 0:
                return False
            closed.append(closeddic[i])
            if closed[0] == opend[0] or closed[0] == opend[-1]:
                if closed[0] == opend[-1]:
                    closed.pop(0)
                    opend.pop()
                else:
                    closed.pop(0)
                    opend.pop(0)
            else:
                return False
    if len(opend) == 0 and len(closed) == 0:  
        return True 
    else:
        return False
        
inputs = "()()()()()((()))[][()]"

correct_parenthesis(inputs)


