# https://leetcode.com/problems/find-peak-element/

# A peak element is an element that is greater than its neighbors.

# Given an input array where num[i] ≠ num[i+1], find a peak element 
# and return its index.

# The array may contain multiple peaks, in that case return the index 
# to any one of the peaks is fine.

# You may imagine that num[-1] = num[n] = -∞.

# For example, in array [1, 2, 3, 1], 3 is a peak element and your function 
# should return the index number 2.



class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # boundary case
        if (not nums) | (len(nums) == 1): return 0
        
        # for convenience
        nums = [nums[0]-1] + nums + [nums[-1]-1]
        
        # binary search
        lptr = 0
        rptr = len(nums)-1
        while True:
            ptr = (lptr+rptr)//2
            l,m,r = nums[ptr-1], nums[ptr], nums[ptr+1]
            if (l < m):
                if (m > r):  # /\
                    return ptr-1
                else:  # //
                    lptr = ptr
            if (l > m):  # \\ or \/
                rptr = ptr

                