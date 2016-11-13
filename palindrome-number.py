# https://leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. Do this without extra space.



from math import log, floor
class Solution(object):
    def isPalindrome(self, x):
        if abs(x) > 0x7FFFFFFF:
            return False
        elif x < 0:
            return False

        exp = 1
        while x / (10 ** exp) != 0:
            exp += 1
        exp -= 1

        while exp > 0:
            if x / (10 ** exp) != x % 10:
                return False
            x = x % (10 ** exp)
            x = x / 10
            exp -= 2
        return True
        
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
