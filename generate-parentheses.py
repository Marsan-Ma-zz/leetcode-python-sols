# https://leetcode.com/problems/generate-parentheses/

# Given n pairs of parentheses, write a function to generate all 
# combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(n, n, "", res)
        return res
        
    def dfs(self, left, right, st, res):
        if (left == right == 0):
            res.append(st)
        elif (left <= right):
            if left > 0: 
                self.dfs(left-1, right, st+"(", res)
            if right > 0: 
                self.dfs(left, right-1, st+")", res)
                
