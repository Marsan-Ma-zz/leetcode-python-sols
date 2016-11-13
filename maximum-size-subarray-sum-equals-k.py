# # https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

# Given an array nums and a target value k, find the maximum length of a subarray
# that sums to k. If there isn't one, return 0 instead.

# Example 1:
# Given nums = [1, -1, 5, -2, 3], k = 3,
# return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

# Example 2:
# Given nums = [-2, -1, 2, 1], k = 1,
# return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

# Follow Up:
# Can you do it in O(n) time?


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # [Ideas]
        # add up numbers from the leftmost to the rightmost:
        #    memo total_sum and sum until position
        #    use this memo to find if there are better candidate
        
        res_cnt = 0
        memo = {0: -1}
        total_sum = 0
        
        for i, n in enumerate(nums):
            total_sum += n
            
            # since only want the leftmost partial sum
            if total_sum not in memo:
                memo[total_sum] = i
            
            # search for candidate
            trim_out = total_sum - k
            if trim_out in memo:
                cand = i - memo[trim_out]
                if (res_cnt == None) or (cand > res_cnt):
                    res_cnt = cand
                
        # print("memo",memo)
        return res_cnt
    
    
    def test(self):
        cases = [
            ([], 0),
            ([], 2),
            ([1,2,3], 3),
            ([1, -1, 5, -2, 3], 3),
            ([-2, -1, 2, 1], 1),
        ]
        for nums, k in cases:
            res = self.maxSubArrayLen(nums, k)
            print(nums, k, res)
            
            
# Solution().test()