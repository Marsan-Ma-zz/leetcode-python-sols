# https://leetcode.com/problems/power-of-three/

# Given an integer, write a function to determine if it is a power of three.

# Follow up:
# Could you do it without using any loop / recursion?


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n > 0) and (1162261467 % n == 0)


    # recursive sol
    def isPowerOfThree(n):
        return n>0 && (n==1 || (n%3==0 && isPowerOfThree(n/3)))

    # log sol
    def isPowerOfThree(n):
        return (math.log10(n) / math.log10(3)) % 1 == 0