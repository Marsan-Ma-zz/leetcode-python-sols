# https://leetcode.com/problems/count-numbers-with-unique-digits/

# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. permutanio of 0-9 and 0 can be MSB
        # 2. 0 digit: 1
        #    1 digit: 9 + (0 digit)
        #    2 digit: 9*9 + (1 digit)
        #    3 digit: 9*9*8 + (2 digits)
        #    4 digit: 9*9*8*7 + (3 digits)
        #    n digit: 9*9! + (ans of n-1 digit)
        
        dp = [1]
        for i in range(1, n+1):
            dp.append(9)
            for j in range(11-i,10):
                dp[i] *= j
            dp[i] += dp[i-1]
        return dp[n]
    
    
    def test(self):
        cases = [
            0,
            1,
            2,
            3,
            4,
            5,
        ]
        for c in cases:
            print(c, self.countNumbersWithUniqueDigits(c))
            
# Solution().test()
# print(9*9*8*7 + 739)