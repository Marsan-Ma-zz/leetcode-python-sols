# https://leetcode.com/problems/single-number-ii/

# Given an array of integers, every element appears three times except for one. 
# Find that single one.


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # [Ideas]
        # 1. design a FSM counter (twos, ones): 00 -> 01 -> 10 -> 00
        #    which make 3 time nums disappear, leave only 1 time nums
        # 2. how to decide the change? by observation FSM above.
        #       curent  income  ouput
        #       ab      c/c       ab/ab
        #       00      1/0       01/00
        #       01      1/0       10/01
        #       10      1/0       00/10
        # 3. Observing only what make result '1', like digital circuit.
        #       a=~abc+a~b~c;
        #       b=~a~bc+~ab~c;
        #       [Note] they have to be run in parallel, since it's non-blocking circuit logic '<=' 
        
        ones, twos = 0, 0
        for n in nums:
            ones, twos = ~ones&twos&n | ones&~twos&~n, ~ones&~twos&n | ~ones&twos&~n
        print(ones, twos)
        return ones | twos
        