# https://leetcode.com/problems/powx-n/

# Implement pow(x, n).

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        
        1. brute force : loop and multiply x for n times. in n multiplex O(n)
        
        2. [idea] time complexity in O(log(2n)) -> O(log(n))
            if n = i + j, pow(x,n) = pow(x,i)*pow(x,j) => minimize i and j
            if m = log2(n), x*x -> x^2 * x^2 -> ... -> x^(m-1) * x^(m-1)
              Ex: n = 64, m = log2(64) = 6, x^64 = (x^32)^2 = (((((x^2)^2)^2)^2)^2)^2
                  n = 70 = 64 + 4 + 2
                  ans = x^n = x^(2^6+2^2+2^1) = x^(2^6) * x^(2^2) * x^(2^1)
                  
        3. [find factorized n] in time complexity O(log(n))
            n = 70, build binary representation of n
            n & 1, n >> 1, gather the factors of n
            
        4. [if n < 0]
            x^-n = 1 / x^n
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            negative = True
            n = -n
        else:
            negative = False
        
        # [find factorized n]
        factors = []
        pw = 0
        m = n
        while m >= 1:                  # m = 70, 35, 17, 8, 4, 2, 1    # m = 3, 1 
            if m & 1:                  # mod  0,  1,  1, 0, 0, 0, 1    # mod 1, 1    
                factors.append(pw)     # pow  0,  1,  2, 3, 4, 5, 6    # pow 0, 1
            pw += 1                    # factors = [1,2,6]             # factors = [0,1]
            m = m >> 1
        print(factors)
        
        # [do multiplex with DP]
        mul_nums = {0:x, 1:x*x}  # we need pow of x with m = [1,2,6] => we have ans = x^(2^6) * x^(2^2) * x^(2^1)
        for i in range(2, factors[-1]+1):  # we would have x^[(2^2),(2^3),(2^4),...,(2^6)]
            mul_nums[i] = mul_nums[i-1] * mul_nums[i-1]
        print(mul_nums)
        
        # [final multiplex]
        ans = 1
        for m in factors:  # factors = [1,2,6]
            ans *= mul_nums[m]
            
        if negative:
            return 1 / ans
        else:
            return ans
            
            