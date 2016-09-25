# https://leetcode.com/problems/3sum/
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sols = set()
        # exceptions
        if len(nums) < 3: 
            return list(sols)

        # main
        visited = set()
        nums.sort()
        for i1, n1 in enumerate(nums):
            # 3sum with n1 as 1st number => 2 sum with target = -n1
            comb = {}
            if n1 in visited: 
                continue
            else:
                visited.add(n1)
                    
            for i2, n2 in enumerate(nums[i1+1:]):
                if comb.get(n2) != None:
                    sols.add((n1, comb[n2], n2))
                else:
                    comb[-n1-n2] = n2

        return list(sols)

    
    def test(self):
        cases = [
            [0],
            [1,2],
            [1,1,-2],
            [0,-1,1],
            [0,0,0,0,0],
            [-1, 0, 1, 1, 1, 2, -1, -4],
            [-1, 12, 0, 3, 1, 2, -1, -4, -3, 10],
        ]
        for c in cases:
            sols = self.threeSum(c)            
            print(c, sols)

            
Solution().test()
