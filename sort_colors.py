# https://leetcode.com/problems/sort-colors/
# Given an array with n objects colored red, white or blue, 
# sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # [Ideas]
        # 1. one pass go through all objects, if red, cast to the left, if right, cast to the right
        # 2. use two pointer to memo rightmost red(0) and leftmost blue(2)
        # 3. one more pointer for current checking object
        # -----
        # 4. a more easy way, count all the category, overwrite the nums.

        # boundary cases
        if not nums: return nums

        ptr, ptr1, ptr2 = 0, 0, len(nums)-1
        while ptr < ptr2:
            if nums[ptr] == 0:
                nums[ptr1], nums[ptr] = nums[ptr], nums[ptr1]   # swap
                while (nums[ptr1] == 0) and (ptr1 < ptr2): ptr1 += 1
                ptr = max(ptr, ptr1)
            elif nums[ptr] == 2:
                nums[ptr2], nums[ptr] = nums[ptr], nums[ptr2]   # swap
                while (nums[ptr2] == 2) and (ptr1 < ptr2): ptr2 -= 1
            else:
                ptr += 1
        if nums[ptr] == 0:
            nums[ptr1], nums[ptr] = nums[ptr], nums[ptr1]

    def test(self):
        cases = [
            [],
            [0],
            [1],
            [2],
            [1,0],
            [2,1],
            [1,2,0],
            [0,2,1],
            [1,2,0,2,1,0],
            [1,2,0,2,1,0,1,1,0,2,2,0],
        ]
        for c in cases:
            print(c)
            self.sortColors(c)
            print(c)

# Solution().test()


# [1, 2, 0, 2, 1, 0, 1, 1, 0, 2, 2, 0] 
# [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2] 
#  ^                       ^        
    
# [0, 0, 0, 2, 1, 0, 1, 1, 2, 2, 2, 2] 
#           ^              |  ^