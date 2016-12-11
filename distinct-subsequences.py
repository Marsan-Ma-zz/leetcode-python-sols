# https://leetcode.com/problems/distinct-subsequences/

# Given a string S and a string T, count the number of distinct subsequences of T in S.

# A subsequence of a string is a new string which is formed from the original string 
# by deleting some (can be none) of the characters without disturbing the relative 
# positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# Here is an example:
# S = "rabbbit", T = "rabbit"

# Return 3.


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        # [Examples]
        # S = "rabbbit", T = "rabbit"
        #
        #  i\j r   a   b   b   i   t
        #   r  1   0   0   0   0   0
        #   a  1   1   0   0   0   0
        #   b  1   1   1   0   0   0
        #   b  1   1   2   1   0   0
        #   b  1   1   3   3   0   0
        #   i  1   1   3   3   3   0
        #   t  1   1   3   3   3   3
        
        # [Ideas]
        # 1. looks like yet another string comparison char-by-char
        #    DP with O(m*n) time and O(m*n) space, maybe O(m) space
        # 2. invariant: dp[m][n] = dp[m-1][n] + dp[m-1][n-1]
        # 3. we could use only 1 row of dp, have to implement CAREFULLY!
        
        if not s or not t: return 0
        
        m, n = len(s), len(t)
        dp = [0]*m
        
        # first column
        dp[0] = int(s[0] == t[0])
        for i in range(1, m):
            dp[i] = dp[i-1]+(s[i] == t[0])
        # print(dp)
        
        # rest table
        for j in range(1, n):
            last = 0
            for i in range(1, m):
                # print(j, i, last, dp[i-1])
                if s[i] == t[j]:
                    cur = last + dp[i-1]
                else: 
                    cur = last
                dp[i-1], last = last, cur
            dp[i] = cur
            # print(dp)
        return dp[-1]
    
    
    def test(self):
        cases = [
            ("", ""),
            ("rabbbit", "rabbit"),
            ('abcde', 'ace'),
        ]
        for s, t in cases:
            print(s, t, self.numDistinct(s, t))
            
# Solution().test()