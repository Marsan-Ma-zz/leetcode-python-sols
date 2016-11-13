# https://leetcode.com/problems/remove-k-digits/

# Given a non-negative integer num represented as a string, 
# remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.


class Solution(object):

    # use stack to remove larger previous digits
    def removeKdigits(self, num, k):
        out = []
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)
        return ''.join(out[:-k or None]).lstrip('0') or '0'


    # def removeKdigits(self, num, k):
    #     """
    #     :type num: str
    #     :type k: int
    #     :rtype: str
    #     """
        
    #     # [Examples]
    #     # num = "1432219", k = 3, Output: "1219"
    #     # num = "10200", k = 1, Output: "200"
    #     # num = "10", k = 2, Output: "0"
        
        
    #     # [Ideas]
    #     # 1. brute force: trace all possible combination by recursion
    #     # 2. if we have 0s within num[:k+1], eliminate numbers before 0s 
    #     #    is first priority
    #     # 3. suppose we are deling with num without 0 in num[:k+1]
    #     #    then we eliminate large MSB first:
    #     #    => as long as num[i] > num[i+1], remove num[i]
    #     #    => should consider num[:k], remove until meet minimum
    #     # 4. as progressing, k will consume and smaller
        
    #     if (not num) or (k == len(num)): return '0'
        
    #     # minimize MSB one digit by one
    #     msb = ''
    #     while num and (k > 0):ㄥ
    #         c = min(num[:k+1])
    #         i = num.index(c)
    #         msb += num[i]
    #         num = num[i+1:]
    #         k -= i
    #     ans = msb + num
        
    #     # special case: all numbers are ascending or equal
    #     if ans and (k > 0):
    #         ans = ans[:len(ans)-k]
        
    #     # remove trailing zero
    #     i = 0
    #     while ans and (i < len(ans)) and (ans[i] == '0'):
    #         i += 1
    #     ans = ans[i:]
    #     if len(ans) == 0:
    #         ans = '0'
    #     return ans
        
        
    def test(self):
        cases = [
            ('', 0),
            ('10', 1),
            ('1111111', 3),
            ('1430219', 3),
            ('1432219', 3),
            ('12321234543212321', 6),
            ('12321234543212321', 9),
            ('10200', 1),
            ('10', 2),
        ]
        for c, k in cases:
            print(c, k, self.removeKdigits(c, k))
            
            
# Solution().test()
