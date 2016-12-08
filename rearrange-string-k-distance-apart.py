# https://leetcode.com/problems/rearrange-string-k-distance-apart/

# Given a non-empty string str and an integer k, rearrange the string such 
# that the same characters are at least distance k from each other.

# All input strings are given in lowercase letters. If it is not possible to 
# rearrange the string, return an empty string "".

# Example 1:
# str = "aabbcc", k = 3

# Result: "abcabc"

# The same letters are at least distance 3 from each other.
# Example 2:
# str = "aaabc", k = 3 

# Answer: ""

# It is not possible to rearrange the string.
# Example 3:
# str = "aaadbbcc", k = 2

# Answer: "abacabcd"

# Another possible answer is: "abcabcda"

# The same letters are at least distance 2 from each other.


from collections import Counter
from heapq import *

class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        
        # [Examples]
        # 1. str = "aabbcc", k = 3 => "abcabc"
        # 2. str = "aaabc", k = 3  => ""
        # 3. str = "aaadbbcc", k = 2 => "abacabcd"

        # [Ideas]
        # 1. greedy: count char number, sort, start from largest group
        # 2. place a => jump k spaces => place another
        # 3. then 2nd largest group, doing the same
        #    until finish or stocked
        # 4. how to prove it's the best strategy?
        #    => a__a__a___ 
        #    => ab_ab_ab__
        #    => abcabcab__
        #    => abcabcabd_  can't fit another d
        # X. any idea to make counter-example?
        #    => abcdabcd, k = 3
        #    => a__a____ will fail.
        #----------------------------
        # 1. still count, but don't sort. fill all chars unfullfilled
        #    per round.
        # X. abcdeabcdeaba fail => abcadebabcdea ok
        #----------------------------
        # 1. count char number, sort and push to heap
        #    every round (fill k chars) always fill chars with more
        #    count to fit.
        
        ans = []
        stat = [(-v, c) for c,v in Counter(str).items()]
        heapify(stat)    # max-heap
        k = max(1,k)
        
        while stat:
            tmp = []
            # 1 round fill chars
            for _ in range(k):
                if not stat: 
                    return '' if tmp else ans
                v, c = heappop(stat)
                ans.append(c)
                if v < -1:
                    tmp.append((v+1, c))
            # add back rest chars to heap
            for v, c in tmp:
                heappush(stat, (v,c))
        return ''.join(ans)
    
    def test(self):
        cases = [
            ('', 3),
            ('a', 2),
            ('aabbcc', 3),
            ('aaabc', 3),
            ('aaadbbcc', 2),
        ]
        for c, k in cases:
            print(c, self.rearrangeString(c, k))
            
# Solution().test()
