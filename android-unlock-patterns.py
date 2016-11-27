# https://leetcode.com/problems/android-unlock-patterns/

# Given an Android 3x3 key lock screen and two integers m and n, 
# where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns 
# of the Android lock screen, which consist of minimum of m keys and maximum n keys.

# Rules for a valid pattern:
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern 
# passes through any other keys, the other keys must have previously 
# selected in the pattern. No jumps through non selected key is allowed.
# The order of keys used matters.

# Explanation:
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# Invalid move: 4 - 1 - 3 - 6 
# Line 1 - 3 passes through key 2 which had not been selected in the pattern.

# Invalid move: 4 - 1 - 9 - 2
# Line 1 - 9 passes through key 5 which had not been selected in the pattern.

# Valid move: 2 - 4 - 1 - 3 - 6
# Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

# Valid move: 6 - 5 - 4 - 1 - 9 - 2
# Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

# Example:
# Given m = 1, n = 1, return 9.


from collections import defaultdict

class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # [Example]
        # | 1 | 2 | 3 |
        # | 4 | 5 | 6 |
        # | 7 | 8 | 9 |

        # [Ideas]
        # 1. it's a graph but keep varying (passed key could be crossed)
        # 2. can't use dynamic programming (not stateless, graph varying)
        # 3. OMG ...
        #------------------------------------------
        # 1. we could regard crossing duplicate grid as edge without weight
        #    since crossing some other node have unique destiny:
        #    ex: 123, 159, 258, only these 3 kinds.
        # 2. we use DFS to traverse all solutions.
        # 3. we only traverse from 1, 2, 5, since others are symmetrics.
        #    and multiply solutions from 1,2 by 4 times
        
        
        # graph
        self.invalid = {
            1: [3,7,9],
            2: [8],
            3: [1,7,9],
            4: [6],
            5: [],
            6: [4],
            7: [1,3,9],
            8: [2],
            9: [1,3,7],
        }
        
        self.lut = defaultdict(int)
        self.m, self.n = m, n
        self.dfs([1])
        self.dfs([2])
        self.dfs([5])
        # print(self.lut)
        # print(self.m, self.n)
        return sum(self.lut.values())
                 
        
    def dfs(self, seq):
        cur, l = seq[-1], len(seq)
        if self.m <= l <= self.n:
            self.lut[l] += (1 if seq[0] == 5 else 4)
            # print(self.lut)
        if l < self.n:
            # print(l)
            for i in range(1,10):
                if i in seq: 
                    continue
                elif (i in self.invalid[cur]) and ((i+cur)//2 not in seq):
                    continue
                else:
                    self.dfs(seq+[i])


    def test(self):
        cases = [
            (1,1),
            (2,2),
            (3,3),
            (1,2),
            (1,3),
        ]
        for m, n in cases:
            print((m,n),self.numberOfPatterns(m,n))
            
            
Solution().test()
# print(1 <= 3 <= 5)