# https://leetcode.com/problems/one-edit-distance/

# Given two strings S and T, determine if they are both one edit distance apart.

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # [Ideas]
        # 1. compare from both head
        # 2. while 1st different => see if match one of conditions fit 'one edit distance'
        # 3. O(n)
        if not s and not t: return False

        if len(s) < len(t):
            s, t = t, s

        for i, c in enumerate(s):
            if i >= len(t):
                return len(s[i:]) == 1
            if s[i] != t[i]:
                if (s[i+1:] == t[i+1:]) or (s[i+1:] == t[i:]): # or (s[i:] == t[i+1:]):
                    return True
                else:
                    return False
        return False  # s == t


    def test(self):
        cases = [
            ('', ''),
            ('a', ''),
            ('ab', 'b'),
            ('b', 'ab'),
            ('ba', 'ab'),
            ('abbc', 'bbc'),
            ('abbcd', 'bbc'),
            ('bbc', 'abbcd'),
        ]
        for s, t in cases:
            print(s, t, self.isOneEditDistance(s, t))


Solution().test()