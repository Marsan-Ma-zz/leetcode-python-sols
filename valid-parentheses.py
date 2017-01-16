# https://leetcode.com/problems/valid-parentheses/

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid 
# but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # boundary cases
        
        
        # main process
        lefts, rights = ["(", "[", "{"], [")", "]", "}"]
        stack = []
        for idx, c in enumerate(s):
            if c in lefts:
                stack += [c]
            else:
                if len(stack) == 0:
                    return False
                l = stack.pop()
                if l+c not in ["()", "[]", "{}"]:
                    return False
        return (len(stack) == 0)
            