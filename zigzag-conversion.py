# https://leetcode.com/problems/zigzag-conversion/

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # [Example]
        # PAYPALISHIRING, numRows=3 => PAHNAPLSIIGYIR
        #----------------
        # P   A   H   N
        # A P L S I I G
        # Y   I   R
        #----------------
        # 0   4   8    12
        # 1 3 5 7 9 11 13
        # 2   6  10
        
        
        # [Ideas]
        # 1. use lists to dispatch characters one by one => O(n) time
        
        if numRows == 1:
            return s
        
        ans = ['' for i in range(numRows)]
        ptr, nxt = 0, 1
        
        for c in s:
            ans[ptr] += c
            if (ptr == 0 and nxt == -1) or (ptr == numRows-1 and nxt == 1):
                nxt = -nxt
            ptr += nxt
            
        return ''.join(ans)
            
            
    def test(self):
        cases = [
            ('', 3),
            ('abc', 1),
            ('abc', 3),
            ('abcde', 3),
            ('abcdefghifk', 3),
            ('PAYPALISHIRING', 3),
        ]
        for c, r in cases:
            print(c, self.convert(c, r))
            
            
# Solution().test()