# https://leetcode.com/problems/ones-and-zeroes/

# In the computer world, use restricted resource you have to generate maximum 
# benefit is what we always want to pursue.

# For now, suppose you are a dominator of m 0s and n 1s respectively. On the other 
# hand, there is an array with strings consisting of only 0s and 1s.

# Now your task is to find the maximum number of strings that you can form with given 
# m 0s and n 1s. Each 0 and 1 can be used at most once.

# Note:
# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.
# Example 1:
# Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# Output: 4

# Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
# Example 2:
# Input: Array = {"10", "0", "1"}, m = 1, n = 1
# Output: 2

# Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".



from collections import Counter, defaultdict
class Solution(object):

    # https://discuss.leetcode.com/topic/71587/0-1-knapsack-in-python
    # 1. [transition func]: 
    #   dp(k, x, y) = max(dp(k-1, x-z, y-o) + 1, dp(k-1, x, y))   
    #   where z is zeroes in strs[k], o is ones in strs[k]
    #   dp(len(strs), M, N) is the answer we are looking for
    # 
    # 2. dp(k, x, y) is the maximum strs we can include when we have x zeros, 
    #    y ones and only the first k strs are considered.
    # 3. I first implemented a dfs + memoization, which gets MLE, 
    #    so I created a bottom up style dp.
    #    With bottom up, we can use something called "rolling array" to optimize 
    #    space complexity from O(KMN) to O(MN)

    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')
        
        for z, o in [count(s) for s in strs]:
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x >= z and y >= o:
                        dp[x][y] = max(1 + dp[x-z][y-o], dp[x][y])
        return dp[m][n]


    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # [Examples]
        # 1. {"10", "0001", "111001", "1", "0"}, m = 5, n = 3 
        #    => “10,”0001”,”1”,”0”
        # 2. {"10", "0", "1"}, m = 1, n = 1
        #    => "0" and "1"
        
        # [Ideas]
        # 1. first transfer strs to stat by Counter
        # 2. DFS for all possible combs.
        #    => any prune branch cond?
        #    => dp[(m,n)] for best solution ... X, strs might different
        #    => dp[strs] and use bit mask to represent strs
        # 3. if we always choose leftmost, not possible to repeat,
        #    X. thus no need for DP? no, strings with same char stat would 
        #       be complex, like 11000, 01100 
        # 4. got TLE, but rough idea is correct.
        
        dic = {}
        for s in strs:
            stat = Counter(s)
            key = (stat.get('0',0), stat.get('1',0))
            dic[key] = 1 + dic.get(key, 0)
        ldic = [(k,v) for k,v in dic.items()]
        # print(ldic)
        
        dp = {}
        def dfs(ldic, m, n):
            # DP
            key = tuple([v for k,v in ldic])
            if key in dp: return dp[key]
            # dfs
            best = 0
            for i, (k, v) in enumerate(ldic):
                if k[0] <= m and k[1] <= n and v > 0:
                    # print(k, m, n)
                    ndic = ldic[:]
                    ndic[i] = (k, v-1)
                    sol = 1 + dfs(ndic, m-k[0], n-k[1])
                    best = max(best, sol)
            dp[key] = best
            # print(key, best)
            return best
        
        sol = dfs(ldic, m, n)
        return sol
            
        
        
    def test(self):
        cases = [
            ([], 1, 1),
            # (["10", "1", "0"], 5, 3),
            (["10", "0", "1"], 1, 1),
            (["10", "0001", "111001", "1", "0"], 5, 3),
        ]
        for strs, m, n in cases:
            print(self.findMaxForm(strs, m, n))
            
            
# Solution().test()