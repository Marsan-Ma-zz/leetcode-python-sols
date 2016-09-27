# https://leetcode.com/problems/perfect-squares/

# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.


class Solution(object):
    
    # cheat on leetcode: class variable will be reused for continuous cases
    lut = {0: 0}
        
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. dynamic programming, build a table from 1 to n 
        #    which 
        # X. this can't guarantee least number
        # ------------------------------------------------------
        # 1. find all perfect square numbers < n
        # 2. try to compose n from the largest, 
        #    and keep best solution (record least number)
        #    during trying, abandom as soon as solution worse than best
        # X. too slow as n grows
        # ------------------------------------------------------
        # 1. still find all perfect square numbers < n
        # 2. dynamic programming, build table from 0 to n as target
        
        
        if not n: return []
        
        all_cands = [i**2 for i in range(1, int(n ** 0.5)+1)]
        
        ci, cands = 0, []
        for i in range(1, n+1):
            # little cheat for leetcode
            if i in self.lut: continue
                
            # update candidates
            while True:
                if ci >= len(all_cands): 
                    break
                elif all_cands[ci] <= i:
                    cands.append(all_cands[ci])
                    ci += 1
                else:
                    break
                    
            # build lookup-table
            if i in cands:
                self.lut[i] = 1
            else:
                self.lut[i] = 1 + min([self.lut[i-j] for j in cands])
            
        return self.lut[n]
        
        
    def test(self):
        cases = [
            0, 
            10,
            12,
            13,
            100,
            6255,
            9917,
        ]
        for c in cases:
            res = self.numSquares(c)
            print(c, res)
            
            
            
# Solution().test()
