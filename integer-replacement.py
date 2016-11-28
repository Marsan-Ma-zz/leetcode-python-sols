# https://leetcode.com/problems/integer-replacement/

# Given a positive integer n and you can do operations as follow:

# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# What is the minimum number of replacements needed for n to become 1?

# Example 1:

# Input:
# 8

# Output:
# 3

# Explanation:
# 8 -> 4 -> 2 -> 1
# Example 2:

# Input:
# 7

# Output:
# 4

# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {1: 0, 2: 1}  # i = 0, 1, 2
        
        def dfs(i):
            if i in dp: 
                return dp[i]
            if i % 2 == 0:
                dp[i] = dfs(i//2) + 1
            else: 
                dp[i] = min(dfs(i-1), dfs((i+1)//2) + 1) + 1
            return dp[i]
        
        dfs(n)
        # print(dp)
        return dp[n]


    def test(self):
        print(self.integerReplacement(100))


# Solution().test()
