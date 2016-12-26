# https://leetcode.com/problems/combination-sum/

# Given a set of candidate numbers (C) (without duplicates) and a target number (T), 
# find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# [
#   [7],
#   [2, 2, 3]
# ]


# =============================
#   DFS + DP
# =============================
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        # [Ideas]
        # 1. dfs with dp
        # 2. but dp is useless since have to limit midx...
        
        dp = {}
        def helper(t, midx):    # midx (minimum index) to limit duplicated sols
            if t == 0: return [[]]  # key! return [] will all no answer!
            if (t, midx) not in dp: 
                sols = []
                for i in range(midx, len(candidates)):
                    c = candidates[i]
                    if c <= t:
                        sols.extend([[c]+s for s in helper(t-c, i)])
                dp[(t, midx)] = sols
            return dp[(t, midx)]
            
        sols = helper(target, 0)
        return sols
        