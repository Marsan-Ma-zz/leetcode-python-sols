# https://leetcode.com/problems/coin-change/

# You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)

# Example 2:
# coins = [2], amount = 3
# return -1.

# Note:
# You may assume that you have an infinite number of each kind of coin.



from collections import deque

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # [Examples]
        # 1. coins = [1, 2, 5], amount = 11 => return 3 (11 = 5 + 5 + 1)
        # 2. coins = [2], amount = 3 => return -1.
        
        # [Ideas]
        # 1. DP + recursion from top
        # TLE. for this case, dfs waste time traverse 1+1+1... case.
        #----------------------------------
        # 1. BFS will achieve target faster with using larger coins case!
        
        
        # BFS solution (fast!)
        q = deque([amount])
        step, visited = 0, set()
        while q:
            step += 1
            for i in range(len(q)): # trick to ctrl batch, per step 
                amt = q.popleft()
                if amt == 0: return step - 1
                # prune branch
                if amt in visited: continue
                visited.add(amt)
                # move forward
                q.extend(amt-c for c in coins if amt-c >= 0)
        return -1
                
        
        
        # # DFS solution (slow...)
        # dp = {c: 1 for c in coins}
        # dp[0] = 0
        # def dfs(amount):
        #     if amount in dp: 
        #         return dp[amount]
        #     else:
        #         cands = [1+dfs(amount-c) for c in coins if amount >= c]
        #         cands = [c for c in cands if c > 0] # remove -1 cases
        #         dp[amount] = min(cands) if cands else -1
        #         return dp[amount]
        # return dfs(amount)
        
    
    def test(self):
        cases = [
            # ([], 3),
            # ([1], 3),
            # ([1], 0),
            # ([2,5], 11),
            # ([1,2,5], 11),
            # ([1,2,5], 110),
            # ([2], 3),
            ([27,398,90,323,454,413,70,315], 6131),
        ]
        for c, a in cases:
            print(c, a, self.coinChange(c, a))
            
Solution().test()