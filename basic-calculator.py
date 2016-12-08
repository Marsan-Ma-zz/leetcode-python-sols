# https://leetcode.com/problems/basic-calculator/

# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ), 
# the plus + or minus sign -, non-negative integers and empty spaces .

# You may assume that the given expression is always valid.

# Some examples:
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23



class Solution(object):

    def calculate(self, s):
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':
                signs.pop()
            i += 1
        return total


    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        # [Examples]
        # "1 + 1" = 2
        # " 2-1 + 2 " = 3
        # "(1+(4+5+2)-3)+(6+8)" = 23
        
        # [Ideas]
        # 1. only +/- => remove () and adjust sign accordingly
        
        sign, stack = 0, []
        s = ['+'] + [c for c in s if c != ' ']
        for i in range(len(s)):
            # change sign
            if s[i:i+2] == ['-', '(']:
                sign = 1^sign
                stack.append(1)
                s[i+1] = ' '
                s[i] = '-' if sign else '+'
            elif s[i:i+2] == ['+', '(']:
                stack.append(0)
                s[i+1] = ' '
                s[i] = '-' if sign else '+'
            elif s[i] == ')':
                if stack.pop():
                    sign = 1^sign
                s[i] = ' '
            elif sign: # reverse sign
                if s[i] == '-': 
                    s[i] = '+'
                elif s[i] == '+': 
                    s[i] = '-'
            
        s = [c for c in s if c != ' '][1:] + ['+']
        sol = 0
        sign, tmp = 0, ''
        for i in range(len(s)):
            if s[i].isdigit():
                tmp += s[i]
            else: # +/-
                sol += -int(tmp) if sign else int(tmp)
                sign = 0 if s[i] == '+' else 1
                tmp = ''
                # print(i, sol)
        return sol
        
        
    def test(self):
        cases = [
            "1 + 1", # = 2
            " 2-1 + 2 ", # = 3
            "(1+(4+5+2)-3)+(6+8)", # = 23
            "(1-(4+5+2)-3)-(6+8)", # = 23
            "(1-(4+(5-(4-6)+2))-3)-(6+8)", # = 23
        ]
        for c in cases:
            print(eval(c), self.calculate(c))
        
        
# Solution().test()
