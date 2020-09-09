# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:06:52 2020

@author: alexi
"""



#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/ --- Alexis Galvan


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic.pop(nums[i])
        return next(iter(dic))
    

