# https://leetcode.com/problems/edit-distance/

# Given two words word1 and word2, find the minimum number of steps required 
# to convert word1 to word2. (each operation is counted as 1 step.)

# You have the following 3 operations permitted on a word:

# a) Insert a character
# b) Delete a character
# c) Replace a character


class Solution(object):
    def minDistance(self, word1, word2):
        m, n = map(len, (word1, word2))
        dp = [list(range(n + 1))] + [[i] + [0] * n for i in range(1, m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(
                    dp[i][j - 1] + 1, # insert from w1
                    dp[i - 1][j] + 1, # insert from w2
                    dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]) # replace if not equal
                )
        # for r in dp: print(r)
        return dp[m][n]
    
    
    def test(self):
        cases = [
            ('abc', 'cbd'),
        ]
        for w1, w2 in cases:
            print(self.minDistance(w1, w2))
            
# Solution().test()