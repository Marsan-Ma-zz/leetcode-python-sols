# https://leetcode.com/problems/house-robber-ii/

# After robbing those houses on that street, the thief has found himself a new place 
# for his thievery so that he will not get too much attention. This time, all houses 
# at this place are arranged in a circle. That means the first house is the neighbor 
# of the last one. Meanwhile, the security system for these houses remain the same as 
# for those in the previous street.

# Given a list of non-negative integers representing the amount of money of each house, 
# determine the maximum amount of money you can rob tonight without alerting the police.


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # [Ideas]
        # 1. just do house-robber-I twice, 
        #    one without first house,
        #    one without last house.
        
        if len(nums) < 3: return max(nums) if nums else 0
        
        def rob_line(houses):
            # [Ideas]
            # dp[i] = max(dp[i-2] + h[i], dp[i-1])
            last2, last = houses[0], max(houses[:2])
            cur = max(last2, last)
            for m in houses[2:]:
                cur = max(last2+m, last)
                last2, last = last, cur
            return cur
            
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
        