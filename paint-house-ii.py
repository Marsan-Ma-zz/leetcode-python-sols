# https://leetcode.com/problems/paint-house-ii/

# There are a row of n houses, each house can be painted with one 
# of the k colors. The cost of painting each house with a certain 
# color is different. You have to paint all the houses such that 
# no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented 
# by a n x k cost matrix. For example, costs[0][0] is the cost of 
# painting house 0 with color 0; costs[1][2] is the cost of painting 
# house 1 with color 2, and so on... Find the minimum cost to paint all houses.

# Note:
# All costs are positive integers.

# Follow up:
# Could you solve it in O(nk) runtime?

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        # min1 means we paint all other states with the minimum cost, 
        # while min2 means we cannot paint consecutive houses with same color 
        # so we choose the second lowest cost to add up with.
        
        if not costs: return 0
        n, k = len(costs), len(costs[0])
        for i in xrange(1, n):
            min1 = min(costs[i-1])
            idx = costs[i-1].index(min1)
            min2 = min(costs[i-1][:idx] + costs[i-1][idx+1:])
            for j in xrange(k):
                if j == idx:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
        return min(costs[-1])