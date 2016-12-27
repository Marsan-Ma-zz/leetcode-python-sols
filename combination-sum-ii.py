# https://leetcode.com/problems/combination-sum-ii/

# Given a collection of candidate numbers (C) and a target number (T), 
# find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]



class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        # [Ideas]
        # 1. dfs + dp (maybe?)
        # 2. limit available index start from largest among used
        # 3. [TRICKY!!] how to avoid duplicate?
        #    => "sort" and "if i != midx and c == candidates[i-1]"
        
        
        # DFS
        candidates.sort()
        m = len(candidates)
        self.sols = []
        def dfs(target, midx, items):
            if target == 0:
                self.sols.append(items)
            else:
                for i in range(midx, m):
                    c = candidates[i]
                    if i != midx and c == candidates[i-1]:
                        continue  # [KEY to avoid DUPLICATION!!]
                    if c <= target:
                        dfs(target - c, i+1, items+[c])
        
        dfs(target, 0, [])
        return list(self.sols)
        