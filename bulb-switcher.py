# https://leetcode.com/problems/bulb-switcher/

# There are n bulbs that are initially off. You first turn on all 
# the bulbs. Then, you turn off every second bulb. On the third round, 
# you toggle every third bulb (turning on if it's off or turning off 
# if it's on). For the ith round, you toggle every i bulb. For the nth 
# round, you only toggle the last bulb. Find how many bulbs are on 
# after n rounds.

# Example:

# Given n = 3. 

# At first, the three bulbs are [off, off, off].
# After first round, the three bulbs are [on, on, on].
# After second round, the three bulbs are [on, off, on].
# After third round, the three bulbs are [on, off, off]. 

# So you should return 1, because there is only one bulb is on.


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. it's the n doors same problem. all factors is paired
        #    except sequared number like 1, 4, 9, 16, 25
        
        sol = 0
        for i in range(1, int(n**0.5)+1):
            if i * i <= n:
                sol += 1
                
        return sol 

    def test(self):
        cases = [
            0, 1, 2, 5, 10, 15
        ]
        for c in cases:
            print(c, self.bulbSwitch(c))
            
# Solution().test()
