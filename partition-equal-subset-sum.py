# https://leetcode.com/problems/partition-equal-subset-sum/

# Given a non-empty array containing only positive integers, 
# find if the array can be partitioned into two subsets such that the sum of elements 
# in both subsets is equal.

# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# Example 1:

# Input: [1, 5, 11, 5]

# Output: true

# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: [1, 2, 3, 5]

# Output: false

# Explanation: The array cannot be partitioned into equal sum subsets.


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # [Ideas]
        # 1. target is v = sum(nums)/2
        # 2. it's 0/1 knapsack problem ... DP!
        #    (http://love-oriented.com/pack/P01.html)
        #    with i=0-n item, quota from 0-v
        #    dp[i][v] = max(dp[i-1][v], dp[i-1][v-wi] + wi)
        #    explain: best choice of ith item is :
        #    => not choose, remain choice until i-1
        #    => choose, update from i-1 item with v-ith_weight quota
        # 3. memory could be saved for item dimention, to be only dp[v]
        #    => beware, v loop should be reversed to avoid overwrite 
        #       parameters to use!
        
        # get target
        vol = sum(nums)
        if vol % 2 == 1: return False
        vol = vol // 2
        
        # dp
        dp = [0 for _ in range(vol+1)]
        for n in nums:
            for v in range(vol, 0, -1):
                if v >= n:
                    dp[v] = max(dp[v], dp[v-n]+n)
            # print(dp)
        return dp[vol] == vol
        
    
    # another brute-force sol
    class Solution(object):
        def canPartition(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            possible_sums = {0}
            for n in nums:
                possible_sums.update({(v + n) for v in possible_sums})
            return (sum(nums) / 2.)  in possible_sums  

