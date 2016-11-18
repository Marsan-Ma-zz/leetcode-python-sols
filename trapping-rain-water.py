# https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map 
# where the width of each bar is 1, compute how much water it 
# is able to trap after raining.

# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.



class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        
        # [Examples]
        # [0,1,0,2,1,0,1,3,2,1,2,1] => 6
        #  
        
        # [Ideas]
        # 1. do one-pass sweep, conclude water amount whenever meet 
        #    new largest value
        # 2. as for rest grids, just reverse it and do the same.
        
        while height and height[0] == 0:
            height.pop(0)
        
        if not height: return 0
        
        water, stack = self.trace_uphill(height)
        water2, _ = self.trace_uphill(reversed(stack))
        return water + water2
    
        
    def trace_uphill(self, height):
        water = 0
        stack = []
        for h in height:
            if not stack or h < stack[0]:
                stack.append(h)
            else: # h >= stack[0]
                base = stack[0]
                water += sum([base-s for s in stack])
                stack = [h]
        return water, stack
    
    
    def test(self):
        cases = [
            [],
            [1,2,3],
            [1,2,3,3,2,1],
            [3,2,1,1,2,3],
            [0,1,0,2,1,0,1,3,2,1,2,1],   
        ]
        for c in cases:
            print(c, self.trap(c))
            
            
# Solution().test()