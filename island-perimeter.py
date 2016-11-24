# https://leetcode.com/problems/island-perimeter/

# You are given a map in form of a two-dimensional integer grid 
# where 1 represents land and 0 represents water. Grid cells are 
# connected horizontally/vertically (not diagonally). The grid is 
# completely surrounded by water, and there is exactly one island 
# (i.e., one or more connected land cells). The island doesn't have 
# "lakes" (water inside that isn't connected to the water around 
# the island). One cell is a square with side length 1. The grid is 
# rectangular, width and height don't exceed 100. Determine the perimeter 
# of the island.

# Example:

# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # [Ideas]
        # 1. every connection of two grid will cancel-out 2 edges
        # 2. do a DFS, traverse all grids to count how many connections
        # 3. 4*grid_number - 2*connections = perimeter
        
        
        if not grid or not grid[0]: return 0
        
        m, n = len(grid), len(grid[0])
        area = sum([sum(row) for row in grid])
        
        # find first "1" grid
        ecnt = 0
        for i in range(m):
            for j in range(n):
                for di, dj in [(1,0),(0,1)]:
                    ii, jj = i+di, j+dj
                    if (ii < m) and (jj < n) and (grid[i][j]) and (grid[ii][jj] == 1):
                        ecnt += 1
                        # print(i, j, ii, jj)
                        
        # print(area, ecnt)
        sol = area*4 - ecnt*2
        return sol
    
    
    def test(self):
        cases = [
            [[0,0,0,0],
             [0,1,1,0],
             [0,1,1,0],
             [0,0,0,0]],
        ]
        for c in cases:
            print(self.islandPerimeter(c))
            
            
# Solution().test()

