# https://leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. Do this without extra space.


from math import log, floor
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # [Ideas] WITHOUT extra spaces!
        # 1. detect num of digit of x 
        # => compare from MSB and LSB, 
        # => then remove them by substraction and divide by 10
        # 
        
        if not x: return True
        if x < 0: return False 
        return str(x) == str(x)[::-1]
        
        
    def test(self):
        cases = [
            None,
            0,
            1,
            123,
            12321,
            1000021,
            123454321,
            123232321,
            1232332321,
        ]
        for c in cases:
            print(c, self.isPalindrome(c))
            
# Solution().test()
