# https://leetcode.com/problems/minimum-window-substring/

# Given a string S and a string T, find the minimum window in S 
# which will contain all the characters in T in complexity O(n).

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".

# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".

# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.


from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # [Examples]
        # S = "ADOBECODEBANC"
        # T = "ABC"
        # Minimum window is "BANC".
        
        # [Ideas]
        # 1. use hashmap to record nearest last requested char
        # 2. one-pass scan to and record the minimum
        
        if not s: return ''
        
        tbl = {k: [-1]*v for k, v in Counter(t).items()}
        res, flatten = None, []
        missing = len(t)
        for idx, c in enumerate(s):
            # update nearest table
            if (c in t):
                k = tbl[c].pop(0)
                tbl[c].append(idx)
                if k == -1: 
                    missing -= 1
                    if missing == 0: # initialize flatten values
                        flatten = sorted([j for k in tbl.values() for j in k])
                elif flatten:
                    flatten.remove(k)
                    flatten.append(idx)
                
            # start checking
            if missing == 0:
                min_val = flatten[0]
                cand = (min_val, idx+1)
                if (not res) or (res[1]-res[0] > cand[1]-cand[0]):
                    res = cand
        sol = s[res[0]:res[1]] if res else ''
        return sol
    
    
    def test(self):
        cases = [
            ('', 'aa'),
            ('a', 'aa'),
            ('ADOBECODEBANC', 'ABC'),   
            ('ADOBECODEBANC', 'OA'),   
            ('ADOBECODEKANC', 'BK'),   
            ('ADOBECODEKANC', 'BKK'),   
            ('ADOBECODEKANC', 'AKA'),
            ('ADOBECODEKANC', 'AKAA'),
            ('ADOBECODEKANC', 'AKC'),
            ('ADOBECODEKANC', 'AKCC'),
        ]
        for s, t in cases:
            print(s, t, self.minWindow(s, t))
            
            
# Solution().test()

# a = {'1': 0, '2': 2, '3': -1}
# sol = all([v >= 0 for v in a.values()])
# print(sol)