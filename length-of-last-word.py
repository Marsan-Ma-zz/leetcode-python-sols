# https://leetcode.com/problems/length-of-last-word/

# Given a string s consists of upper/lower-case alphabets and empty space 
# characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# For example, 
# Given s = "Hello World",
# return 5.


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or not s.strip(): return 0
        return len([w for w in s.split() if len(w) > 0][-1])