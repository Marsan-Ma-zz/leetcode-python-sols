# https://leetcode.com/problems/the-skyline-problem/

# A city's skyline is the outer contour of the silhouette formed by 
# all the buildings in that city when viewed from a distance. 
# Now suppose you are given the locations and height of all the buildings 
# as shown on a cityscape photo (Figure A), write a program to output the 
# skyline formed by these buildings collectively (Figure B).


# Buildings Skyline Contour
# The geometric information of each building is represented by a triplet 
# of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the 
# left and right edge of the ith building, respectively, and Hi is its 
# height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, 
# and Ri - Li > 0. You may assume all buildings are perfect rectangles 
# grounded on an absolutely flat surface at height 0.

# For instance, the dimensions of all buildings in Figure A are recorded 
# as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

# The output is a list of "key points" (red dots in Figure B) in the format 
# of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. 
# A key point is the left endpoint of a horizontal line segment. Note that 
# the last key point, where the rightmost building ends, is merely used to 
# mark the termination of the skyline, and always has zero height. Also, 
# the ground in between any two adjacent buildings should be considered part 
# of the skyline contour.

# For instance, the skyline in Figure B should be represented as:
# [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

# Notes:

# The number of buildings in any input list is guaranteed to be in the range [0, 10000].
# The input list is already sorted in ascending order by the left x position Li.
# The output list must be sorted by the x position.
# There must be no consecutive horizontal lines of equal height in the output 
# skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not 
# acceptable; the three lines of height 5 should be merged into one in the 
# final output as such: [...[2 3], [4 5], [12 7], ...]



from heapq import *

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # [Ideas]
        # 1. sort buildings according to left key-points
        # 2. one-pass and replace intervals height as max-height there
        #    => use max-heap, pop all intervals larger than new left-edge
        #    => update height, push back to heap.
        #    => use interval as a node? or use a point only?
        #    => O(n^2)
        # ----------------------------------
        # 1. sort buildings according to height? O(nlogn)
        #    => later intervals only need to break
        #    => no efficient data structure to check all existing intervals
        #    => each new interval should check all n existing => O(n^2)
        # ----------------------------------
        # 1. scan once, find all critical points, sort => O(nlogn)
        # 2. use max-heap to record current max height
        #    => how to efficiently delete height from heap?
        #    => no update, but pop until node right edge valid before use
        #    collect key-points in the same time
        
        
        # adding right node for checking "falling to lower places"!
        nodes = buildings + [[r, None, None] for l, r, h in buildings]
        nodes = sorted(nodes, key=lambda v: v[0])
        
        
        sol = []
        heap = [[0, 1<<32]]  # (-height, right) max-heap
        for l, r, h in nodes:
            # update heap
            while heap[0][1] <= l:
                heappop(heap)
            if h != None:
                heappush(heap, [-h, r])
            
            # append new key-point
            max_h = -heap[0][0]
            if (not sol):
                sol.append([l, max_h])
            elif (sol[-1][0] == l):
                sol[-1][1] = max(max_h, sol[-1][1])
            elif (sol[-1][1] != max_h):
                sol.append([l, max_h])
                
        return sol

        
        
    def test(self):
        cases = [
            [],
            [ [10,20,30]],
            [ [10,20,30], [12, 40, 20] ],
            [ [10,20,30], [12, 40, 50] ],
            [ [10,20,30], [12, 40, 50], [15, 80, 70] ],
            [[1,2,1],[1,2,2],[1,2,3]],
            [ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ],
            [[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]],    # [[0,7],[5,12],[10,7],[15,12],[20,7],[25,0]]
        ]
        
        for c in cases:
            print(self.getSkyline(c))
            
            
# Solution().test()