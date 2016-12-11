# https://leetcode.com/problems/longest-valid-parentheses/

# Given a string containing just the characters '(' and ')', find the length 
# of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is 
# "()()", which has length = 4.



class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # [Ideas]
        # 1. use stack to record '('
        # 2. each '(' also carry how many '()' close to it's left
        #    if this '(' got ')', then add himself plus valid '()' count 
        #    close to it's left.
        
        stack = []
        best, sol = 0, 0
        for c in s:
            if c == ')' and stack:
                sol += 2 + stack.pop()
                best = max(best, sol)
            elif c == '(':
                stack.append(sol) # '(' carry how many sol in it's left
                sol = 0
            else: # ')' and not stack
                stack = []
                sol = 0
        return best
    
    
    def test(self):
        cases = [
            '',
            '(',
            ')',
            '()',
            ')(',
            '))()()((',
            ')()())',
            ')()())))()()((',
            "()(()",
            "()(())",
            "(()",
            "((())))(",
        ]
        for c in cases:
            print(c, self.longestValidParentheses(c))
            
            
# Solution().test()
        