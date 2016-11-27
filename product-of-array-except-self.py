# https://leetcode.com/problems/product-of-array-except-self/

# Given an array of n integers where n > 1, nums, return an array 
# output such that output[i] is equal to the product of all the 
# elements of nums except nums[i].

# Solve it without division and in O(n).

# For example, given [1,2,3,4], return [24,12,8,6].

# Follow up:
# Could you solve it with constant space complexity? 
# (Note: The output array does not count as extra space for the purpose 
#     of space complexity analysis.)




# multiply toward right, then toward left
#       1   1    1      1
# ->        1   1*2   1*2*3 
# <-  2*3*4 3*4   4

class Solution:
    
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output



class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
   
   idx: 0 1 2 3
   val: 1 2 3 4
        -------
          1 1 1
        2   2 2
        3 3   3
        4 4 4
        -------
          1 1 1
            2 2
          2   3
          3 3
        ->4 4 4
        -------
        
        """
        l = len(nums)
        res = [1] * l
        
        # upper triangle
        for i in range(1,l):
            res[i] = nums[i-1] * res[i-1]
        # print(res)
        
        # lower triangle
        for i in reversed(range(1,l-1)):  # (l-1), ... 2
            nums[i] *= nums[i+1]
        # print(nums)
        
        # merge
        for i in range(l-1):
            res[i] *= nums[i+1]
        # print(res)
        
        return res
        
        