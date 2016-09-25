# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

# Show Company Tags
# Show Tags
# Show Similar Problems

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        1. use two pointer: one for place for insert, one for checking
        
        nums = [1,1,2,2,2,3,4,5,5,5]
        """
        # boundary case
        if len(nums) == 0: return 0
        
        # 1 pass scan, O(n) time complexity
        ptr = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[ptr-1]:
                nums[ptr] = nums[i]
                ptr += 1
        # print(ptr, nums)
        return ptr