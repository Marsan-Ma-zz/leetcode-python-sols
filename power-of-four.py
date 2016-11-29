# https://leetcode.com/problems/power-of-four/

# Given an integer (signed 32 bits), write a function to check 
# whether it is a power of 4.

# Example:
# Given num = 16, return true. Given num = 5, return false.

# Follow up: Could you solve it without loops/recursion?



def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<1:
            return False
        if num==1:
            return True
        if  num%2!=0:
            return False
        return (num&num-1)==0 and num&1431655765!=0#(2^30+2^28+2^26....2^0=1431655765)