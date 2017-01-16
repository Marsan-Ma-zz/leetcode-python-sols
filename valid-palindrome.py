# https://leetcode.com/problems/valid-palindrome/
# Given a string, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s == '': return True
        if s == None: return False

        s = s = re.sub(r"[^a-z0-9]", '', s.lower())
        p1, p2 = 0, len(s)-1
        while(p1 < p2):
            if s[p1] != s[p2]: 
                return False
            else:
                p1 += 1
                p2 -= 1
        return True


    def test(self):
        cases = [
            '',
            'a',
            'acac',
            'bc b',
            'aba',
            'abba',
            'raceacar',
            'amanaplanacanalpanama',
            "A man, a plan, a canal: Panama",
            "race a car",
            "0123aba3210",
            "0123aba3214",
        ]
        for c in cases:
            print(c, self.isPalindrome(c))


Solution().test()
