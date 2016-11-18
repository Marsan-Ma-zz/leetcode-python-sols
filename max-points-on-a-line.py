# https://leetcode.com/problems/max-points-on-a-line/

# Given n points on a 2D plane, find the maximum number of 
# points that lie on the same straight line.


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

from collections import defaultdict
from itertools import combinations

class Solution(object):
    
    # def maxPoints(self, points):
    #     d = collections.defaultdict(set)
    #     for p, q in itertools.combinations(points, 2):
    #         d[p.x if p.x==q.x else ((p.y-q.y)/float(p.x-q.x), (p.x*q.y-q.x*p.y)/float(p.x-q.x))] |= {p, q}
    #     return max(map(len, d.values())) if len(points)>1 else len(points)
        
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        
        # [Ideas]
        # 1. line in 2d plane: y=ax+b or x=b
        #    => cache key (a,b) and (None, b)
        # 2. go through each pair of points, save points in 
        #    correspoinding hash, then find key with max # of values
        
        if not points: return 0
        if len(points) == 1: return 1
        
        lines = defaultdict(set)
        for p1, p2 in combinations(points, 2):
            if p1.x == p2.x:
                key = (None, p1.x)
            else:
                a = float(p1.y - p2.y) / float(p1.x - p2.x)
                # b = y - a*x 
                #   = p1.y - float(p1.y*p1.x - p2.y*p1.x) / float(p1.x - p2.x)
                #   = (p2.y*p1.x - p1.y*p2.x) / float(p1.x - p2.x)
                b = (p2.y*p1.x - p1.y*p2.x) / float(p1.x - p2.x)
                key = (a, b)
            lines[key].add(p1)
            lines[key].add(p2)
            
        return max(len(v) for v in lines.values())
    
    
    def test(self):
        cases = [
            [],
            [(1,2), (3,4)],
            [(1,2), (3,4), (5,6), (4,8)],
        ]
        for c in cases:
            print(c, self.maxPoints(c))
            
# Solution().test()
