# https://leetcode.com/problems/subsets-ii/

# Given a collection of integers that might contain duplicates, nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

from collections import Counter
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # [Ideas]
        # 1. brute force: every number is a switch (on/off), 
        #    2**n possible solutions then use set() to distinct
        # 2. improve: count numbers use collections.Counter
        #    then only variate used number of each number
        #    Ex: {1: 2, 4: 2, 2: 1, 3: 1, 5: 1}
        #    => 0-2 1's, 0-2 4's, 0-1 2's, 0-1 3's, 0-1 5's
        
        
        self.sols = []
        stat = list(Counter(nums).items())
        
        self.dfs(stat, [])
        return self.sols
    
    def dfs(self, stat, current):
        if len(stat) == 0:
            self.sols.append(current)
        else:
            num, cnt = stat[0]
            for i in range(cnt+1):
                self.dfs(stat[1:], current + [num]*i)

    def test(self):
        cases = [
            [],
            [1],
            [1,2,3],
            [1,2,2],
            [1,1,1,1,1],
            [1,1,1,1,2],
            [1,1,1,1,2,2,3],
        ]
        for c in cases:
            res = self.subsetsWithDup(c)
            print(c, res)
            
            
# Solution().test()