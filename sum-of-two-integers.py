# https://leetcode.com/problems/sum-of-two-integers/

# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example:
# Given a = 1 and b = 2, return 3.


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
    
        # [A tricky 3-line sol]
        # for _ in xrange(32):
        #     a, b = a^b, (a&b)<<1
        # return a if a & 0x80000000 else a & 0xffffffff
        
        
        # [Ideas]
        # 1. BEWARE NEGATIVE NUMBERS !!
        # 2. python has no interger bits bound, 
        #    we have to set this bound for 2's complement work
        #    so we could add negative numbers
    
        res = self.adder(a, b)
        # print("res", res, ci)
        
        # deal with negative number
        if res & 0x80000000:
            res = res ^ 0xffffffff
            res = -self.adder(res, 1) # 2's complement
        return res
    
    def adder(self, a, b):
        res, ci, mask = 0, 0, 1
        while mask <= 0x80000000:
            a1 = a & mask
            b1 = b & mask
            s  = a1 ^ b1 ^ ci
            res |= s
            # carry-in
            ci = (a1 & b1) | ((a1 | b1) & ci)
            ci = ci << 1
            mask = mask << 1
        return res
        
    
    def test(self):
        cases = [
            (0, 0),
            (0, 9),
            (1, 2),
            (7, 8),
            (9, 10),
            (12, 98),  # 1100 + 1100010 = 1101110 = 14 + 96 = 110
                       # 0111011
            (123, 321),
            (1212, 3434),
            (12345678, 87654321),
            (12345678, 87654322),
            (-1, 1),
            (-12345, 12345),
            (-12345, 12346),
            (-10, 22),
            (-12, -8),
            (-12, -34),
        ]
        for a, b in cases:
            print(a, b, self.getSum(a, b))
            
            
            
            
# Solution().test()
# print(0x7fffffff)