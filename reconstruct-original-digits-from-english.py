# https://leetcode.com/problems/reconstruct-original-digits-from-english/

# Given a non-empty string containing an out-of-order English representation of digits 0-9, 
# output the digits in ascending order.

# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits. 
# That means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.

# Example 1:
# Input: "owoztneoer"

# Output: "012"
# Example 2:
# Input: "fviefuro"

# Output: "45"



from collections import Counter
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        # [Ideas]
        # 1. all even numbers got their unique char:
        #    z => zero, w => two, u => four, x => six, g => eight
        # 2. after even numbers removed with their unique char:
        #    o => one, h => three, f => five, v => seven, rest: nine
        
        raw = Counter(s)
        nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        nums = {n: Counter(s) for n, s in enumerate(nums)}
        
        sols = {k: 0 for k in range(10)}
        for char, num in zip('zwuxgohfvi', [0,2,4,6,8,1,3,5,7,9]):
            sols[num] = raw[char]
            for k,v in nums[num].items():
                raw[k] -= v*sols[num]
        return "".join(str(num)*cnt for num, cnt in sorted(sols.items()))
        
        
        