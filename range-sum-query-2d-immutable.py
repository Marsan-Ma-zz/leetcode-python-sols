# https://leetcode.com/problems/range-sum-query-2d-immutable/

# Given a 2D matrix matrix, find the sum of the elements inside the 
# rectangle defined by its upper left corner (row1, col1) and lower 
# right corner (row2, col2).

# Range Sum Query 2D
# The above rectangle (with the red border) is defined by 
# (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.



class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]: 
            self.sols = [[]]
            return
        
        m, n = len(matrix), len(matrix[0])
        self.sols = [[0]*n for _ in range(m)]
        
        self.sols[0][0] = matrix[0][0]
        for i in range(1, m):
            self.sols[i][0] = self.sols[i-1][0] + matrix[i][0]
        
        for i in range(m):
            s = matrix[i][0]
            for j in range(1, n):
                s += matrix[i][j]
                self.sols[i][j] = self.sols[i-1][j] + s
            # print(self.sols[i])
                

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # exception
        c1 = (row1 <= row2 <= len(self.sols))
        c2 = (col1 <= col2 <= len(self.sols[0]))
        if not (c1 and c2): return 0
        
        sol = self.sols[row2][col2]
        if row1: sol -= self.sols[row1-1][col2]
        if col1: sol -= self.sols[row2][col1-1]
        if row1 and col1: sol += self.sols[row1-1][col1-1]
        # print(sol)
        return sol
        
def test():
    matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      # [4, 1, 0, 1, 7],
      # [1, 0, 3, 0, 5]
    ]
    nom = NumMatrix(matrix)
    nom.sumRegion(2, 1, 4, 3) #-> 8
    nom.sumRegion(1, 1, 2, 2) #-> 11
    nom.sumRegion(1, 2, 2, 4) #-> 12

# test()