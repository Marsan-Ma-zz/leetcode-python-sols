# https://leetcode.com/problems/flip-game-ii/

# You are playing the following Flip Game with your friend: 
# Given a string that contains only these two characters: + and -, 
# you and your friend take turns to flip two consecutive "++" into 
# "--". The game ends when a person can no longer make a move and 
# therefore the other person will be the winner.

# Write a function to determine if the starting player can guarantee a win.

# For example, given s = "++++", return true. The starting player can 
# guarantee a win by flipping the middle "++" to become "+--+".

# Follow up:
# Derive your algorithm's runtime complexity.



class Solution(object):

    memo = {}
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in self.memo: return self.memo[s]

        for i in range(len(s)-1):
            if s[i:i+2] != '++': continue
            key = s[:i] + '--' + s[i+2:]
            self.memo[key] = self.canWin(key)
            if not self.memo[key]: return True
        return False
    #------------------------------------------------------------------
    # With memoization:  ~ 140 ms
    # The previous one reuses memoized results from previous test cases, 
    # but that's not why it's fast. It's almost as fast without that.

    class Solution(object):
        def canWin(self, s):
            memo = {}
            def can(s):
                if s not in memo:
                    memo[s] = any(s[i:i+2] == '++' and not can(s[:i] + '-' + s[i+2:])
                                  for i in range(len(s)))
                return memo[s]
            return can(s)


    #------------------------------------------------------------------
    # With memoization and counts instead of a string:  ~ 44 ms
    # Using tuples like (2, 3) to represent a state instead of strings like "-+++---++--".

    class Solution(object):
        def canWin(self, s):
            memo = {}
            def can(piles):
                piles = tuple(sorted(p for p in piles if p >= 2))
                if piles not in memo:
                    memo[piles] = any(not can(piles[:i] + (j, pile-2-j) + piles[i+1:])
                                      for i, pile in enumerate(piles)
                                      for j in range(pile - 1))
                return memo[piles]
            return can(map(len, re.findall(r'\+\++', s)))



    def test(self):
        cases = [
            '',
            '+',
            '++--',
            '+++++',
            '++++++',
            '+++++++',
            '++++++++',
        ]
        for c in cases:
            print(c, self.canWin(c)) # 8




# Solution().test()
