# https://leetcode.com/problems/longest-repeating-character-replacement/

# Given a string that consists of only uppercase English letters, you can replace any 
# letter in the string with another letter at most k times. Find the length of a longest 
# substring containing all repeating letters you can get after performing the above operations.

# Note:
# Both the string's length and k will not exceed 104.

# Example 1:

# Input:
# s = "ABAB", k = 2

# Output:
# 4

# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input:
# s = "AABABBA", k = 1

# Output:
# 4

# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.



class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. 2 pointer, when k items not largest char, 
        #    drop from slower pointer
        
        
        best, ptr = 0, 0
        stat = {}
        for i, c in enumerate(s):
            stat[c] = stat.get(c, 0) + 1
            while sum(sorted(stat.values())[:-1]) > k:
                stat[s[ptr]] -= 1
                ptr += 1
            best = max(best, i-ptr+1)
        return best
            
                