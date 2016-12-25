# https://leetcode.com/problems/factor-combinations/

# Numbers can be regarded as product of its factors. For example,

# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.

# Note: 
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# Examples: 
# input: 1
# output: 
# []
# input: 37
# output: 
# []
# input: 12
# output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# input: 32
# output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]



class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        # [Ideas]
        # 1. recursively find next factor >= current factor 
        # 2. factor start from 2 to n**0.5
        #    
        
        def helper(num, lower):
            sols = []
            for i in range(lower, int(num**0.5)+1):
                if num % i == 0:
                    rest = helper(num//i, i) + [[num//i]]
                    sols.extend([[i] + t for t in rest])
            return sols
        
        return helper(n, 2)
    
    
    def test(self):
        cases = [
            2,
            8,
            37,
            16,
        ]
        for c in cases:
            print(c, self.getFactors(c))
            
# Solution().test()