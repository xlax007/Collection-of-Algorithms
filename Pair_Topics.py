# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:33:27 2020

@author: alexi
"""



#http://codeforces.com/contest/1324/problem/D -- Alexis Galvan



def pair_topics():
    length = int(input())
    topicA = list(map(int, input().split()))
    topicB = list(map(int, input().split()))
    
    output = 0
    for i in range(len(topicA)):
        for j in range(i+1, len(topicA)):
            temp = topicA[i] + topicA[j]
            if temp > (topicB[i] + topicB[j]):
                output += 1
    
    return output

answer = pair_topics()
print(answer)
            