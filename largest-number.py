# https://leetcode.com/problems/largest-number/

# Given a list of non negative integers, arrange them such that they form the largest number.

# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.


# [3, 30, 34, 31, 32, 312, 345, 334] => 345, 
# [3, 32, 33, 34, 334]
# 1. compare 2nd MSB?  => what if no 2nd MSB ones?
# 2. for no 2nd MSB ones, append trailing same number?
#    => [333, 323, 333, 343, 334] 
#    => brute force: compare each pair combination
#       3+32, 3+33, 3+34, 3+334, 32+3, 32+33, 32+34, 32+334, ...

from functools import cmp_to_key

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        
        # [Ideas]
        # 1. n with largest MSB should be the MSB
        # 2. same with the rest numbers, thus just do it recursively
        # X. for same MSB: process them with 2nd MSB, recursively
        #    for number without 2nd MSB, pad with itself
        # X. use padded to solve 2nd/3nd...MSB instead, much easier.
        # -------------------------------------
        # OMG... it's a overwrited comparator and use it to sort!
        
        if not nums: return ''
        
        def comparator(x, y):
            # print("cmp:", x, y)
            x, y = str(x), str(y)
            s1, s2 = x + y, y + x
            if s1 > s2:
                return -1
            elif s1 < s2:
                return 1
            else:
                return 0
            
        # sol = sorted(nums, cmp=comparator)
        nums = sorted(nums, key=cmp_to_key(comparator))
        nums = "".join([str(n) for n in nums])
        return nums.lstrip('0') or '0'
    
        
    def test(self):
        cases = [
            [],
            [0, 0],
            [0, 1],
            [0, 1, 0],
            [12, 1214], # 14 > 12
            [121, 12], # 121,12 < 12,121
            [191, 19], # 191,19 < 19,191
            [515, 51], # 515,51 > 51,515
            [554, 55], # 554,55 < 55,554
            [1,2,3],
            [1,2,3,100],
            [3, 30, 34, 5, 9],
            [3, 30, 34, 5, 9, 321, 123,231,213],
        ]
        for c in cases:
            print(c, self.largestNumber(c))
            
            
# Solution().test()
