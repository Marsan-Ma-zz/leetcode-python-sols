# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# Say you have an array for which the ith element is the price of a given 
# stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most 
# k transactions.

# Note:
# You may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        # [Ideas]
        # 0. if k if large enough to cover all ramps, this fall-back to 
        #    infinite-transaction problem.
        # 1. use FSM idea from (https://discuss.leetcode.com/topic/5934/)
        #    we have buy[i], sell[i] where i = 1 to k,
        #    means "suppose we are buying/selling i'th time currently"
        #    => it's O(n*k) since one-pass, update k states per step.
         
        # [FSM]
        #-------------------------------------
        # price    p1       p2             p3                p4
        # buy_1    -p1  max(-p1, -p2)      ...               ...
        # sell_1            p2-p1      p3-max(-p1, -p2)      ...
        # buy_2                         -p1+p2-p3            ...
        # sell_2                                        -p1+p2-p3+p4
        # ....
        #-------------------------------------
        # O(k*n/2) time and O(k) space

        if not prices: return 0

        # large k, fallback
        if k > len(prices)//2:
            return sum(p2 - p1 for p1, p2 in zip(prices, prices[1:]) if p2 > p1)
        
        # FSM
        hold = [-float('inf')]*(k+1)
        sell = [0]*(k+1)
        for p in prices:
            for i in range(1, k+1):
                sell[i] = max(sell[i], hold[i]+p)
                hold[i] = max(hold[i], sell[i-1]-p)
        # print(hold, sell)
        return sell[k]
    
    
    def test(self):
        cases = [
            # ([], 3),
            ([3,3,5,0,0,3,1,4], 3),
        ]
        for ps, k in cases:
            print(ps, k, self.maxProfit(k, ps))
        
# Solution().test()

#-----------------------------------------------------------------
# [A better solution in O(n+k*log(n))]
# (https://discuss.leetcode.com/topic/9522/c-solution-with-o-n-klgn-time-using-max-heap-and-stack)
#-----------------------------------------------------------------
# We can find all adjacent valley/peak pairs and calculate the profits easily. 
# Instead of accumulating all these profits like Buy&Sell Stock II, we need the highest k ones.

# The key point is when there are two v/p pairs (v1, p1) and (v2, p2), 
# satisfying v1 <= v2 and p1 <= p2, we can either make one transaction at [v1, p2], 
# or make two at both [v1, p1] and [v2, p2]. The trick is to treat [v1, p2] as the first transaction, 
# and [v2, p1] as the second. Then we can guarantee the right max profits in both situations, p2 - v1 
# for one transaction and p1 - v1 + p2 - v2 for two.

# Finding all v/p pairs and calculating the profits takes O(n) since there are up to n/2 such pairs. 
# And extracting k maximums from the heap consumes another O(klgn).


class Solution {
public:
    int maxProfit(int k, vector<int> &prices) {
        int n = (int)prices.size(), ret = 0, v, p = 0;
        priority_queue<int> profits;
        stack<pair<int, int> > vp_pairs;
        while (p < n) {
            // find next valley/peak pair
            for (v = p; v < n - 1 && prices[v] >= prices[v+1]; v++);
            for (p = v + 1; p < n && prices[p] >= prices[p-1]; p++);
            // save profit of 1 transaction at last v/p pair, if current v is lower than last v
            while (!vp_pairs.empty() && prices[v] < prices[vp_pairs.top().first]) {
                profits.push(prices[vp_pairs.top().second-1] - prices[vp_pairs.top().first]);
                vp_pairs.pop();
            }
            // save profit difference between 1 transaction (last v and current p) and 2 transactions (last v/p + current v/p),
            // if current v is higher than last v and current p is higher than last p
            while (!vp_pairs.empty() && prices[p-1] >= prices[vp_pairs.top().second-1]) {
                profits.push(prices[vp_pairs.top().second-1] - prices[v]);
                v = vp_pairs.top().first;
                vp_pairs.pop();
            }
            vp_pairs.push(pair<int, int>(v, p));
        }
        // save profits of the rest v/p pairs
        while (!vp_pairs.empty()) {
            profits.push(prices[vp_pairs.top().second-1] - prices[vp_pairs.top().first]);
            vp_pairs.pop();
        }
        // sum up first k highest profits
        for (int i = 0; i < k && !profits.empty(); i++) {
            ret += profits.top();
            profits.pop();
        }
        return ret;
    }
};