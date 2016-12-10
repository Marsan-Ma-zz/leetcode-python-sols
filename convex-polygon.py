# https://leetcode.com/problems/convex-polygon/

# Given a list of points that form a polygon when joined sequentially, 
# find if this polygon is convex (Convex polygon definition).

# Note:

# There are at least 3 and at most 10,000 points.
# Coordinates are in the range -10,000 to 10,000.
# You may assume the polygon formed by given points is always a simple polygon 
# (Simple polygon definition). In other words, we ensure that exactly two edges 
# intersect at each vertex, and that edges otherwise don't intersect each other.
# Example 1:

# [[0,0],[0,1],[1,1],[1,0]]

# Answer: True

# Explanation:
# Example 2:

# [[0,0],[0,10],[10,10],[10,0],[5,5]]

# Answer: False


class Solution(object):
    def isConvex(self, points):
        curr = [points[-1][0] - points[-2][0], points[-1][1] - points[-2][1]]
        dir = 0
        for i in range(len(points)):
            curr, prev = [points[i][0] - points[i-1][0], points[i][1] - points[i-1][1]], curr[:]
            cross_prod = prev[0]*curr[1] - prev[1]*curr[0]
            if cross_prod*dir < 0:
                return False
            if not dir and cross_prod:
                dir = 1 if cross_prod > 0 else -1
        return True
        
    def test(self):
        cases = [
            [[0,0],[0,1],[1,1],[1,0]],
            [[0,0],[0,10],[10,10],[10,0],[5,5]],
        ]
        for c in cases:
            print(c, self.isConvex(c))
            
# Solution().test()