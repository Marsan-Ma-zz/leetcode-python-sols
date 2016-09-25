# https://leetcode.com/problems/number-of-islands/
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:

# 11000
# 11000
# 00100
# 00011
# Answer: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        # [Ideas]
        # 1. each time find a '1', 
        #     recursively write all connected grid to '0' 
        #     (let's call this 'occupy' function)
        # 2. that's 1 island, then we find next '1'
        if not grid: return 0

        self.grid = grid
        self.size_x, self.size_y = len(self.grid), len(self.grid[0])
        cnt = 0
        for i in range(self.size_x):
            for j in range(self.size_y):
                if grid[i][j] == '1':
                    self.occupy(i, j)  
                    cnt += 1
        return cnt


    def occupy(self, i, j):
        cands = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        cands = [(i,j) for i,j in cands if i>=0 and j>=0 and i<self.size_x and j<self.size_y]
        for i, j in cands:
            if self.grid[i][j] == '1':
                self.grid[i][j] = '0'
                self.occupy(i, j)

    def test(self):
        cases = [
            [],
            [
                ['1', '1', '1', '0', '1'],
                ['1', '1', '0', '0', '1'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '0', '1', '1'],
            ]
        ]
        for c in cases:
            print(self.numIslands(c))

Solution().test()