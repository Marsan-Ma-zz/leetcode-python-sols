# https://leetcode.com/problems/add-strings/

# Given two non-negative numbers num1 and num2 represented as string, 
# return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs 
# to integer directly.



class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        if len(num1) < len(num2):
            num1, num2 = num2, num1
            
        if not num1: return 0
        
        ci = 0
        sol = ''
        len1, len2 = len(num1)-1, len(num2)-1
        for i in range(len1+1):
            if i <= len2:
                s = int(num2[len2-i]) + int(num1[len1-i]) + ci
            else:
                s = int(num1[len1-i]) + ci
            ci = 1 if s >= 10 else 0
            sol = str(s % 10) + sol
        if ci:
            sol = '1' + sol
        return sol
            
            
    def test(self):
        cases = [
            ('', ''),
            ('123', '456'),
            ('789', '222'),
            ('7788', '2222'),
            ('12345', '654321'),
        ]
        for n1, n2 in cases:
            print(n1, n2, self.addStrings(n1, n2))
            
# Solution().test()
            
            
            
            