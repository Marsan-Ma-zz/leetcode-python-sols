# https://leetcode.com/problems/combination-sum-iv/

# Given an integer array with all positive numbers and no duplicates, 
# find the number of possible combinations that add up to a positive integer target.

# Example:

# nums = [1, 2, 3]
# target = 4

# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)

# Note that different sequences are counted as different combinations.

# Therefore the output is 7.

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. traverse through all possible combinartions
        #    => while branch reach or overflow, stop
        # 2. always traverse from small to large candidates
        #-------------------------------------
        # 1. dynamic programming, build the table of target
        #    and corresponding result
        
        if not nums: return 0
        
        lut = {0: 1}
        for t in range(1, target+1):
            lut[t] = sum([lut[t-n] for n in nums if t >= n])
        print(lut)
        return lut[target]
    
    
    def test(self):
        cases = [
            ([], 2),
            ([1,2], 4),
            ([1,2,3], 4),
        ]
        for nums, t in cases:
            res = self.combinationSum4(nums, t)
            print(nums, t, res)
            
Solution().test()
