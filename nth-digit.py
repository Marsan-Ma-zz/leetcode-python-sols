# https://leetcode.com/problems/nth-digit/

# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).

# Example 1:

# Input:
# 3

# Output:
# 3
# Example 2:

# Input:
# 11

# Output:
# 0

# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. n < 2**31 ~ 1000**3
        # 2. 1-9, 9 numbers, 1 digit per number
        #    10-99, 90 numbers, 2 digit per number
        #    100-999, 900 numbers, 3 digit per number
        #    1000-9999, 9000 numbers, 4 digit per number
        
        
        cnt = 0
        base = 9
        unit = 1
        segments = base * unit
        while n > segments:
            cnt += segments
            n -= segments
            base *= 10
            unit += 1
            segments = base * unit
        
        ans = (base // 9) + ((n - 1) // unit)
        # print(base, unit, ans, n)
        return int(str(ans)[(n - 1) % unit])
        
    def test(self):
        cases = [
            1,
            3,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            189,
            190,
            191,
            192,
            193,
            194,
            195,
        ]
        for c in cases:
            print(c, self.findNthDigit(c))
            
            
# Solution().test()