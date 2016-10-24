# https://leetcode.com/problems/divide-two-integers/

# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT.


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        # [Ideas]
        # 0. WITHOUT using multiplication, division and mod operator.
        # 1. only shift instead of *,/ and we still got +,-
        # 2. ALWAYS be ware NEGATIVE NUMBER !!!
        
        
        if not divisor: return 0x7fffffff # as overflow
        
        A, B = abs(dividend), abs(divisor)
        sign = (dividend < 0) ^ (divisor < 0)
        sol, mask = 0, 1
        
        # find start point
        while (B << 1) < A:
                B = B << 1
                mask = mask << 1
                
        while A >= abs(divisor):
            # subtract the most B out of A
            while B > A:
                B = B >> 1
                mask = mask >> 1
            # accumulate answer
            A -= B
            sol += mask
        
        if sign: sol = -sol
        if (sol >= 0x7fffffff) or (sol < -0x7fffffff-1): 
            return 0x7fffffff
        return sol
    
    def test(self):
        cases = [
            (0, 0),
            (1, 0),
            (1, 2),
            (10, 2),
            (123, 3),
            (123, 4),
            #--------
            (-1, 0),
            (1, -1),
            (-10, 2),
            (30, -4),
        ]
        for a, b in cases:
            print(a, b, self.divide(a, b))
            
            
# Solution().test()
# print(-0x7fffffff-1)