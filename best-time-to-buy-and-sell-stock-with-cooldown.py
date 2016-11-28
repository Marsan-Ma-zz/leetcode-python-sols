# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# Say you have an array for which the ith element is the price of a 
# given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as 
# many transactions as you like (ie, buy one and sell one share of the 
# stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. 
# (ie, cooldown 1 day)

# Example:

# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]


class Solution(object):

    # [Ideas]
    # 3 status: free, have, cooldown
    # [current -> action -> next]
    #        buy  sell  wait
    # free  have     x  free
    # have     x  cool  have
    # cool     x     x  free


    # [next state]
    # free = max(free, cool)
    # have = max(free-p, have)
    # cool = have+p

    def maxProfit(self, prices):
        if not prices: return 0
        free, have, cool = (0, -prices[0], 0)
        for p in prices[1:]:
            free, have, cool = max(free, cool), max(free-p, have), have+p
        return max(free, have, cool)


    def test(self):
        cases = [
            [],
            [1],
            [1,2,3,4],
            [1,2,3,8,16,8,4,2,1],
            [1,2,3,2,3,4,3,4,5],
        ]
        for c in cases:
            print(c, self.maxProfit(c))

# Solution().test()