# https://leetcode.com/problems/sqrtx/

# Implement int sqrt(int x).

# Compute and return the square root of x.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        
        1. binary search from 1 to x/2 (sqrt(x) <= x/2 unless x < 2)
        Ex: x,lptr,rptr,ptr = (5,0,2,1)
           0 1 2
           l p r
               A       
        
        Ex: x,lptr,rptr,ptr = (10,0,5,2)
         0 1 2 3 4 5 
         l   p     r
               l p r    (next p=3+2//2=4)
               A
               
        Ex: x,lptr,rptr,ptr = (17,0,8,4)
         0 1 2 3 4 5 6 7 8
         l       p       r
                   l p   r    (p=5+3//2=6)
                   A
        ----------------------------
         l       p       r
         l     r p
                   
        [solution]: 
          1. if we got A**2 > x, return A-1, else return A (can't prove clearly)
          2. if we got p**2 == x, return p instantly.
        """
        # boundary cases
        if x == 0: return 0
        elif x < 4: return 1
        
        # binary search     
        lptr, rptr = 0, x//2                     # x=(8,0,4,2)
        while rptr > lptr:          
            ptr = lptr + (rptr - lptr)//2
            check = ptr*ptr        
            if check > x:                        
                rptr = ptr - 1
            elif check < x:
                lptr = ptr + 1                   #   (8,3,4,2)
            else: # ptr**2 == x
                return ptr
        return rptr if rptr**2 <= x else rptr-1
        