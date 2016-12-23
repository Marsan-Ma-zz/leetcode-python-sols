# https://leetcode.com/problems/bitwise-and-of-numbers-range/

# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise 
# AND of all numbers in this range, inclusive.

# For example, given the range [5, 7], you should return 4.


from math import log
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. bits involving carry-in will be '0'
        # 2. if int(log2(n)) > int(log2(m)) then all bits will be '0'
        #    since all bits been carry-in when, like '11111' => '100000'
        # 3. check from both msb to lsb, stop when different,
        #    calculate both '1' count
        
        if not m or not n: return 0
        check = int(log(n, 2)) - int(log(m, 2))
        print(check)
        if check > 0: return 0
        
        mask = 1 << int(log(n, 2))
        cnt = 0
        while mask:
            a, b = m & mask, n & mask
            if a != b: break
            if a and b: cnt += mask
            mask = mask >> 1
        return cnt
        
        