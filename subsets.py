# Given a set of distinct integers, nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # [Idea]
        # 1. use a boolean to represent each element (included/excluded).
        #    all solutions correspond to all permutations of this 
        #    "active lists"
        # 2. user recursion to go through all permutations
        if not nums: return []
        
        self.nums = nums            # [1,2,3]
        self.memo = {}

        return self.traverse(0)
    
        
    def traverse(self, idx):
        if idx == len(self.nums)-1:
            return [[], [self.nums[idx]]]
        elif idx in self.memo:
            return self.memo[idx]
        else:
            rests = self.traverse(idx+1)
            self.memo[idx] = rests + [[self.nums[idx]] + r for r in rests]
            return self.memo[idx]
                
                

    def test(self):
        cases = [
            [],
            [4,9],
            [1,2,3],
            [10,3,1,4,5],
        ]
        for c in cases:
            print(c, self.subsets(c))
            
            
            
Solution().test()