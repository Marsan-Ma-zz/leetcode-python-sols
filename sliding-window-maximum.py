# https://leetcode.com/problems/sliding-window-maximum/

# Given an array nums, there is a sliding window of size k which is moving 
# from the very left of the array to the very right. You can only see the 
# k numbers in the window. Each time the sliding window moves right by one position.

# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].

# Note: 
# You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty 
# array.

# Follow up:
# Could you solve it in linear time?





class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # [Ideas]
        # 1. at any moment, pop everything smaller than new num
        #    since they can't be max
        # 2. so max should always in queue[0]
        
        if not nums: return []
        
        q, res = [], []
        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            while q and q[0] <= i-k:
                q.pop(0)
            q.append(i)
            res.append(nums[q[0]])
        return res[k-1:]
    
    
    def test(self):
        cases = [
            ([], 3),
            ([1], 3),
            ([4, -2], 2),
            ([1,2,3,4,5], 3),
            ([1,3,-1,-3,5,3,6,7], 3),
            ([1,3,-1,-3,5,4,4,4,4,3,6,7], 3),
            ([1,2,3,2,1,2,3,2,1,2,3,2,1,2,3,2,1], 3),
        ]
        for nums, k in cases:
            print(self.maxSlidingWindow(nums, k))
            
            
# Solution().test()