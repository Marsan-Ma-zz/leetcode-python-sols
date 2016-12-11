# https://leetcode.com/problems/dungeon-game/

# The demons had captured the princess (P) and imprisoned her in the bottom-right 
# corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. 
# Our valiant knight (K) was initially positioned in the top-left room and must 
# fight his way through the dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. 
# If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons, so the knight loses health (negative integers) 
# upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that 
# increase the knight's health (positive integers).

# In order to reach the princess as quickly as possible, the knight decides to move only 
# rightward or downward in each step.


# Write a function to determine the knight's minimum initial health so that he is able to 
# rescue the princess.

# For example, given the dungeon below, the initial health of the knight must be at least 7 
# if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

# -2 (K)  -3  3
# -5  -10 1
# 10  30  -5 (P)

# Notes:

# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight enters and the 
# bottom-right room where the princess is imprisoned.



class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        
        # [Examples]
        # -2     -3    3
        # -5    -10    1
        # 10     30   -5
        #
        
        # [ideas]
        # 1. start from right-bottom, propagate to top-left
        # 2. change "monster strength" into "life knight need"
        # 3. add dummy "life needed" as extra row, col
        
        if not dungeon or not dungeon[0]: return 1
        
        dp = dungeon
        m, n = len(dp), len(dp[0])
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i == m-1 and j == n-1: 
                    dp[i][j] = max(1, 1-dp[i][j])
                else:
                    cur = dp[i][j]
                    down = dp[i+1][j] if i+1 < m else float('inf')
                    right = dp[i][j+1] if j+1 < n else float('inf')
                    dp[i][j] = max(min(down-cur, right-cur), 1)
                
        for d in dp: print(d)
        return dp[0][0]
    
    
    def test(self):
        dg = [
            [-2, -3, 3],
            [-5, -10, 1],
            [10, 30, -5],
        ]
        print(self.calculateMinimumHP(dg))
        
        
# Solution().test()