# https://leetcode.com/problems/unique-paths/

# A robot is located at the top-left corner of a m x n grid 
# (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid 
# (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        tbl = {}
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (i <= 1) | (j <= 1):
                    tbl[i, j] = 1
                else:
                    tbl[i, j] = tbl[i-1, j] + tbl[i, j-1]
        return tbl[m, n]