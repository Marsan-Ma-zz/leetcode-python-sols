# https://leetcode.com/problems/super-ugly-number/

# Write a program to find the nth super ugly number.

# Super ugly numbers are positive numbers whose all prime factors 
# are in the given prime list primes of size k. For example, 
# [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the 
# first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.


from heapq import *

class Solution(object):
    
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        # [Ideas]
        # 1. next ugly number is composed by some ugly * prime
        #    => all existing ugly number * all_primes could be 
        #       next candidates
        #    => ensure all new ugly number multiplied by all primes
        # 2. P primes have P lanes, each start from 1st ugly number,
        #    multiply it, then 2nd, 3rd ... 
        # 3. how to find smallest next ugly? 
        #    => each time choose smallest in lane, update it,
        #    => fill smallest among lanes into solutions, then update it
        
        if n == 0: return 0
        
        val, idx = [1]*len(primes), [-1]*len(primes)
        nums = [0]*n
        
        for i in range(n):
            nums[i] = min(val)
            for j in range(len(primes)):
                if val[j] == nums[i]:
                    idx[j] += 1
                    val[j] = nums[idx[j]] * primes[j]
        # print(idx, val, nums)
        return nums[-1]
    
    
    
    def test(self):
        for i in range(15, 16):
            print(i, self.nthSuperUglyNumber(i, [2,7,13]))
            # [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
            
            
# Solution().test()
            