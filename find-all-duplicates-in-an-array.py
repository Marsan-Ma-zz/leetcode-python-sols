# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]



class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # [Ideas]
        # 1. still use index to save number, by adding len(nums)
        #    to original number to make difference,
        #    thus we could record > 1 action numbers
        # 2. be careful about +1/-1 in index/value
        
        m = len(nums)
        for i,n in enumerate(nums):
            nums[(n-1)%m] = nums[(n-1)%m] + m
        return [i+1 for i,n in enumerate(nums) if n > 2*m]