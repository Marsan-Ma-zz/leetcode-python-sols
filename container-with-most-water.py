# https://leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an, where each represents 
# a point at coordinate (i, ai). n vertical lines are drawn such that 
# the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
# which together with x-axis forms a container, such that the container 
# contains the most water.



class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        
        p1, p2 = 0, len(height)-1
        sol = 0
        while p1 < p2:
            sol = max(sol, (p2-p1)*min(height[p1], height[p2]))
            if height[p1] < height[p2]:
                p = p1
                while (height[p] <= height[p1]) and (p < p2):
                    p += 1
                p1 = p
            else:
                p = p2
                while (height[p] <= height[p2]) and (p > p1):
                    p -= 1
                p2 = p
        return sol
        
        
                    