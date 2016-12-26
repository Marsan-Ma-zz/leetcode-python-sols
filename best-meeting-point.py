# https://leetcode.com/articles/best-meeting-point/

# A group of two or more people wants to meet and minimize the total travel distance. 
# You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. 
# The distance is calculated using Manhattan Distance, 
# where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

# For example, given three people living at (0,0), (0,4), and (2,2):

# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

# Hint:

# Try to solve it in one dimension first. How can this solution apply to the two dimension case?



class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        
        xs, ys = [], []
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    xs.append(i)
                    ys.append(j)
                
        if not xs: return 0
        mid = len(xs)//2
        xs, ys = sorted(xs), sorted(ys)
        xmid, ymid = xs[mid], ys[mid]
        sol = sum(abs(x-xmid) for x in xs) + sum(abs(y-ymid) for y in ys)
        return sol