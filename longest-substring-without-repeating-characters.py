# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        current, max_cnt = s[0], 1
        for c in s[1:]:
            if c in current:
                current = current[current.index(c)+1:] + c
            else:
                current += c
            max_cnt = max(max_cnt, len(current))
                
        return max_cnt
        
    def test(self):
        cases = [
            "",
            "abcabcbb",
            "bbbbb",
            "pwwkew",
            "abcdabcdabcd",
            "abcdabcdeabcd",
        ]
        for c in cases:
            print(c, self.lengthOfLongestSubstring(c))
                 
                  
# Solution().test()