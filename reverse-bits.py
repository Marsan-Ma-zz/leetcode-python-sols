# https://leetcode.com/problems/reverse-bits/

# Reverse bits of a given 32 bits unsigned integer.

# For example, given input 43261596 (represented in binary as 
# 00000010100101000001111010011100), return 964176192 
# (represented in binary as 00111001011110000010100101000000).

# Follow up:
# If this function is called many times, how would you optimize it?




class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        sol, mask = 0, 1 << 31            #  n=111001, sol=0
        while n:                          #   
            n, b = n >> 1, n & 1          #    11100 , 1...
            if b: sol += mask             #    1110  , 10...
            mask = mask >> 1              #    111   , 100...
        return sol                        #    11    , 1001..