# https://leetcode.com/problems/fraction-to-recurring-decimal/

# Given two integers representing the numerator and denominator of a fraction, 
# return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# For example,

# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        # boundary cases
        if denominator == 0:
            return None
        elif numerator == 0:
            return '0'
        
        # sign
        sign = '' if numerator * denominator > 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        
        # before decimal
        d, m = divmod(numerator, denominator)
        if m == 0:
            return sign+str(d)
        else:
            res = {0: sign+str(d) + '.'}
            
        # after decimal
        numerator = m
        history = {}
        ptr = 0
        while True:
            ptr += 1
            numerator *= 10
            d, m = divmod(numerator, denominator)
            
            res[ptr] = str(d)
            history[numerator] = ptr
            numerator = m
            
            if m == 0:
                return "".join([s for i, s in res.items()])
            
            next_num = m*10
            if next_num in history:
                res[history[next_num]] = '(' + res[history[next_num]]
                res[ptr] += ')'
                return "".join([s for i, s in res.items()])
                
            
            
            
    def test(self):
        cases = [
            (1, 0),
            (0, 1),
            (10, 3),
            (1, 2),
            (2, 1),
            (2, 3),
        ]
        for n, d in cases:
            print(n, d, self.fractionToDecimal(n, d))
        
                  
# Solution().test()