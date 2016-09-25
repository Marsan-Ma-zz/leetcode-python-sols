# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        len_a, len_b = len(a), len(b)
        
        if len_a == 0: return b
        if len_b == 0: return a
        
        if len_a < len_b:
            a, b = b, a
            len_a, len_b = len_b, len_a
            
        ci = '0'
        res = ''
        for i in range(len_a):
            if len_b-1-i >= 0:
                # print(len_b, i, a, b)
                vb = b[len_b-1-i]
            else:
                vb = '0'
            va = a[len_a-1-i]
            vv = [va, vb, ci].count('1')
            vs = '1' if vv in [1, 3] else '0'
            ci = '1' if vv in [2, 3] else '0'
            res = vs + res
        if ci == '1': res = ci + res
        return res

    def test(self):
        cases = [
            ['', ''],
            ['0', ''],
            ['', '1'],
            ['11', '1'],
            ['110', '1'],
            ['1011', '1'],
            ['1011', '11'],
        ]
        for a, b in cases:
            print(a, b, self.addBinary(a, b))
            
            
Solution().test()