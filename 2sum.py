# https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such 
# that they add up to a specific target.

# You may assume that each input would have exactly one solution.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # [Idea]:
        # 1. one-pass through nums, save another number needed in hash
        # 2. return if good couple found
        
        
        # exception handling
        if len(nums) < 2:
            return []
        
        rec = {}
        for i1, n1 in enumerate(nums):
            i2 = rec.get(target - n1)
            if i2 != None:
                return i2, i1
            else:
                rec[n1] = i1
        return []
    
    
    def test(self):
        cases = [
            ([], 1),
            ([2, 7, 11, 15], 9),
            ([-1, 2, 3, 1], 3),
        ]
        for nums, target in cases:
            res = self.twoSum(nums, target)
            print(nums, target, res)
            
            
Solution().test()