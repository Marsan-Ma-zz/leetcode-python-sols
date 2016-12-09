# https://leetcode.com/problems/longest-increasing-subsequence/

# Given an unsorted array of integers, find the length of longest increasing subsequence.

# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. 
# Note that there may be more than one LIS combination, it is only necessary for 
# you to return the length.

# Your algorithm should run in O(n2) complexity.

# Follow up: Could you improve it to O(n log n) time complexity?


from bisect import *

class Solution(object):

    # [10, inf, inf, inf, inf, inf, inf, inf, inf] 
    # [9, inf, inf, inf, inf, inf, inf, inf, inf] 
    # [2, inf, inf, inf, inf, inf, inf, inf, inf] 
    # [2, 5, inf, inf, inf, inf, inf, inf, inf] 
    # [2, 3, inf, inf, inf, inf, inf, inf, inf] 
    # [2, 3, 7, inf, inf, inf, inf, inf, inf] 
    # [2, 3, 7, 101, inf, inf, inf, inf, inf] 
    # [2, 3, 7, 18, inf, inf, inf, inf, inf] 
    def lengthOfLIS(self, nums):
        minend = [float('inf')] * (len(nums) + 1)
        for num in nums:
            minend[bisect_left(minend, num)] = num
            # print(minend)
        return minend.index(float('inf'))
    
    def test(self):
        cases = [
            [10, 9, 2, 5, 3, 7, 101, 18],
        ]
        for c in cases:
            print(self.lengthOfLIS(c))
            
# Solution().test()

