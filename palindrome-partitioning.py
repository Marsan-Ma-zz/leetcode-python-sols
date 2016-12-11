# https://leetcode.com/problems/palindrome-partitioning/

# Given a string s, partition s such that every substring of the partition 
# is a palindrome.

# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return

# [
#   ["aa","b"],
#   ["a","a","b"]
# ]


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        sols = []
        def dfs(s, ps):
            if not s:
                sols.append(ps)
            else:
                for i in range(1, len(s)+1):
                    if s[:i] == s[:i][::-1]:
                        dfs(s[i:], ps+[s[:i]])
        dfs(s, [])
        return sols
    
    
    def test(self):
        cases = [
            "",
            "abb",
            "abc",
            "aabbccbba",
        ]
        for c in cases:
            print(c, self.partition(c))
            
            
# Solution().test()