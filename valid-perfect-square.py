# https://leetcode.com/problems/valid-perfect-square/

# Given a positive integer num, write a function which returns True 
# if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Returns: True
# Example 2:

# Input: 14
# Returns: False



class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        p1, p2 = 1, num // 2
        while p1 < p2:
            p = (p1 + (p2-p1)//2)
            t = p*p
            if t > num:
                p2 = p-1
            elif t < num:
                p1 = p+1
            else: # t == num
                return True
        return (num in [p1*p1, p2*p2])