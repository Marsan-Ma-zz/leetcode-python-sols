# https://leetcode.com/problems/repeated-substring-pattern/

# Given a non-empty string check if it can be constructed by taking 
# a substring of it and appending multiple copies of the substring together. 
# You may assume the given string consists of lowercase English letters only 
# and its length will not exceed 10000.

# Example 1:
# Input: "abab"

# Output: True

# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"

# Output: False
# Example 3:
# Input: "abcabcabcabc"

# Output: True

# Explanation: It's the substring "abc" four times. 
# (And the substring "abcabc" twice.)



from collections import Counter

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        
        # [Examples]
        # 1. 'aabbbaabbbaabbb' => {'a':6, 'b':9}
        # 2. could be {'a':60, 'b':90} and one unit use {'a':20, 'b':30}
        #    while GCD is 15, imply {'a': 4, 'b':6} is minimum unit
        #    so check from head and finally find 5*{'a': 4, 'b':6} is unit.
        
        # [Ideas]
        # 1. one-pass stat the char appear counts, find chars 
        #    composing one-unit segment
        # 2. start from head, traverse until one-unit found, then see 
        #    if rest of string could be composed by same segment
        # 3. find GCD of stat values,
        #------------------------------------------------
        # 1. finding minimum unit candidate cost O(n)
        # 2. knowing the minimum unit length M, try str[:M] == str[M:2*M]
        #    if not, double length M = 2*M, 3*M
        #------------------------------------------------
        # 1. just try do divide by 2, 3, 4 ... N/2
        
        if not str: return True
        if len(str) == 1: return False
        
        k, l = 1, len(str)
        
        while k <= l // 2:
            if l % k == 0:
                unit = str[:k]
                for i in range(1, l//k):
                    if str[k*i: k*(i+1)] != unit:
                        break
                    if i+1 == l // k:
                        return True
            k += 1
        return False
        
        
    def test(self):
        cases = [
            '',
            'a',
            'ab',
            'bb',
            'bbbbb',
            'bbbbba',
            'abab',
            'aba',
            'ababa',
            'abcabcabcabc',
            'abcabcabcabcd',
            'abc'*100,
        ]
        for c in cases:
            print(c, self.repeatedSubstringPattern(c))
            
            
# Solution().test()