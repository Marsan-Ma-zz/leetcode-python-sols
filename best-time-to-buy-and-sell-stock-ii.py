# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Say you have an array for which the ith element is the price of a 
# given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as 
# many transactions as you like (ie, buy one and sell one share of the 
# stock multiple times). However, you may not engage in multiple transactions 
# at the same time (ie, you must sell the stock before you buy again).



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        profit = 0
        low = prices[0]
        for p in prices[1:]:
            if p > low:
                profit += p - low
                low = p
            elif p < low:
                low = p
        return profit            
    