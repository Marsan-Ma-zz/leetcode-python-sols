# https://leetcode.com/problems/max-sum-of-sub-matrix-no-larger-than-k/

# Given a non-empty 2D matrix matrix and an integer k, find the max sum of a 
# rectangle in the matrix such that its sum is no larger than k.

# Example:
# Given matrix = [
#   [1,  0, 1],
#   [0, -2, 3]
# ]
# k = 2
# The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is 
# the max number no larger than k (k = 2).

# Note:
# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?



class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        # [Ideas]
        # 1. brute force will be O(n^4)
        # 2. we could do some trick to make last dimention become binary search,
        #    something like "minimum subsequence sum" but it's a "nearest" probem
        #    thus can't use hashmap, but use binary-search to find "nearest"
        #    => O(n**3 * log(k))

        m = len(matrix)
        n = len(matrix[0]) if m else 0
        
        M = max(m, n)
        N = min(m, n)
        ans = None
        for x in range(N):
            sums = [0] * M
            for y in range(x, N):
                slist, num = [], 0
                for z in range(M):
                    sums[z] += matrix[z][y] if m > n else matrix[y][z]
                    num += sums[z]
                    if num <= k: ans = max(ans, num)
                    i = bisect.bisect_left(slist, num - k)
                    if i != len(slist): ans = max(ans, num - slist[i])
                    bisect.insort(slist, num)
        return ans or 0