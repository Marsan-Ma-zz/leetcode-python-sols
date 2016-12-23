# https://leetcode.com/problems/spiral-matrix/

# Given a matrix of m x n elements (m rows, n columns), 
# return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


class Solution(object):

    # [tricky] https://discuss.leetcode.com/topic/19034/1-liner-in-python
    def spiralOrder(self, matrix):
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])


    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        ------> Y
        | 1 2 3
        | 4 5 6
        v 7 8 9
        X
        """
        ans = []
        if not matrix: return ans
        if not matrix[0]: return ans
        
        ymax = len(matrix[0])
        xmax = len(matrix)
        dirs = [[0,1,ymax-1], [1,0,xmax-1], [0,-1,0], [-1,0,1]]  # [(0,1,1), (1,0,0), (0,-1,0), (-1,0,1)]
        didx = 0
        cur = [0,0,1]
        end = xmax * ymax  # 2
        while cur[2] <= end:
            ans.append(matrix[cur[0]][cur[1]]) # = cur[2]
            d = dirs[didx]
            if (cur[(didx+1) % 2] == d[2]):
                d[2] = d[2] + (1 if (didx >=2) else -1)
                didx = (didx + 1) % 4
                d = dirs[didx]
            cur[0] += d[0]
            cur[1] += d[1]
            cur[2] += 1
        return ans

        