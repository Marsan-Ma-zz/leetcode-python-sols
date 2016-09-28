# https://leetcode.com/problems/search-a-2d-matrix-ii/

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,

# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.

# Given target = 20, return false.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # [Example]
        # [
        #   [1,   4,  7, 11, 15],
        #   [2,   5,  8, 12, 19],
        #   [3,   6,  9, 16, 22],
        #   [10, 13, 14, 17, 24],
        #   [18, 21, 23, 26, 30]
        # ]
        #
        # [ideas]
        # 1. start from leftmost-bottommost (18), 
        #    => if larger, go right => the next > target, return False
        #    => if smaller, go up => the next < target, return False
        #    => if found, return True
        #    => O(m+n)
        
        
        
        if not matrix or not matrix[0]: return None
        
        i, j = len(matrix)-1, 0
        while True:
            cur = matrix[i][j]
            if cur == target:
                return True
            elif (cur > target) and (i-1 >= 0):
                i -= 1
            elif (cur < target) and (j+1 < len(matrix[0])):
                j += 1
            else:
                return False
            
    def test(self):
        mat = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
        tar = [0, 15, 18, 27, 30, 33]
        for t in tar:
            print(t, self.searchMatrix(mat, t))
        
Solution().test()