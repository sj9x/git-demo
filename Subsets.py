#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:42:13 2023

@author: swatjain

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Psuedocode

## Check if the list is empty
return list of list 

## subsets nums[1:]



"""
class Solution:
    def subsets(self, nums):
        self.nums = nums
        ans = self.subsets2(0)
        return ans
        
    def subsets2(self,st):
        if len(self.nums[st:])==0:
            return [[]]
        out = self.subsets2(st+1).copy()
        new = [[self.nums[st]]+w.copy() for w in out]
        return new.copy()+out.copy()
        
testinputs  = [[],[1],[1,2],[1,2,3]]
testoutputs = [
    [[]],
    [[],[1]],
    [[],[1],[2],[1,2]],
    [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
    ]        

s = Solution()
for k in range(len(testinputs)):
    assert sorted(testoutputs[k]) == sorted(s.subsets(testinputs[1])), f"test failed for: {k+1}th input"
        
