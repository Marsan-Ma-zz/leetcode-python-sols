# https://leetcode.com/problems/roman-to-integer/

# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        ss = [rom[c] for c in s]
        ans = 0
        last = 0
        while ss:
            c = ss.pop()
            ans += c if (c >= last) else -c
            last = c
        return ans
        