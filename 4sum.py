# https://leetcode.com/problems/4sum/

# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if not nums or len(nums) < 4: return []
        nums = sorted(nums)
        
        i, sols = 0, []
        while i < len(nums)-3:
            t = target - nums[i]
            sols += [[nums[i]]+s for s in self.threeSum(nums[i+1:], t)]
            while (i < len(nums)-2) and (t == target - nums[i]): i += 1
        
        return sols
        
        
    def threeSum(self, nums, target):
        i, sols = 0, []
        while i < len(nums)-2:
            t = target - nums[i]
            sols += [[nums[i]]+s for s in self.twoSum(nums[i+1:], t)]
            while (i < len(nums)-2) and (t == target - nums[i]): i += 1
        return sols
        
        
    def twoSum(self, nums, target):
        p1, p2 = 0, len(nums)-1
        sols = []
        while p1 < p2:
            s = nums[p1] + nums[p2]
            if s == target:
                sols += [[nums[p1], nums[p2]]]
                while (p1 < p2) and (s == nums[p1] + nums[p2]): p1 += 1
            elif s > target:
                while (p1 < p2) and (s == nums[p1] + nums[p2]): p2 -= 1
            elif s < target:
                while (p1 < p2) and (s == nums[p1] + nums[p2]): p1 += 1
        # print("2:", nums, target, sols)
        return sols
        
        
    def test(self):
        cases = [
            ([], 3),
            ([1,2,3], 6),
            ([1,2,3,4], 10),
            ([1,2,3,4,5,6,7,8], 15),
            ([1,2,3,4,5,6,7,8], 25),
            ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 3),
            ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 4),
            ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 5),
            ([1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3], 6),
            ([1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3], 9),
            ([1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3], 12),
            ([1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3], 15),
        ]
        for nums, t in cases:
            print(nums, t, self.fourSum(nums, t))
            
            
# Solution().test()