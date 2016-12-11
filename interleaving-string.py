# https://leetcode.com/problems/interleaving-string/

# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",

# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.



class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # [Examples]
        # aabcc + dbbca = aadbbcbcac
        # 
        #     _   a   a   b   c   c
        # _    
        # d       0   1   1   0   0
        # b       0   1   1   1   0
        # b
        # c
        # a
        
        
        
        # [Ideas]
        # 1. dp[i][j] = (s3[i+j] == s1[i] and dp[i-1][j]) or 
        #               (s3[i+j] == s2[j] and dp[i][j-1])
        
        if not s1: return s2 == s3
        if not s2: return s1 == s3
        
        m, n = len(s1), len(s2)
        if m+n != len(s3): return False
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == j == 0: continue
                k = s3[i+j-1]
                cond1 = (k == s1[i-1] and dp[i-1][j])
                cond2 = (k == s2[j-1] and dp[i][j-1])
                dp[i][j] = cond1 or cond2
        # print(dp)
        return dp[-1][-1]
                
        
    def test(self):
        cases = [
            ('', '', ''),
            ('', 'a', ''),
            ('', '', 'b'),
            ('a', 'b', 'b'),
            ('db', 'b', 'cbb'),
            ('aabcc', 'dbbca', 'aadbbcbcac'),
            ('aabcc', 'dbbca', 'aadbbbaccc'),
        ]
        for s1, s2, s3 in cases:
            print(s1, s2, s3, self.isInterleave(s1, s2, s3))
            
            
# Solution().test()