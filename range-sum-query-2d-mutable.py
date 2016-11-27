# https://leetcode.com/problems/range-sum-query-2d-mutable/

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
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10

# Note:
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function 
# is distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.



# [Ideas]
# 1. for inmutable NumMatrix, we use table[i][j] to record
#     the sum of square from (0,0) to (i,j) and make update and
#     sum region be O(1)
# 2. there is a data structure "binary indexed tree" dedicate to 
#     this problem, it's tricky and not generous, but in O(log(n))
# 3. here we use same idea as 1, but only sum in one dimention,
#     table[i][j] = sum from table[i][0] to table[i][j],
#     thus update and sum take O(n)


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
        self.matrix = matrix
        self.sols = [[0]*n for _ in range(m)]
        
        self.sols[0] = matrix[0]
        for i in range(1, m):
            for j in range(n):
                self.sols[i][j] = self.sols[i-1][j] + matrix[i][j]
            # print(self.sols[i])
                
                
    def update(self, row, col, val):
        self.matrix[row][col] = val
        for i in range(row, len(self.sols)):
            self.sols[i][col] = self.matrix[i][col]
            if i > 0:
                self.sols[i][col] += self.sols[i-1][col]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sol = 0
        for i in range(col1, col2+1):
            sol += self.sols[row2][i]
            if row1 > 0:
                sol -= self.sols[row1-1][i]
        # print(sol)
        return sol
    
        
def test():
    matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    nom = NumMatrix(matrix)
    nom.sumRegion(2, 1, 4, 3) #-> 8
    nom.update(1,2,10)
    nom.sumRegion(1, 1, 2, 2) #-> 11
    nom.sumRegion(1, 2, 2, 4) #-> 12

# test()