# https://leetcode.com/problems/elimination-game/

# There is a list of sorted integers from 1 to n. Starting from left to right, 
# remove the first number and every other number afterward until you reach the end of the list.

# Repeat the previous step again, but this time from right to left, 
# remove the right most number and every other number from the remaining numbers.

# We keep repeating the steps again, alternating left to right and right to left, 
# until a single number remains.

# Find the last number that remains starting with a list of length n.

# Example:

# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6

# Output:
# 6



class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # [Ideas]
        # 1st round: remove all odd nums
        # 2nd round: 2 4 6 8 10 12 14 16 18 20 ...
        #         => remove 4k or 4k+2 depend on n//2 odd/even
        #         => Ex: 2 6 10 14 18 / or 4 8 12 16 20
        # 3rd round: 6 14 / or 8 16  (8k or 8k-2  depend on )
        # ------------------
        # 1. update and record head in each turn. when the total number becomes 1, 
        #    head is the only number left.
        # 2. When will head be updated?
        #    => if we move from left
        #    => if we move from right and the total remaining number % 2 == 1
        

        head, step, dir = 1, 1, 1
        while n > 1:
            if (dir == 1) or (dir == 0 and n % 2 == 1):
                head += step
            dir = dir ^ 1
            step *= 2
            n //= 2
        return head