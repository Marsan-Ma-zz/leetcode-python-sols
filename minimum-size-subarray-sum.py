# https://leetcode.com/problems/minimum-size-subarray-sum/

# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.

# click to show more practice.


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        
        Ex: [2,3,1,2,4,3] and s = 9, ans = [4,3]
        
        1. use two-pointer, if sum >= s, forward lptr, if sum < s, forward rptr. 
           record and return the minimum (rptr-lptr).  time complexity: O(n)
          
        """
        # 1 pass scan 
        lptr, rptr = 0, 0
        sum = 0
        ans = 0                                      #   0,1, 2,3, 4,5, 6, 7, 8
        for n in nums:                               # [10,6,35,2,56,4,33,56,99]
            rptr += 1                                #  10   54  112
            sum += n                                 #  rptr=5, lptr=0, sum=113 
            while sum >= s:                          #  rptr=5, lptr=1, sum=103 
                length = rptr - lptr                 #  rptr=5, lptr=2, sum= 97
                if (ans == 0) or (length < ans):     #  rptr=6, lptr=2, sum=130
                    ans = length                     #  rptr=6, lptr=3, sum= 95
                # release                            #  rptr=7, lptr=3, sum=151
                sum -= nums[lptr]                    #  rptr=7, lptr=4, sum=149
                lptr += 1                            #  rptr=7, lptr=5, sum= 93
                                                     #  rptr=8, lptr=5, sum=192
                                                     #  rptr=8, lptr=6, sum=188
                                                     #  rptr=8, lptr=7, sum=155 <=[ans]
                                                     #  rptr=8, lptr=8, sum= 99
        return ans
                