# https://leetcode.com/problems/4sum-ii/

# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) 
# there are such that A[i] + B[j] + C[k] + D[l] is zero.

# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. 
# All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

# Example:

# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]

# Output:
# 2

# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0



from collections import Counter

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        # [Ideas]
        # 1. since list could be random number, no benefit to take.
        #    => what we could do is find efficient way to get all combinations
        # 2. get all combs from A+B and C+D, then do 2Sum to these two result
        # 3. use python comprehension to gen all combs efficiently!
        
        comb1 = Counter([a+b for a in A for b in B])
        comb2 = Counter([c+d for c in C for d in D])
        
        sol = 0
        for k,v in comb1.items():
            if -k in comb2:
                sol += v * comb2[-k]
                
        return sol