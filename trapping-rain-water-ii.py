# https://leetcode.com/problems/trapping-rain-water-ii/

# Given an m x n matrix of positive integers representing the height 
# of each unit cell in a 2D elevation map, compute the volume of water 
# it is able to trap after raining.

# Note:
# Both m and n are less than 110. The height of each unit cell is greater 
# than 0 and is less than 20,000.

# Example:

# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]

# Return 4.


class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
        
        import heapq    
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0]*n for _ in xrange(m)]

        # Push all the block on the border into heap
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        
        result = 0
        while heap:
            height, i, j = heapq.heappop(heap)    
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height-heightMap[x][y])
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = 1
        return result