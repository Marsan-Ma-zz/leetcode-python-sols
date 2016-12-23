# https://leetcode.com/problems/single-number-iii/

# Given an array of numbers nums, in which exactly two elements appear only once 
# and all the other elements appear exactly twice. Find the two elements that appear only once.

# For example:

# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using 
# only constant space complexity?



class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # [Ideas]
        # 1. xor all numbers, get the xor of the two number only appear once
        # 2. find any '1' bit of this result, this bit could separate this two number
        # 3. use this bit to partition all nums, so this two target number would be 
        #    separated in opposite group
        # 4. do all-xor for each group, we could find target two number accordingly.
        
        # get all xor
        par = 0
        for n in nums:
            par = par ^ n
        
        # get separation bit
        par = par & -par   # get 1st LSB '1' bit 
        
        # get each target
        sol1, sol2 = 0, 0
        for n in nums:
            if n & par:
                sol1 = sol1 ^ n
            else: 
                sol2 = sol2 ^ n
        return [sol1, sol2]
        