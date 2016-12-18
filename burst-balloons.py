# https://leetcode.com/problems/burst-balloons/

# Given n balloons, indexed from 0 to n-1. Each balloon is painted with 
# a number on it represented by array nums. You are asked to burst all 
# the balloons. If the you burst balloon i you will get 
# nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent 
# indices of i. After the burst, the left and right then becomes adjacent.

# Find the maximum coins you can collect by bursting the balloons wisely.

# Note: 
# (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# (2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

# Example:

# Given [3, 1, 5, 8]

# Return 167

#     nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#    coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167



class Solution(object):
    
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # [Ideas]
        # 1. for continuous segment from m to n, suppose "last burst" is i
        #    (or, imagine we are "creating" rather than "burst" baloon)
        #    then dp[m][n] = dp[m][i-1] + dp[i+1][n] + m*i*n
        #    Note: we do NOT burst m and n in this segment
        #    and we always keep boundary, and the outermost boundary is
        #    the two extra '1's, and we don't burst them.
        # 2. to save all pairs of ans(start, end) need O(n**2) space
        # 3. worry ballon with '0' value? just burst them first!
        
        dp = {}
        nums = [n for n in nums if n > 0]    # remove 0 values
        if not nums: return 0
        nums = [1] + nums + [1]
        
        def max_coins(m, n):
            # print(m, n)
            if (m, n) in dp: 
                return dp[(m, n)]
            elif n == m+1:
                return 0
            
            best = 0
            for i in range(m+1, n):
                boom = nums[m]*nums[i]*nums[n]
                sol = max_coins(m, i) + boom + max_coins(i, n)
                best = max(best, sol)
            dp[(m, n)] = best
            return best
        
        return max_coins(0, len(nums)-1)
    
    
    def test(self):
        cases = [
            [],
            [10],
            [5, 9],
            [3,1,5,8], # 167
        ]
        for c in cases:
            print(c, self.maxCoins(c))
            
            
# Solution().test()