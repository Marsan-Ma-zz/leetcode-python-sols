# https://leetcode.com/problems/line-reflection/

# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

# Example 1:
# Given points = [[1,1],[-1,1]], return true.

# Example 2:
# Given points = [[1,1],[-1,-1]], return false.

# Follow up:
# Could you do better than O(n2)?



from collections import defaultdict

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        
        # [Examples]
        # 1. [[1,1],[-1,1]], return true.
        # 2. [[1,1],[-1,-1]], return false
        
        # [Ideas]
        # 1. reflect: 
        #    => y value are paired, 
        #    => each pair have same average value x
        # 2. use hashmap to store same y points
        #    better keep them sorted, or sort them after hash constructed
        # 3. this cost O(nlogn) for sorting, could be better!
        #-------------------------------------- 
        # 1. scan and find min/max of x, thus we have reflection x
        # 2. use hash map to record x value haven't found pair, 
        #    in all y value
        
        if len(points) <= 1: return True
        
        xs = [x for x,y in points]
        mid_x = float(min(xs) + max(xs)) / 2
        
        pairs = defaultdict(dict)
        
        # validation
        for x,y in points:
            mirror_x = x - 2 * (x-mid_x)
            if x == mid_x:
                continue
            elif mirror_x in pairs[y]:
                pairs[y][x] = 0
                pairs[y][mirror_x] = 0
            else:
                pairs[y][x] = 1
        
        # print(pairs)
        unpaired = sum([sum(v.values()) for k,v in pairs.items()])
        return (unpaired == 0)
    
    
    def test(self):
        cases = [
            # [],
            # [[1,1]],
            # [[0,0],[1,0]],
            # [[1,1],[-1,1]],
            # [[1,1],[-1,-1]],
            # [[1,1],[-1,-1],[-1,1]],
            [[1,1],[-1,-1],[-1,1], [1,-1]],
            # [[1,1],[-1,-1],[-1,1], [2,-1]],
        ]
        for c in cases:
            print(c, self.isReflected(c))
            
        
# Solution().test()

