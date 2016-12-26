# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

# Find the length of the longest substring T of a given string 
# (consists of lowercase letters only) such that every character in T appears no less than k times.

# Example 1:

# Input:
# s = "aaabb", k = 3

# Output:
# 3

# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input:
# s = "ababbc", k = 2

# Output:
# 5

# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.




from collections import Counter
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. stat s, split s with chars total number < k times.
        # 2. recursive to splitted substrings => O(nlog(n))
        #---------------------------
        # 1. one-pass traverse:
        #    => update best only when all chars freq qualified
        #    => how to decide abandom or not? X
        
        if not s: return 0
        rares = [c for c,v in Counter(s).items() if v < k]
        if not rares: return len(s)
        s = ''.join([c if c not in rares else ' ' for c in s])
        return max(self.longestSubstring(sub, k) for sub in s.split() or [0])
        