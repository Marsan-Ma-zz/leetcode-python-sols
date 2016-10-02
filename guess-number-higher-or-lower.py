# https://leetcode.com/problems/guess-number-higher-or-lower/

# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I'll tell you whether the number is higher or lower.

# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
# Example:
# n = 10, I pick 6.

# Return 6.



class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. I guess ... it's binary search.
        
        p1, p2 = 1, n
        g = None
        
        while g != 0:
            p = p1 + (p2-p1)//2
            g = guess(p)
            print(p, p1, p2)
            if g == -1:
                p2 = p-1
            elif g == 1:
                p1 = p+1
        return p