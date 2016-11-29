# https://leetcode.com/problems/ugly-number-ii/

# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

# Ex:
# nums      1  2  3  4  5 ...
# lane-2    2  4  6 ->
# lane-3    3  6 ->
# lane-5    5  10 ->


# Note that 1 is typically treated as an ugly number.

# Hint:

# The naive approach is to call isUgly for every number until you reach 
# the nth one. Most numbers are not ugly. Try to focus your effort on generating 
# only the ugly ones.
# An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
# The key is how to maintain the order of the ugly numbers. Try a similar approach 
# of merging from three sorted lists: L1, L2, and L3.
# Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).



from heapq import *

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        # [Ideas]
        # 1. keep generate next numbers, use heap to maintain 
        # 2. to guarantee always get next minimum number, 
        #    use current smallest number to multiply with primes
        #    usually we use heap with k size to get kth smallest/largest
        #    number, but this time we pop them instead, and use heap to 
        #    keep the candidates for "current smallest"
        # 3. then pop the current smallest, do the same to 2nd smallest
        # 4. the nth number to pop will be the nth smallest ugly number
                
        if n == 1: return 1
        
        primes = [2, 3, 5]
        cands = [(1, 1)]
        
        for i in range(n):
            val, th = heappop(cands)
            for p in primes:
                if th <= p:
                    heappush(cands, (val*p, p))
            if i == n-1: return val
            
    
    
    def test(self):
        # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
        for i in range(15):
            print(i, self.nthUglyNumber(i))
            
            
# Solution().test()