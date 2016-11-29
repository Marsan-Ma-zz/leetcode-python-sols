# https://leetcode.com/problems/pacific-atlantic-water-flow/

# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:

# Given the following 5x5 matrix:

#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic

# Return:

# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # [Example]
        #       Pacific ~   ~   ~   ~   ~ 
        #   ~  1   2   2   3  (5) *
        #   ~  3   2   3  (4) (4) *
        #   ~  2   4  (5)  3   1  *
        #   ~ (6) (7)  1   4   5  *
        #   ~ (5)  1   1   2   4  *
        #       *   *   *   *   * Atlantic
        
        # [Ideas]
        # 1. find highland surrounded by lower neighbors
        # 2. left-bottom, right-top is always "True"
        # 3. top-down, bottom-up to the highest, then find intersection
        #    then do the same left-right, right-left
        # 4. how about zig-zag route? like:
        #   ~  1   2   2   3  (5) *
        #   ~  3   2   3  (4) (4) *
        #   ~  2   4  (5)  9   9  *
        #   ~ (6) (7)  4   3   9  *
        #   ~ (5)  9   9   2   9  *
        # ------------------------------------------------------------
        # 1. propagate from left-top and only down/right, 
        #    find end of ascending 
        # 2. same from right-bottom and only up/left, 
        #    find find end of ascending 
        # 3. take their intersection as answer, plus 2 always True point
        # 4. expand solutions with its neighbors with same height.
        # ------------------------------------------------------------
        # 1. do BFS from all coastal nodes 
        # 2. find pacific reach, find atalantic reach, find intersection
        
        if not matrix or not matrix[0]: return []
        
        m, n = len(matrix), len(matrix[0])
        
        pac = [(j, 0) for j in range(m)] + [(0, i) for i in range(1,n)]
        atl = [(j, n-1) for j in range(m)] + [(m-1, i) for i in range(n-1)]

        def fill(stack):
            ocean = set()
            while stack:
                r,c = stack.pop()
                if (r,c) in ocean: continue
                ocean.add((r,c))
                cands = [(nr, nc) for nr, nc
                         in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)] 
                         if (0 <= nr < m) and (0 <= nc < n) 
                         and (matrix[nr][nc] >= matrix[r][c])]
                stack.extend(cands)
            return ocean
        
        
        pacific, atlantic = fill(pac), fill(atl)
        sol = [list(x) for x in pacific & atlantic]
        return sol
            
        
        
        
    def test(self):
        matrix = [
            [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,9,9],
            [6,7,4,3,9],
            [5,9,9,2,9],
        ]
        print(self.pacificAtlantic(matrix))
        
        
# Solution().test()