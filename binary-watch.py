# https://leetcode.com/problems/binary-watch/

# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

# Each LED represents a zero or one, with the least significant bit on the right.


# For example, the above binary watch reads "3:25".

# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

# Example:

# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# Note:
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        
        # [ideas]
        # 1. first distribute num into num1 for hour and num2 for min
        # 2. counting combination
        
        if num < 0 or num > 9: return []
        
        dist = [(i, num-i) for i in range(4) if 0 <= num-i <=6]
        
        sols = [] 
        print(dist)
        for hs, ms in dist:
            for h in self.get_hours(hs):
                for m in self.get_mins(ms):
                    sols.append("%i:%02i" % (h, m))
        return sols
    
    
    def get_hours(self, hs):
        ans = [n for n in range(12) if self.bits(n) == hs]
        return ans
        
    def get_mins(self, ms):
        ans = [n for n in range(60) if self.bits(n) == ms]
        return ans
    
    
    def bits(self, n):
        cnt = 0
        while n > 0:
            if n % 2 == 1: 
                cnt += 1
            n = n >> 1
        return cnt
        
            
    def test(self):
        cases = [
            0,
            1,
            2,
            9,
            10,
            11,
        ]
        for c in cases:
            print(c, self.readBinaryWatch(c))
            
Solution().test()