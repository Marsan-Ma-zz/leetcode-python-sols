# https://leetcode.com/problems/guess-number-higher-or-lower-ii/

# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

# However, when you guess a particular number x, and you guess wrong, you pay $x. You win 
# the game when you guess the number I picked.

# Example:

# n = 10, I pick 8.

# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.

# Game over. 8 is the number I picked.

# You end up paying $5 + $7 + $9 = $21.
# Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.



class Solution(object):


    # bottom-up ver. (https://discuss.leetcode.com/topic/51356/two-python-solutions)
    def getMoneyAmount(self, n):
        need = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi])
                                   for x in range(lo, hi))
        return need[1][n]


    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. find "worst value" rather than "expected value"
        # 2. recursive find worst case, than select minimum of cases
        #    (the idea of MinMax)
        # 3. use DP to avoid repeating done case
        # 4. base case:
        #    => 1 value: no cost
        #    => 2 value: select lower number
        #    => 3 value: select mid number
        
        dp = [[None]*(n+1) for _ in range(n+1)]
        
        def helper(lo, hi):
            if dp[lo][hi] == None:
                diff = hi - lo
                if diff == 0:
                    sol = 0
                elif diff == 1:
                    sol = lo
                elif diff == 2:
                    sol = lo+1
                else: # diff >= 3
                    sol = float('inf')
                    for i in range(lo, hi):
                        s = i + max(helper(lo, i-1), helper(i+1, hi))
                        sol = min(sol, s)
                dp[lo][hi] = sol
            return dp[lo][hi]
        
        return helper(0, n)
    
    def test(self):
        for i in range(15):
            print(i, self.getMoneyAmount(i))
            
            
# Solution().test()
        
        