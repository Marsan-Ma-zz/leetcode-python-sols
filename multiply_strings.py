# Given two numbers represented as strings, return multiplication of the numbers as a string.

# Note:
# The numbers can be arbitrarily large and are non-negative.
# Converting the input string to integer is NOT allowed.
# You should NOT use internal library such as BigInteger.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # [Idea]
        # 1. multiply each digit in num2 with num1.
        # 2. carefully implement, especially carry-ins.

        if not num1 or not num2: return 0

        len1, len2 = len(num1), len(num2)

        res = ['0'] * (len1 + len2)
        lens = len(res)
        for i2 in range(len2):
            ci = 0
            d2 = int(num2[len2-i2-1])
            for i1 in range(len1):
                d1 = int(num1[len1-i1-1])
                sm = (d1*d2 + ci + int(res[lens-i1-i2-1]))
                ci = sm // 10
                sm = sm % 10
                res[lens-i1-i2-1] = str(sm)
            sm = ci + int(res[lens-len1-i2-1])
            res[lens-len1-i2-1] = str(sm)
                
        while (len(res) > 1) and (res[0] == '0'): res = res[1:]
        return ''.join(res)
    
    def test(self):
        cases = [
            ('0', '0'),
            ('1', '0'),
            ('10', '10'),
            ('99', '99'),
            ('123', '456'),
            ('999', '9999'),
        ]
        for n1, n2 in cases:
            res = self.multiply(n1, n2)
            print(n1, n2, res, int(n1)*int(n2))
            
Solution().test()            