# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:04:16 2020

@author: Lenovo
"""


#ZS the Coder is coding on a crazy computer. If you don't type in a word for a c consecutive seconds, everything you typed disappear!

#For example, if c = 5 and you typed words at seconds 1, 3, 8, 14, 19, 20 then at the second 8 there will be 3 words on the screen. After that, everything disappears at the second 13 because nothing was typed. At the seconds 14 and 19 another two words are typed, and finally, at the second 20, one more word is typed, and a total of 3 words remain on the screen.

#input
#6 5
#1 3 8 14 19 20
#output
#3
#input
#6 1
#1 3 5 7 9 10
#output
#2


def crazy_computer():
    cases = input().split() ##[0] = number of words, [1] = c
    words = input().split()
    
    output = 1
    
    for i in range(1,len(words)):
        if (int(words[i]) - int(words[i-1])) > int(cases[1]):
            output = 1
        else:
            output += 1
    
    print(output)
    return 
        
    
crazy_computer()

