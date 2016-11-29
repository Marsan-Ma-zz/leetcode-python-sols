# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

# Given an integer, write an algorithm to convert it to hexadecimal. 
# For negative integer, two’s complement method is used.

# Note:

# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number 
# is zero, it is represented by a single zero character '0'; otherwise, 
# the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the 
# number to hex directly.

# Example 1:

# Input:
# 26

# Output:
# "1a"
# Example 2:

# Input:
# -1

# Output:
# "ffffffff"



class Solution(object):


    # one-liner
    def toHex(self, num):
            return   ''.join(
                            '0123456789abcdef'[(num >> 4 * i) & 15] 
                            for i in range(8)
                            )[::-1].lstrip('0') or '0'

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num: return '0'
        mapper = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
 
        sign = (num < 0)
        if sign: num = abs(num)-1
        
        sol = ''
        while num:
            num, rest = divmod(num, 16)
            if sign: rest = 15-rest
            c = str(rest) if rest < 10 else mapper[rest]
            sol = c + sol
        
        if sign:
            sol = 'f'*(8-len(sol)) + sol
        return sol

