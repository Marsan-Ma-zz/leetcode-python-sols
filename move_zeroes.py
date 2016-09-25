# https://leetcode.com/problems/move-zeroes/
# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        

        # [Idea]
        # 1. moving pointer check from end of array, switch if zero

        # [boundary cases]
        if len(nums) < 2: return nums

        # ---[main]---
        ptr1 = 0
        while nums[ptr1] != 0: 
            ptr1 += 1
            if ptr1 == len(nums): break
                
        ptr2 = ptr1 + 1
        while ptr2 < len(nums):
            if nums[ptr2] != 0:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr1, ptr2 = ptr1+1, ptr2+1
            else:
                ptr2 += 1
        print(nums)

                
    def test(self):
        cases = [
            [0],
            [0,1],
            [1,2,0,4,3],
            [1,4,3,0,0,2,4,0,6,7,0,0,0,0],
        ]
        for c in cases:
            self.moveZeroes(c)

            
Solution().test()