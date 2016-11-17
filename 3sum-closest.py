# https://leetcode.com/problems/3sum-closest/

# Given an array S of n integers, find three integers in S such that 
# the sum is closest to a given number, target. Return the sum of the 
# three integers. You may assume that each input would have exactly one solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.

#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).



class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # [Examples]
        # S = {-1 2 1 -4}, and target = 1. 
        # The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
        
        # [Ideas]
        # 1. for 3sum, fix 1st and deal the rest as 2sum
        # 2. do the same, remember the best sol. => O(n**2)
        
        if not nums or len(nums) < 3: return 0
        
        nums = sorted(nums)
        best = sum(nums[:3])
        loss = abs(target - best)
        for i, n1 in enumerate(nums[:-2]):
            t = target - n1
            p1, p2 = i+1, len(nums)-1
            while p1 < p2:
                psum = nums[p1] + nums[p2]
                ploss = abs(psum - t)
                if ploss < loss:
                    best, loss = n1 + psum, ploss
                # print(p1, p2, psum, loss, best)
                if psum == t:
                    return target
                elif psum > t:
                    p2 -= 1
                else: # psum < t
                    p1 += 1
        return best
    
    
    def test(self):
        cases = [
            ([], 3),
            ([1,2], 3),
            ([1,4,7,10], 10),
            ([-1,2,1,-4], 1),
            ([-4,-1,1,2], 1),
            ([-10,-5, 0, 5, 10], 3),
            ([-10,-5, 0, 5, 10], 5),
            ([-10,-5, 0, 5, 10], 8),
            ([-10,-5, 0, 5, 10], 12),
            ([-10,-5, 0, 5, 10], 20),
        ]
        for nums, t in cases:
            print(nums, t, self.threeSumClosest(nums, t))
                    
                    
# Solution().test()
            