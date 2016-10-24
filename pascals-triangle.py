# https://leetcode.com/problems/pascals-triangle/

# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        # [Ideas]
        # row_i = (row_i << 1) + row_i
        
        if not numRows: return []
        
        sol = [[1]]
        for i in range(1, numRows):
            row = sol[i-1] + [0]
            for j in range(1, len(row)):
                row[j] += sol[i-1][j-1]
            sol.append(row)
        return sol
    
    
    def test(self):
        cases = [0, 1, 2, 3, 5, 10]
        for c in cases:
            print(c, self.generate(c))
        
        
# Solution().test()