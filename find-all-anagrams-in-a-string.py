# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Given a string s and a non-empty string p, find all the start 
# indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length 
# of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # [Ideas]
        # 1. use two pointer and a hash to remember characters
        #    of current checking window
        
        sols, lp = [], len(p)
        cnt1, cnt2 = Counter(p), Counter(s[:lp])
        if cnt1 == cnt2: sols.append(0)
        
        for i in range(lp, len(s)):
            j = i - lp
            cnt2[s[j]] -= 1
            cnt2[s[i]] += 1
            if set((k,v) for k, v in cnt1.items() if v) == set((k,v) for k, v in cnt2.items() if v):
                sols.append(j+1)
            
        return sols
        
