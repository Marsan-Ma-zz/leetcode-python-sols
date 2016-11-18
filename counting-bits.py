# https://leetcode.com/problems/counting-bits/

# Given a non negative integer number num. For every numbers i in 
# the range 0 ≤ i ≤ num calculate the number of 1's in their binary 
# representation and return them as an array.

# Example:
# For num = 5 you should return [0,1,1,2,1,2].

# Follow up:

# It is very easy to come up with a solution with run time 
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly 
# in a single pass?

# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function 
# like __builtin_popcount in c++ or in any other language.



class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        # [Examples]
        # 1. [0,1,1,2,1,2,2,3,1,2, 2, 3, 2, 3, 3, 4, 1, 2, 2]
        #    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        
        #    
        
        # [Ideas]
        # 1. even number will carry-in, bit count tend to maintain or reduce
        # 2. all odd number = last bit-count + 1
        #    all 2**i = 1
        #    every time pass 2**i, restart the routine from 0 
        #    but add one bit, the highest bit.
        
        
        sol = [0,1,1]
        
        last_2exp = 2
        for i in range(3, num+1):
            if i == last_2exp*2:
                last_2exp *= 2
                sol.append(1)
            else:
                sol.append(1 + sol[i-last_2exp])
                
        return sol[:num+1]
    
    
    def test(self):
        for i in range(15):
            print(i, self.countBits(i))

            
# Solution().test()