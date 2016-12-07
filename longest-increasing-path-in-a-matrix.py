# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# Given an integer matrix, find the length of the longest increasing path.

# From each cell, you can either move to four directions: left, right, up or down. 
# You may NOT move diagonally or move outside of the boundary 
# (i.e. wrap-around is not allowed).

# Example 1:

# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].

# Example 2:

# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Return 4
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


class Solution(object):

    # [Ideas] bottom-up
    # 1. use python complex to make matrix hash, 2D => 1D
    # 2. sort this 1D by value
    # 3. from smallest grid, update according to neighbors 
    #    with largest possesed length
    
    def longestIncreasingPath(self, matrix):
        matrix = {i + j*1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}
        length = {}
        
        for z in sorted(matrix, key=matrix.get):
            val = 0
            for Z in z+1, z-1, z+1j, z-1j:
                if Z in matrix and matrix[z] > matrix[Z]:
                    val = max(val, length[Z])
            length[z] = 1 + val
        return max(length.values() or [0])

    
    # top-down version
    def longestIncreasingPath(self, matrix):
        def length(z):
            val = 0
            if z not in memo:
                for Z in z+1, z-1, z+1j, z-1j:
                    if Z in matrix and matrix[z] > matrix[Z]:
                        val = max(val, length(Z))
                memo[z] = 1 + val
            return memo[z]
        memo = {}
        matrix = {i + j*1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}
        sol = list(map(length, matrix))
        return max(sol) if sol else 0
    
    
    
#     def longestIncreasingPath(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: int
#         """
        
        # [Ideas]
        # 1. if grid has any neighbor smaller than self, pass
        # 2. if grid smaller than any neighbor, could be a start point candidate
        # 3. do DFS for start point candidates, their path shall not overlap, thus O(m*n)

#         if not matrix or not matrix[0]: return 0
        
#         self.matrix = matrix
#         self.m, self.n = len(matrix), len(matrix[0])
#         visited = [[0]*self.n for _ in range(self.m)]
        
#         sol = 0
#         for i in range(self.m):
#             for j in range(self.n):
#                 if visited[i][j]: continue
#                 for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
#                     if 0 <= x < self.m and 0 <= y < self.n:
#                         if matrix[x][y] < matrix[i][j]:
#                             visited[i][j] = True
#                             break
#                         elif matrix[x][y] > matrix[i][j]:
#                             visited[x][y] = True
#                 if not visited[i][j]: 
#                     sol = max(sol, self.bfs(i, j))
#                     visited[i][j] = True
#         return sol
    
    
#     def bfs(self, xi, yi):
#         print("bfs:", xi, yi)
#         cands = [(xi, yi, 1)]
#         best = 0
#         while cands:
#             i, j, v = cands.pop(0)
#             best = max(best, v)
#             for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
#                 if 0 <= x < self.m and 0 <= y < self.n and self.matrix[x][y] > self.matrix[i][j]:
#                     cands.append((x, y, v+1))
#                     # print((x, y, v+1))
#         # print("dbg", xi, yi, best)
#         return best
                    
        
    def test(self):
        cases = [
            [],
            [[9,9,4], [6,6,8], [2,1,1]],
            [[3,4,5], [3,2,6], [2,2,1]],
        ]
        for c in cases:
            print(self.longestIncreasingPath(c))
            
# Solution().test()
