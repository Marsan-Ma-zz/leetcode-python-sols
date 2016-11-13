# https://leetcode.com/problems/contains-duplicate-ii/

# Given an array of integers and an integer k, 
# find out whether there are two distinct indices i and j in the array 
# such that nums[i] = nums[j] and the difference between i and j is at most k.



class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        # [Ideas]
        # 1. use hash-table to track existing number
        # 2. use two pointer for nums, cancel out lag number from 
        #    hash-table
        
        
        exist = set()
        for i, n in enumerate(nums):
            if n in exist:
                return True
            else:
                exist |= {n}
            if i >= k:
                exist.remove(nums[i-k])
        return False
    
    
    def test(self):
        cases = [
            ([], 1),
            ([1,2,3], 2),
            ([1,2,3,1,2], 3),
            ([1,2,3,1,2], 2),
            ([1,2,3,1,2], 1),
        ]
        for nums, k in cases:
            print(nums, k, self.containsNearbyDuplicate(nums, k))
            
            
# Solution().test()