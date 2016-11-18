# https://leetcode.com/problems/rectangle-area/

# Find the total area covered by two rectilinear rectangles 
# in a 2D plane.

# Each rectangle is defined by its bottom left corner and top 
# right corner as shown in the figure.


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        
        l, r = max(A, E), min(C, G)
        t, b = min(D, H), max(B, F)
        if l >= r or b >= t: 
            cross = 0
        else:
            cross = (r-l)*(t-b)
        
        a1 = (C-A)*(D-B)
        a2 = (G-E)*(H-F)
        return a1 + a2 - cross
            
        