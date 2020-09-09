# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:37:24 2020

@author: alexi
"""



#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/ --- Alexis Galvan


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        length = len(nums)
        pop = []
        while i != length:
            if nums[i] == 0:
                pop.append(i)
                nums.append(0)
            i += 1
        
        for i in range(len(pop)):
            nums.pop(pop[(-i)-1])