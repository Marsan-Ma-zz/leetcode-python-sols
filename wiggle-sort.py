# https://leetcode.com/problems/wiggle-sort/

# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

# For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # [Ideas]
        # 1. key: we don't care global order, only adjust local order.
        # 2. we might come with a O(n) solution which only fix local order
        #    one number by one to the end.
        # 3. target: nums[0] < nums[1] > nums[2] < nums[3]...
        #    => first swap to make nums[0] < nums[1]
        #    => swap if nums[1] <= nums[2], since nums[2] >= nums1 > nums[0]
        #       thus nums[0] < nums[2] > nums[1]
        #    => swap if nums[2] >= nums[3], and nums[3] <= nums[2] < nums[1]
        
        
        for i in range(len(nums)-1):
            if (i % 2 == 0):
                if (nums[i] > nums[i+1]):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    
                    
                    
            if (i % 2 == 1):
                if (nums[i] <= nums[i+1]):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                
        # return nums
                
        
    def test(self):
        cases = [
            [],
            [1, 5, 1, 1, 6, 4],
            [1, 3, 2, 2, 3, 1],
            [2, 2, 2, 1, 1, 1],
        ]
        for c in cases:
            print(c, self.wiggleSort(c))
                
                  
Solution().test()