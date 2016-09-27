# https://leetcode.com/problems/plus-one/

# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        if not digits: return None
        
        
        l = len(digits)
        ci = 0
        for i in range(l):
            s = digits[l-i-1] + (1 if i == 0 else ci)
            digits[l-i-1] = s % 10
            ci = s // 10
        if ci:
            digits = [1] + digits
        return digits
    
    def test(self):
        cases = [
            [],
            [0],
            [5],
            [9],
            [1,2,3],
            [1,2,9],
            [1,9,9],
            [9,9,9],
        ]
        for c in cases:
            print(c, self.plusOne(c))
            
            
# Solution().test()            