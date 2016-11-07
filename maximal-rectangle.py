# https://leetcode.com/problems/maximal-rectangle/

# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# For example, given the following matrix:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 6.



class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        # [Ideas]
        # 1. use 1 row to accumulate last rows height
        # 2. find maximum rectangle in current row
        # 3. repeat for all rows
        
        if not matrix or not matrix[0]: return 0
        
        max_area = 0
        hist = [0] * (len(matrix[0]) + 1) # tail 0 for special use
        for row in matrix:
            # update
            for i, v in enumerate(row):
                hist[i] = hist[i]+1 if row[i] == '1' else 0
            # print(state)
            # find max area
            stack = [-1]
            for i, v in enumerate(hist):
                while hist[stack[-1]] > v:
                    h = hist[stack.pop()]
                    w = i - 1 - stack[-1]
                    max_area = max(max_area, h * w)
                stack.append(i)
        return max_area
        
    
    def test(self):
        cases = [
            ["01111",
             "11110",
             "01110",
             "11110",
             "11111",
             "00000"],
        ]
        for mat in cases:
            print(self.maximalRectangle(mat))
        
        
# Solution().test()