# https://leetcode.com/problems/sparse-matrix-multiplication/

# Given two sparse matrices A and B, return the result of AB.

# You may assume that A's column number is equal to B's row number.

# Example:

# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]

# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]


#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not A or not B: return []
        if not A[0] or not B[0]: return []
        
        # initialize C
        C = [[0] * len(B[0]) for _ in range(len(A))]
        
        
        ## [Brute force]
        # # caculate C
        # for i in range(len(A)):
        #     for j in range(len(B[0])):
        #         C[i][j] = sum([A[i][k]*B[k][j] for k in range(len(B))])
          
        ## [Sparse]
        for ai in range(len(A)):
            for aj in range(len(A[0])):
                if A[ai][aj] == 0: continue
                for bi in range(len(B[0])):
                    if B[aj][bi] != 0: 
                        C[ai][bi] += A[ai][aj]*B[aj][bi]
            
        return C
    
    def test(self):
        cases = [
            ([], []),
            ([[1,-5]], [[12],[-1]]),
            ([[1,2,3], [4,5,6]], [[5,6], [7,8], [9,10]]),
        ]
        for a, b in cases:
            print(self.multiply(a, b))
        
        
Solution().test()