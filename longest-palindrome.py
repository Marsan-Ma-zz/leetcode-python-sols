# https://leetcode.com/problems/longest-palindrome/

# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.


from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # [Examples]
        # abccccdd => dccaccd
        
        # [Ideas]
        # 1. count for each items
        # 2. longest palindrome composed of all even count items and 
        #    at most one odd count item
        
        if not s: return 0
        
        has_odd, sol_cnt = False, 0
        raw = Counter(s).items()
        # print(raw)
        for k, v in raw:
            if v % 2 == 1:
                has_odd = True
            sol_cnt += (v // 2)*2
            
        if has_odd:
            sol_cnt += 1
            
        return sol_cnt
    
    def test(self):
        cases = [
            '',
            'abc',
            'abcb',
            'abcbabcba',
            'abccccdd',
        ]
        for c in cases:
            print(c, self.longestPalindrome(c))
            
            
# Solution().test()