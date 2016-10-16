# https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6



from math import floor

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        # [Ideas]
        # 1. we know it's using stack
        # 2. it's all about be ware of the SIGN!!!
        
        if not tokens: return 0
        
        funcs = ['+', '-', '*', '/']
        stack = []
        for t in tokens:
            if t in funcs:
                b = stack.pop()
                a = stack.pop()
                if t == '/':
                    sign = (a<0) ^ (b<0)
                    t = eval("%s %s %s" % (abs(a), t, abs(b)))
                    if sign: t = -t
                else:
                    t = eval("%s %s %s" % (a, t, b))
                
            stack.append(int(float(t)))
            
        ans = int(float(stack.pop()))
        return ans
            
        
    def test(self):
        cases = [
            [],
            ["18"],
            ["2", "1", "+", "3", "*"],
            ["4", "13", "5", "/", "+"],
            ["4","-2","/","2","-3","-","-"],
            ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
        ]
        for c in cases:
            ans = self.evalRPN(c)
            print(c, ans)
            
            
# Solution().test()
# round("1.23")