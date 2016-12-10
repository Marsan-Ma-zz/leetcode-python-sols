# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock 
# before you buy again).


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # [Ideas]
        # 1. we know how to solve with 1 transaction only,
        #    just try split into two segment and get max independently,
        #    then find the best combination.
        # 2. we could use DP to get max of prices[:i] from 
        #    prices[:i-1] to save computing.
        # 3. also, prices[i:] from prices[i+1:]
        
        if not prices or len(prices) < 2: return 0
        
        dp1 = [0] * len(prices)
        dp2 = [0] * (len(prices)+1)
        
        low = prices[0]
        for i, p in enumerate(prices):
            if i == 0: continue
            if p < low: low = p
            dp1[i] = max(dp1[i-1], p-low)
            
            
        high = prices[-1]
        for i, p in reversed(list(enumerate(prices))):
            if i == len(prices)-1: continue
            if p > high:
                high = p
            dp2[i] = max(dp2[i+1], high-p)
            
        # print(dp1, dp2)
        return max(dp1[i]+dp2[i+1] for i in range(len(prices)))
            
        
    def test(self):
        cases = [
            # [],
            # [1],
            # [1,2],
            # [1,2,3,4],
            [3,3,5,0,0,3,1,4],
            # [1,2,3,4,3,2,1,2,3,4,5,7],
        ]
        for c in cases:
            print(c, self.maxProfit(c))
            
            
# Solution().test()