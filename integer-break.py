# https://leetcode.com/problems/integer-break/

# Given a positive integer n, break it into the sum of at least two positive integers 
# and maximize the product of those integers. Return the maximum product you can get.

# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

# Note: You may assume that n is not less than 2 and not larger than 58.

# Hint:

# There is a simple O(n) solution to this problem.
# You may check the breaking results of n ranging from 7 to 10 to discover the regularities.


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # [Examples]
        # 7 = [4,3=12, 3,3,1=9, 2,2,3=12] => 3,4=12
        # 8 = [4,4=16, 3,3,2=18, 2,2,4=16, 2,2,2,2=16] => 3,3,2=18
        # 9 = [5,4=20, 3,3,3=27, 2,2,2,3=24, 2,2,2,2,1=16] => 3,3,3=27
        # 10= [5,5=25, 3,3,4=36, 2,2,3,3=36] => 3,3,4=36
        
        # [Ideas]
        # 1. "for all integers n > 4, ( ( n-3 ) * 3 ) > n".
        # 2. suppose split n into x part,  
        #    => y = x^(n/x), y' = x^(n/x) * n/x^2 * (1-ln(x))
        #    => max when 1-ln(x) = 0, which means x = e, close to 2 or 3
        #    => for all 2*2*2 we could improved to 3*3 
        #    => thus prefer 3 than 2

        known = {2: 1, 3: 2, 4: 4}
        if n in known: return known[n]
        
        sol = 1
        while n > 4:
            sol *= 3
            n -= 3
        if n: sol *= n
        return sol
    
    
    def test(self):
        for i in range(2, 15):
            print(i, self.integerBreak(i))
            
            
# Solution().test()


# [full reason] 
# from https://discuss.leetcode.com/topic/43055/why-factor-2-or-3-the-math-behind-this-problem
        
# For convenience, say n is sufficiently large and can be broken into any smaller real positive numbers. We now try to calculate which real number generates the largest product.
# Assume we break n into (n / x) x's, then the product will be xn/x, and we want to maximize it.

# Taking its derivative gives us n * xn/x-2 * (1 - ln(x)).
# The derivative is positive when 0 < x < e, and equal to 0 when x = e, then becomes negative when x > e,
# which indicates that the product increases as x increases, then reaches its maximum when x = e, then starts dropping.

# This reveals the fact that if n is sufficiently large and we are allowed to break n into real numbers,
# the best idea is to break it into nearly all e's.
# On the other hand, if n is sufficiently large and we can only break n into integers, we should choose integers that are closer to e.
# The only potential candidates are 2 and 3 since 2 < e < 3, but we will generally prefer 3 to 2. Why?

# Of course, one can prove it based on the formula above, but there is a more natural way shown as follows.

# 6 = 2 + 2 + 2 = 3 + 3. But 2 * 2 * 2 < 3 * 3.
# Therefore, if there are three 2's in the decomposition, we can replace them by two 3's to gain a larger product.

# All the analysis above assumes n is significantly large. When n is small (say n <= 10), it may contain flaws.
# For instance, when n = 4, we have 2 * 2 > 3 * 1.
# To fix it, we keep breaking n into 3's until n gets smaller than 10, then solve the problem by brute-force.

