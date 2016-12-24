# https://leetcode.com/problems/ternary-expression-parser/

# Given a string representing arbitrarily nested ternary expressions, 
# calculate the result of the expression. You can always assume that the given 
# expression is valid and only consists of digits 0-9, ?, :, T and F 
# (T and F represent True and False respectively).

# Note:

# The length of the given string is ≤ 10000.
# Each number will contain only one digit.
# The conditional expressions group right-to-left (as usual in most languages).
# The condition will always be either T or F. That is, the condition will never be a digit.
# The result of the expression will always evaluate to either a digit 0-9, T or F.


# Example 1:

# Input: "T?2:3"

# Output: "2"

# Explanation: If true, then result is 2; otherwise result is 3.
# Example 2:

# Input: "F?1:T?4:5"

# Output: "4"

# Explanation: The conditional expressions group right-to-left. Using parenthesis, 
# it is read/evaluated as:

#              "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
#           -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
#           -> "4"                                    -> "4"

# Example 3:

# Input: "T?T?F:5:3"

# Output: "F"

# Explanation: The conditional expressions group right-to-left. Using parenthesis, 
# it is read/evaluated as:

#              "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
#           -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
#           -> "F"                                    -> "F"




class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        
        # [Examples]
        # 1. "T?2:3" => 2
        # 2. "F?1:T?4:5" => 4
        # 3. "T?T?F:5:3" => F
        
        # [Ideas]
        # 1. use stack, do things like reverse-polish notation
        # 2. when meet '?', evaluate "condition",
        #    => then parse two items in, drop negative one
        #    => evaluate positive one
        # 3. use recursive for nested expression, only do one 
        #    '?/:' pair once in one recursion round.
        
        if not expression: return None
                
        sel = expression[0] == 'T'
        state = 0
        for i,c in enumerate(expression[2:]):
            if c == '?':
                state += 1
            elif c == ':' and state:
                state -= 1
            elif c == ':':
                if sel:
                    return self.parseTernary(expression[2:i+2])
                else:
                    return self.parseTernary(expression[i+3:])
        
        return None if state else expression
        
            
        
    def test(self):
        cases = [
            "T?2:3", # => 2
            "F?1:T?4:5", # => 4
            "T?T?F:5:3", # => F                        
        ]
        for c in cases:
            print(c, self.parseTernary(c))
            
# Solution().test()
