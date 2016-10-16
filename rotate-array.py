# https://leetcode.com/problems/rotate-array/

# Rotate an array of n elements to the right by k steps.

# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].



class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return []
        
        k = k % len(nums)
        k = len(nums) - k
        nums[0:len(nums)] = nums[k:] + nums[:k]
    
    
    def test(self):
        cases = [
            ([], 3),
            ([1,2,3], 1),
            ([1,2,3], 2),
            ([1,2,3], 5),
            ([1,2,3,4,5,6,7], 3),
            ([1,2,3,4,5,6,7], 10),
        ]
        for n, k in cases:
            m = n[:]
            self.rotate(m, k)
            print(n, k, m)
            
            
# Solution().test()