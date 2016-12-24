# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

# There are a number of spherical balloons spread in two-dimensional space. 
# For each balloon, provided input is the start and end coordinates of the horizontal diameter. 
# Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end 
# of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

# An arrow can be shot up exactly vertically from different points along the x-axis. 
# A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. 
# There is no limit to the number of arrows that can be shot. An arrow once shot keeps 
# travelling up infinitely. The problem is to find the minimum number of arrows that must 
# be shot to burst all balloons.

# Example:

# Input:
# [[10,16], [2,8], [1,6], [7,12]]

# Output:
# 2

# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) 
# and another arrow at x = 11 (bursting the other two balloons).



class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        # [Ideas]
        # 1. sort by left-x point, then greedy use current arrow to 
        #    burst as many following.
        # 2. cur = current ballon right side, suppose next arrow aim here
        #    => if next ballon start point <= cur, then aim this narrowed
        #       tail. No worry about left-side since we sort by left-x
        #    => until next ballon start point > cur, shot cur arrow and 
        #       start next batch "aiming".
        
        if not points: return 0
        points = sorted(points, key=lambda p: p[0])
        
        sol, cur = 0, points[0][1] # tail of 1st ballon
        for a, b in points[1:]:
            if a <= cur:
                cur = min(cur, b)
            else: # a > cur
                sol += 1  # shoot current batch with 1 arrow
                cur = b   # start next batch
        return sol+1      # with last batch
            