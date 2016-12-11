# https://leetcode.com/problems/arithmetic-slices/

# A sequence of number is called arithmetic if it consists of at least three 
# elements and if the difference between any two consecutive elements is the same.

# For example, these are arithmetic sequence:

# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# The following sequence is not arithmetic.

# 1, 1, 2, 5, 7

# A zero-indexed array A consisting of N numbers is given. A slice of that array is 
# any pair of integers (P, Q) such that 0 <= P < Q < N.

# A slice (P, Q) of array A is called arithmetic if the sequence:
# A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

# The function should return the number of arithmetic slices in the array A.


# Example:

# A = [1, 2, 3, 4]

# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.



class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) < 3: return 0
        
        nums = [i-j for i,j in zip(A, A[1:])]
        cnt, last, sol = 0, nums[0], 0
        for n in nums[1:]:
            if n == last:
                cnt += 1
            else:
                sol += self.ladder_sum(cnt)
                cnt = 0
            last = n
        sol += self.ladder_sum(cnt)
        return sol
    
    def ladder_sum(self, cnt):
        cnt = max(0, cnt)
        sol = 0
        while cnt:
            sol += cnt
            cnt -= 1
        return sol
    
    def test(self):
        cases = [
            [1, 3, 5, 7, 9],
            [7, 7, 7, 7],
            [3, -1, -5, -9],
            [3, -1, -5, -9, 1, 3, 5, 7, 9],
        ]
        for c in cases:
            print(c, self.numberOfArithmeticSlices(c))
            
            
# Solution().test()