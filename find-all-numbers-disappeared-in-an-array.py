# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the 
# returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]



class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # [Ideas]
        # 1. for any appearing number i, mark nums[i] as negative,
        #    then traverse again, report all positive indexes.
        
        for n in nums:
            k = abs(n)
            nums[k-1] = -abs(nums[k-1])
            
        return list({i+1 for i, n in enumerate(nums) if n > 0})
        
        
    def test(self):
        cases = [
            [],
            [4,3,2,7,8,2,3,1],
            [4,3,2,7,8,2,3,6,6,6,3,3,2,4,8],
        ]
        for c in cases:
            print(c, self.findDisappearedNumbers(c))
            
# Solution().test()