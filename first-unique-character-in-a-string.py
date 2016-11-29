# https://leetcode.com/problems/first-unique-character-in-a-string/

# Given a string, find the first non-repeating character in it and 
# return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.



from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return -1
        
        h = [k for k,v in Counter(s).items() if v == 1]
        if not h: return -1
        return min(s.index(v) for v in h)
        
        