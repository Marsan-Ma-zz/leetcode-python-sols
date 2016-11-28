# https://leetcode.com/problems/palindrome-permutation/

# Given a string, determine if a permutation of the string could form a palindrome.

# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counts = set()
        for c in s:
            if c in counts:
                counts.remove(c)
            else:
                counts.add(c)
        return (len(counts) <= 1);
