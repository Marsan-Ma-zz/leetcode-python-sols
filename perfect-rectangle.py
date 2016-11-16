# https://leetcode.com/problems/perfect-rectangle/

# Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

# Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


# Example 1:

# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [3,2,4,4],
#   [1,3,2,4],
#   [2,3,3,4]
# ]

# Return true. All 5 rectangles together form an exact cover of a rectangular region.

# Example 2:

# rectangles = [
#   [1,1,2,3],
#   [1,3,2,4],
#   [3,1,4,2],
#   [3,2,4,4]
# ]

# Return false. Because there is a gap between the two rectangular regions.

# Example 3:

# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [3,2,4,4]
# ]

# Return false. Because there is a gap in the top center.

# Example 4:

# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [2,2,4,4]
# ]

# Return false. Because two of the rectangles overlap with each other.


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
        # [Ideas]
        # 1. divide all into 1x1 rectangle, find left-bot and right-top,
        #    track if all grid are covered and covered only once
        #------------------------------------------------------------
        # 2. improve: don't divide, parse each larger rectangle and remove
        #    grids from set
        #------------------------------------------------------------
        # 3. sort rectangles according to y-axis, then start from lowerest
        #    rectangles, grow the skyline => O(nlogn)
        #------------------------------------------------------------
        # 4. linear solution: count area and corners
        #    => sum(fragment areas) should = max_area
        #    => corners except 4 ends should appear even times
        
        
        if not rectangles: return False
        
        # get boundary
        min_x, min_y, max_x, max_y = rectangles[0]
        for l, d, r, u in rectangles[1:]:
            min_x = min(min_x, l)
            max_x = max(max_x, r)
            min_y = min(min_y, d)
            max_y = max(max_y, u)
            
        ideal_area = (max_x - min_x)*(max_y - min_y)
        
        area, corners = 0, set()
        for l, d, r, u in rectangles:
            area += (r-l)*(u-d)
            for p in [(l,d), (l,u), (r,d), (r,u)]:
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)
                    
        ideal_corners = set([(min_x, min_y), (min_x, max_y), 
                             (max_x, min_y), (max_x, max_y)])
        
        # print(area, ideal_area)
        # print(corners, ideal_corners)
        
        if area != ideal_area: return False
        if corners != ideal_corners: return False
        
        return True
            
#         skyline = {x: min_y for x in range(min_x, max_x)}
#         for l,d,r,u in sorted(rectangles, key=lambda v: v[1]):
#             for x in range(l, r):
#                 if skyline[x] != d:
#                     print(x, skyline[x], d)
#                     return False
#                 else:
#                     skyline[x] = u
        
#         last = None
#         for k,v in skyline.items():
#             if not last: 
#                 last = v
#             elif v != last:
#                 return False
#         # print(skyline)
#         return True
        
        
        
    def test(self):
        cases = [
            [],
            [
                [1,1,2,2],
            ],
            [
                [1,1,2,2],
                [2,2,3,3],
            ],
            [
                [1,1,4,4],
                [2,2,3,3],
            ],
            [
                [1,1,3,3],
                [3,1,4,2],
                [3,2,4,4],
                [1,3,2,4],
                [2,3,3,4]
            ],
            [
                [1,1,2,3],
                [1,3,2,4],
                [3,1,4,2],
                [3,2,4,4]
            ],
            [
                [1,1,3,3],
                [3,1,4,2],
                [1,3,2,4],
                [3,2,4,4]
            ],
            [[0,0,4,1],[7,0,8,2],[6,2,8,3],[5,1,6,3],[4,0,5,1],[6,0,7,2],[4,2,5,3],[2,1,4,3],[0,1,2,2],[0,2,2,3],[4,1,5,2],[5,0,6,1]],
        ]
        
        for c in cases:
            print(self.isRectangleCover(c))
        
        
        
# Solution().test()

