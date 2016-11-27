# https://leetcode.com/problems/paint-house/

# There are a row of n houses, each house can be painted with one of 
# the three colors: red, blue or green. The cost of painting each house 
# with a certain color is different. You have to paint all the houses 
# such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by 
# a n x 3 cost matrix. For example, costs[0][0] is the cost of painting 
# house 0 with color red; costs[1][2] is the cost of painting house 1 with 
# color green, and so on... Find the minimum cost to paint all houses.



class Solution(object):


    def minCost(self, costs):
        return min(reduce(lambda (A,B,C), (a,b,c): (a+min(B,C), b+min(A,C), c+min(A,B)),
                      costs, [0]*3))


    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        # [Ideas]
        # 1. use dynamic programming, for house i there are 3 options
        #    => if not same color as min(dp[i-1]), use cheapest: 
        #    => if same as min(dp[i-1]), use min(dp[others])
        
        if not costs or not costs[0]: return 0
        
        for i in range(1, len(costs)):
            c1 = min(costs[i-1])
            best = costs[i-1].index(c1)
            c2 = min(costs[i-1][:best] + costs[i-1][best+1:])
            for j in range(len(costs[0])):
                costs[i][j] += c2 if j == best else c1
                
        return min(costs[-1])
    
    
    def test(self):
        cases = [
            [
                [1,2,3],
                # [4,5,6],
                # [7,8,9],
            ],
        ]
        for c in cases:
            print(c, self.minCost(c))
        
        
# Solution().test()