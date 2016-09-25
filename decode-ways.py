# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.

class Solution(object):

    # [Idea]
    # 1. use recursive, each stage check decode ways from rest of string

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        
        res = [1 for _ in s]
        
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] in ['1', '2']:
                    res[i] = res[i-2]
                else:
                    return 0
            elif (s[i-1] != '0') and (int(s[i-1:i+1]) <= 26):
                res[i] = res[i-1] + (1 if i < 2 else res[i-2])
            else:
                res[i] = res[i-1]
                
        return res[-1]
        
        
            
    def test(self):
        cases = [
            "",
            "9",
            "12",
            "123",
            "1203",
            "234",
            "2034",
            "5678",
            "91011",
            "47575625458",
        ]
        for c in cases:
            print(c, self.numDecodings(c))
            
            
Solution().test()