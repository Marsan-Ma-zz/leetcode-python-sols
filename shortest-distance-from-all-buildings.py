# https://leetcode.com/problems/shortest-distance-from-all-buildings/

# You want to build a house on an empty land which reaches all buildings 
# in the shortest amount of distance. You can only move up, down, left and right. 
# You are given a 2D grid of values 0, 1 or 2, where:

# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0

# The point (1,2) is an ideal empty land to build a house, as the total travel distance 
# of 3+3+1=7 is minimal. So return 7.

from collections import deque

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # [Ideas]
        # 1. do BFS from all houses, find grids that
        #    => all houses are reachable  (self.grid)
        #    => with smallest distance    (self.dist)
        # 2. use a level to search for grids reachable 
        #    from all houses
        # 3. use complex to represent matrix graph,
        #    to avoid nested loop, improve readbility

        # initialize graph
        grid = {i+1j*j: grid[i][j]
                     for i, row in enumerate(grid)
                     for j, val in enumerate(row)}
        dist = {k: 0 for k,v in grid.items()}
        
        # bfs: update grid and dist from 1 house
        def bfs(start, level):
            q = deque([start])
            d = 1    # distance
            while q:
                for _ in range(len(q)): # key to ctrl batch with same distance!
                    z = q.popleft()
                    for i in range(4):
                        n = z + 1j**i
                        if grid.get(n) == level:
                            q.append(n)
                            grid[n] -= 1
                            dist[n] += d 
                d += 1
        
        # do bfs from all houses
        level = 0
        for z in grid:
            if grid[z] == 1:
                bfs(z, level)
                level -= 1
        
        # choose minimum dist from valid grid
        best = -1
        for z in grid:
            if grid[z] == level:
                if best == -1 or best > dist[z]:
                    best = dist[z]
        return best
        
        
        
        
        
    def test(self):
        cases = [
            [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]],
        ]
        for c in cases:
            print(self.shortestDistance(c))
            
Solution().test()

# class Solution(object):
#     def shortestDistance(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
        
#         self.grid = grid
#         self.m, self.n, self.nth = len(grid), len(grid[0]), 0
#         self.dist = [[0]*self.n for _ in range(self.m)]

#         for i,row in enumerate(grid):
#             for j, num in enumerate(row):
#                 if num == 1:
#                     if self.helper(i,j)==False:
#                         return -1

#         sol = min([ self.dist[i][j]
#                      for i, row in enumerate(grid)
#                      for j, num in enumerate(row)
#                      if num == (self.nth) ] or [-1] )
        
#         for g in self.grid: print(g)
#         # [1, -3, 2, -3, 1] 
#         # [-3, -3, -3, -3, -3] 
#         # [-3, -3, 1, -3, -3] 
        
#         for d in self.dist: print(d)
#         # [0, 9, 0, 9, 0] 
#         # [9, 8, 7, 8, 9] 
#         # [10, 9, 0, 9, 10] 
#         return sol

    
#     def helper(self, i, j):
#         queue, level = deque([(i,j)]), 1
#         count = 0
#         while queue:
#             for _ in range(len(queue)):
#                 i, j = queue.popleft()
#                 for x, y in [(i,j+1), (i,j-1), (i+1,j), (i-1,j)]:
#                     if 0 <= x < self.m and 0 <= y < self.n and self.grid[x][y] == (self.nth):
#                         count += 1
#                         queue.append((x,y))
#                         self.dist[x][y] += level
#                         self.grid[x][y] = self.nth-1
#             level += 1
#         self.nth -= 1
#         return True if count != 0 else False
    
    
#     def test(self):
#         cases = [
#             [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]],
#         ]
#         for c in cases:
#             print(self.shortestDistance(c))
        
        
# Solution().test()
