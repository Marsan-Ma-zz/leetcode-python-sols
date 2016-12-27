# https://leetcode.com/problems/permutations-ii/

# Given a collection of numbers that might contain duplicates, 
# return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]



class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # [Ideas]
        # 1. DFS, but problem is how to avoid duplicate
        #    => use set and tuple to collect answers, not the best but work.
        #    => "sort" + "if i > 0 and nums[i] == nums[i-1]" !! like in "combination-sum-ii"
        #    => one char by one char, and guarantee "don't duplicate in this char" for each round!
        
        self.sols = []
        nums.sort()
        
        def dfs(nums, items):
            if not nums:
                self.sols.append(items)
            else:
                for i, n in enumerate(nums):
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    dfs(nums[:i]+nums[i+1:], items+[n])
                
        dfs(nums, [])
        return self.sols
        