# # https://leetcode.com/problems/maximal-square/

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# For example, given the following matrix:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        [ideas]
            1. start from all mxn points as the left-topmost point, check the maximum square.
            2. DP: record how many continuous '1' for both dimention
                     [n]            
                   0 1 2 3 4
                 ------------
               0 | 1 0 1 0 0   if matrix[2][3] = '1':
          [m]  1 | 1 0 1 1 1      tbl(2,3)[m] = min(tbl(1,3)[m]+1, tbl(2,2)[m])
               2 | 1 1 1 1 1      tbl(2,3)[n] = min(tbl(1,3)[n], tbl(2,2)[n]+1)
               3 | 1 0 0 1 0
        """
        # boundary cases
        if (not matrix) or (not matrix[0]): return 0
        
        # initialize
        m, n = len(matrix), len(matrix[0])
        tbl = [[[0,0,0]]*n for i in range(m)]
        
        # DP: table record min(longest 1's to left, longest 1's to top, possible max square (1+left-top point))
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0': 
                    tbl[i][j] = [0, 0, 0]
                elif (i == '0') and (j == '0'):
                    tbl[i][j] = [1, 1, 1]
                elif (i == '0'):
                    tbl[i][j] = [tbl[i][j-1][0]+1, 1, 1]
                elif (j == '0'):
                    tbl[i][j] = [1, tbl[i-1][j][1]+1, 1]
                else:
                    tbl[i][j] = [tbl[i][j-1][0]+1, tbl[i-1][j][1]+1, tbl[i-1][j-1][2]+1]
                    tbl[i][j][2] = min(tbl[i][j])
        max_sqr = max([c[2] for r in tbl for c in r])
        # print(tbl)
        return max_sqr * max_sqr

    def unit_test(self):
        cases = [
            [],
            [[]],
            [["0"]],
            [["1"]],
            [["1","1"],["1","1"]],
            [["0","1","1"], ["1","1","1"], ["1","0","1"]],
            [["0","0","0","0"], ["1","1","0","1"], ["1","1","0","1"], ["0","0","1","1"]],
        ]
        for case in cases:
            print('-'*40, "\n", case, self.maximalSquare(case))


# Solution().unit_test()
