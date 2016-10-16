# https://leetcode.com/problems/factorial-trailing-zeroes/

# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. trailing zeroes comes from *10 => * (2*5)
        #    2 must be much more than 5, only search 5
        # 2. every 5, every 10 would have 5
        # 3. n//5 + n//5//5 + n//5//5//5 + ...
        
        cnt = 0
        while n:
            cnt += n // 5
            n = n // 5
            
        return cnt
    
    
    def test(self):
        cases = [
            None,
            0,
            2,
            8,
            10,
            15,
            12,
            20,
        ]
        for c in cases:
            print(c, self.trailingZeroes(c))
            
            
# Solution().test()
        