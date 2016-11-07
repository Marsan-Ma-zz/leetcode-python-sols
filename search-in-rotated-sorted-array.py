# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.



from bisect import bisect

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. find the pivot point by binary search. 
        #    then find in left/right part, bisect in that sorted part.
        #    in O(log(n))
        
        if not nums: return -1
        if len(nums) == 1: return 0 if (nums[0] == target) else -1
        
        # search for pivot point
        p1, p2 = 0, len(nums)-1
        while p1 < p2:
            ptr = p1 + (p2 - p1) // 2
            if nums[ptr] >= nums[0]:
                p1 = ptr + 1
            else:
                p2 = ptr - 1
                
        pivot = p1 if nums[p1] >= nums[0] else p1-1
        
        if target >= nums[0]:
            sub_nums = nums[:pivot+1]
        else:
            sub_nums = nums[pivot+1:]
        
        if not sub_nums: return -1
        res = bisect(sub_nums, target)
        # print(sub_nums, target, pivot, res)
        if res > len(sub_nums) or sub_nums[res-1] != target:
            return -1
        else:
            res = res if target >= nums[0] else res + (pivot + 1)
            return res - 1
        
        
    def test(self):
        cases = [
            ([], 3),
            ([1], 1),
            ([2, 1], 1),
            ([1, 2], 1),
            ([1, 2], 2),
            ([1, 3, 5], 0),
            ([1, 3, 5], 7),
            ([1, 3, 5], 2),
            ([5, 1, 3], 1),
            ([1, 2, 3, 4], 1),
            ([1, 2, 3, 4], 4),
            ([4, 5, 6, 7, 0, 1, 2], -1),
            ([4, 5, 6, 7, 0, 1, 2], 4),
            ([4, 5, 6, 7, 0, 1, 2], 5),
            ([4, 5, 6, 7, 0, 1, 2], 6),
            ([4, 5, 6, 7, 0, 1, 2], 7),
            ([4, 5, 6, 7, 0, 1, 2], 0),
            ([4, 5, 6, 7, 0, 1, 2], 1),
            ([4, 5, 6, 7, 0, 1, 2], 2),
            ([4, 5, 6, 7, 0, 1, 2], 3),
        ]
        for nums, target in cases:
            print(nums, target, self.search(nums, target))
            
# Solution().test()
        