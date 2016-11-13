# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Given a n x n matrix where each of the rows and columns are sorted 
# in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, 
# not the kth distinct element.

# Example:
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.


import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        # [Examples]
        # matrix = [
        #    [ 1,  5, 19],
        #    [10, 11, 23],
        #    [52, 53, 95]
        # ],
        # k = 8, return 23.
        
        # [Ideas]
        # 1. use min-heap with size n, each node storing the whole row
        # 2. pop k times to get the kth smallest item 
        # 3. O(n*log(n)) time build heap with 1st column, O(k) time popping
        #----------------------------------
        # 1. neither left-bottom nor right-top grid guarantee to be medium
        
        if not matrix: return None
        if k > len(matrix)**2: return None
        
        h = [(row[0], row[1:]) for row in matrix]
        heapq.heapify(h)
        
        for i in range(k):
            val, row = h[0]
            if row:
                heapq.heapreplace(h, (row[0], row[1:]))
            else:
                heapq.heappop(h)
        return val
    
    def test(self):
        matrix = [
            [ 1,    5,  19, 100],
            [10,   11,  23, 200],
            [52,   53,  95, 321],
            [152, 153, 295, 521],
        ]
        for i in range(1,len(matrix)**2+1):
            print(self.kthSmallest(matrix, i))
              
              

# Solution().test()
# print([1,2,3][5:])