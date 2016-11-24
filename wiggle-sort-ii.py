# https://leetcode.com/problems/wiggle-sort-ii/

# Given an unsorted array nums, reorder it such that 
# nums[0] < nums[1] > nums[2] < nums[3]....

# Example:
# (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
# (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

# Note:
# You may assume all input has valid answer.

# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?




class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # [Ideas]
        # 1. the key is to deal with continuous equal case, 
        #    like [2,2,2,2,3,3,3,3]
        # 2. can we get medium within O(n) time? thus we could 
        #    arrange them into odd/even with smaller/larger than median
        #    => like quick sort, but each time only care half of them 
        #       in next round
        #    => after medium found, put smaller ones in odd, larger ones
        #       in even index positions to achieve
        #       nums[0] < nums[1] > nums[2] < nums[3]...
        #----------------------------------
        # the O(n) algorithm for find medium is too complicated,
        # here we sort them.

        nums.sort()
        # [NO], think the length of nums[::2]
        # half = len(nums)//2  
        half = len(nums[::2])
        
        # [No] for the case that medium is duplocates: [4,5,5,6]
        # nums[::2], nums[1::2] = nums[:half:1], nums[half::1]  
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        
        
    def test(self):
        cases = [
            [],
            [1,4,2,3,5,7],
            [9,8,7,6,5,4,3,2,1],
            [2,2,2,2,3,3,3,3],
            [2,2,2,2,3,3,3,3,2],
            [2,2,2,2,3,3,3,3,3],
            [4,5,5,6],
        ]
        for c in cases:
            self.wiggleSort(c)
            print(c)
        
        
# Solution().test()