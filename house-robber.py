# https://leetcode.com/problems/house-robber/

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # [Ideas]
        # 1. can we only consider local optimum greedily?
        # 2. Ex: nums = [1, 2, 3, 4, 5] 2+4 < 1+3+5
        #        idx  =  0  1  2  3  4
        #       => i=0, rob i0 if i2 > i1
        #       => if last house chosen, give-up this
        #       => loop until end
        # 3. counter ex? => 
        # 4. special ex: [2, 1, 2, 1, 2, 1 ..., 99999]
        #-----------------------------------
        # 1. use recursive to divide problem size
        #    rob(nums) = max(nums[i] + rob(nums[i+2:]), rob(nums[i+1:]))
        #    => will cost O(2**n)
        #    => use dp, so all nums[i:] won't duplicate => O(n)
        
        # boundary cases
        size = len(nums)
        if not size: return 0
        if size <= 2: return max(nums)
            
        # initialize dp table
        self.nums = nums
        self.dp = [-1] * size
        self.dp[size-1] = nums[-1]
        self.dp[size-2] = max(nums[-2:])
        return self.max_rob(0)
    
    
    def max_rob(self, start):
        if self.dp[start] >= 0:
            return self.dp[start]
        else: # len(nums) >= 3
            self.dp[start] = max(
                self.max_rob(start+2) + self.nums[start], 
                self.max_rob(start+1),
            )
            return self.dp[start]
            
        
        
    def test(self):
        cases = [
            [],
            [1,2,3],
            [1,2,3,4,5,4,3,2,1],
            [2,1,2,1,2,1,2,1,100],
            [1,2,1,2,1,2,1,2,100],
            [1000,2,1,2,1,2,1,2,100],
        ]
        for c in cases:
            print(c, self.rob(c))
            
            
            
# Solution().test()