# https://leetcode.com/problems/shortest-palindrome/

# Given a string S, you are allowed to convert it to a palindrome 
# by adding characters in front of it. Find and return the shortest 
# palindrome you can find by performing this transformation.

# For example:

# Given "aacecaaa", return "aaacecaaa".

# Given "abcd", return "dcbabcd".



class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        r = s[::-1]
        for i in range(len(s)):
            if s.startswith(r[i:]):
                return r[:i] + s
        return r + s
        
        
    def test(self):
        cases = [
            "aacecaaa",
            "abcd",
        ]
        for c in cases:
            print(c, self.shortestPalindrome(c))
            
            
# Solution().test()