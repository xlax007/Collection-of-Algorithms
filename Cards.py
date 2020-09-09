# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:57:22 2020

@author: Lenovo
"""
########check what rank of hand you have in poker

def check_royal(dic):
    royal_flush = ['1','J','Q','K','A']
    for i in royal_flush:
        if i in dic:
            continue
        else:
            return False
    return True
    

def check_consecutive(dic):
    consecutive = ['2','3','4','5','6','7','8','9','1','J','Q','K','A']
    for i in range(0, len(consecutive)-4):
        if consecutive[i] in dic:
            for j in range(i+1,i+5):
                if consecutive[j] in dic:
                    continue
                else:
                    return False
            return True
    return False

def check_highest(dic):
    highest = ['A','K','Q','J','1','9','8','7','6','5','4','3','2']
    for i in highest:
        if i in dic:
            return "Highest:" + str(i)
    
def cards(array):
    count_suit = {}
    count_numbers = {}
    pair = 0
    three = 0
    for i in range(len(array)):
        
        if array[i][0] == '1':
            array[i] = array[i][0] + array[i][-1]

        
        if array[i][1] in count_suit:
            count_suit[array[i][1]] += 1
        else:
            count_suit[array[i][1]] = 1
        
        
        if array[i][0] in count_numbers:
            count_numbers[array[i][0]] += 1
        else:
            count_numbers[array[i][0]] = 1     
    
    if len(count_suit) == 1:
        if check_royal(count_numbers):
            return "Royal Flush"
        elif check_consecutive(count_numbers):
            return "Straight Flush"
        else:
            return "Flush"
    else:
        for i in count_numbers:
            if count_numbers[i] == 4:
                return "Four of a Kind"
            elif count_numbers[i] == 3:
                three += 1

            elif count_numbers[i] == 2:
                pair += 1
        if three == 1 and pair == 1:
            return "Full House"
        elif three == 1:
            return "Three of a kind"
        elif pair > 0:
            return str(pair) + "Pair"
        else:
            if check_consecutive(count_numbers):
                return "Straight"
            else:
                return check_highest(count_numbers)
                

royal_flush =['AC','KC','QC','JC','10C']
straight_flush = ['9C','8C','7C','6C','5C']
four = ['AC','AS','AH','AD','9C']
full = ['AC','AS','AH','JC','JH']
flush = ['AC','2C','5C','7C','9C']
straight = ['8C','7H','6S','5D','4C']
three = ['5C','QC','2C','2H','2D']
two_pair = ['AC','AH','KC','KH','2C']
one_pair = ['4H','5S','8C','AD','AS']
high_card = ['5S','6D','JC','QD','AS']

cards(high_card)


