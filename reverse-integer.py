# https://leetcode.com/problems/reverse-integer/

# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

# click to show spoilers.

# Have you thought about this?
# Here are some good questions to ask before coding. Bonus points 
# for you if you have already thought through this!

# If the integer's last digit is 0, what should the output be? 
# ie, cases such as 10, 100.

# Did you notice that the reversed integer might overflow? 
# Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. 
# How should you handle such cases?

# For the purpose of this problem, assume that your function returns 0 
# when the reversed integer overflows.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. deal with sign independently
        # 2. mod by 10 => push result into queue => divide by 10
        #    => then pop, append to ans => multiply 10
        
        if not x: return 0
        
        sign = (x > 0)
        x = abs(x)
        stack = []
        while x:
            stack.append(x % 10)
            x = x // 10
            
        ans = 0
        while stack:
            ans *= 10
            ans += stack.pop(0)
            
        if ans > 2**31: ans = 0  # pretend overflow
        if not sign: ans = -ans
        
        return ans
    
    
    def test(self):
        cases = [
            None,
            0,
            123,
            -1212,
            12341234,
            -12341234,
        ]
        for c in cases:
            print(c, self.reverse(c))
            
            
# Solution().test()