# https://leetcode.com/problems/largest-rectangle-in-histogram/

# Given n non-negative integers representing the histogram's bar height 
# where the width of each bar is 1, find the area of largest rectangle in the histogram.

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.



class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        # [Ideas]
        # 1. use stack, calculate area only when meet decending new height
        #    add tail 0 for ctrl convenience
        #    Ex: [2,1,5,6,2,3] => 2*1 when meet 1, 6*1 when meet tail 0
        #         5*2 when meet 2, 6*1 when meet 2
        
        
        # trick: heights[stack[-1]] = 0
        stack = [-1]
        heights += [0]
        max_area = 0
        for i, v in enumerate(heights):
            while heights[stack[-1]] > v:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1]
                max_area = max(max_area, h*w)
            stack.append(i)
        return max_area
    
    
    def test(self):
        cases = [
            [],
            [1,2,3],
            [3,1,2,3],
            [3,1,2,3,3,3,1,2],
            [2,1,5,6,2,3],
        ]
        for c in cases:
            print(c, self.largestRectangleArea(c))
            
            
# Solution().test()