# https://leetcode.com/problems/flip-game/

# You are playing the following Flip Game with your friend: 
# Given a string that contains only these two characters: + and -, 
# you and your friend take turns to flip two consecutive "++" into 
# "--". The game ends when a person can no longer make a move and 
# therefore the other person will be the winner.

# Write a function to compute all possible states of the string after one valid move.

# For example, given s = "++++", after one move, it may become one of the following states:

# [
#   "--++",
#   "+--+",
#   "++--"
# ]
# If there is no valid move, return an empty list [].




class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]

        [example]
            s = "++++" 
            [
              "--++",
              "+--+",
              "++--"
            ]
        [idea]
            1. start from first char, one pass through each char.
            2. check for '++' and replace it to be '--', append results.
        
        """
        # boundary case
        if not s: return []
        
        
        # main
        results = []
        for i in range(len(s)):
            if s[i:i+2] == '++':
                ans = s[:i] + '--' + s[i+2:]
                results.append(ans)
        return results
    
#     def unit_test(self):
#         cases = [
#             None,
#             "",
#             "+",
#             "++",
#             "+++",
#             "++++",
#             "++-++----+",
#         ]
#         for case in cases:
#             ans = self.generatePossibleNextMoves(case)
#             print(case, "/", ans)
            
            
# # Solution().unit_test()