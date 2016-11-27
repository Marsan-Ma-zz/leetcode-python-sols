# https://leetcode.com/problems/decode-string/

# Given an encoded string, return it's decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string 
# inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; 
# No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not 
# contain any digits and that digits are only for those repeat numbers, 
# k. For example, there won't be input like 3a or 2[4].

# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


# [Python regex]
# https://docs.python.org/3/library/re.html

# regex
import re
class Solution(object):
    def decodeString(self, s):
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s



class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # [Examples]
        # s = "3[a]2[bc]", return "aaabcbc".
        #     => stack as [(3, a), (2, bc)]
        # s = "3[a2[c]]", return "accaccacc".
        #     => stack as [(3, a, (2, c))]
        #     => [(3, a, (2, c))]
        # s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
        #     => stack as [(2, abc), (3, cd), ed]
        # s = "3[a2[c3[d4[e]]]]", return "accaccacc".
        #     => [(3, a2[c3[d4[e]]])]
        #     => [(3, [a, (2, [c3[d4[e]]])])]
        #     => [(3, [a, (2, [c, (3, [d4[e]])] ])])]
        
        # [Ideas]
        # 1. stack them for later use
        #    a) meet '[', stack everything until corresponding ']',
        #       including nested sub '[]', for later pop and deal
        #    b) meet (a-z) to (0-9), stack (a-z), and vice versa.
        # 2. pop them for perform operators
        #    a) pop includes '[]', further parse
        #    b) pop not include '[]', multiply with next (if number)
        #    c) pop and no following number, just append
        #------------------------------------------------
        # 1. or, maybe we just leave all the parsing to recursion,
        #    a) digit: parse until get (num, nested_[])
        #    b) alphabat: parse until meet digit
        
        if not s: return ''
        
        cmds = self.parse(s)
        sol = self.decode(cmds)
        return sol
        
        
        
    def decode(self, cmds):
        if not cmds: 
            return ''
        elif not isinstance(cmds[0], list):
            return cmds[0] + self.decode(cmds[1:])
        else:
            current = self.decode(cmds[0][1]) * int(cmds[0][0])
            return current + self.decode(cmds[1:])
    
    
    
    def parse(self, s):
        if s == '':   # parse ended
            return []
        elif not s[0].isdigit():    # all txt
            i = 1
            while (i < len(s)) and (not s[i].isdigit()):
                i += 1
            rests = self.parse(s[i:]) if s[i:] else []
            return [s[:i]] + rests
        elif s[0].isdigit():    # should be (num, [...]) pair
            # find mutiplexer
            i = 0
            while s[i].isdigit():
                i += 1
            cnt = s[:i]    # s[i] must be '['
            
            # find end of nested []
            nest = 1 # for current s[i] == '['
            i = start = i + 1
            while nest > 0:
                if s[i] == '[':
                    nest += 1
                elif s[i] == ']':
                    nest -= 1
                i += 1
            content = s[start:i-1]
            rests = self.parse(s[i:]) if s[i:] else []
            return [[cnt, self.parse(content)]] + rests
        
        
    def test(self):
        cases = [
            '',
            "3[a]2[bc]", # "aaabcbc".
            "3[a2[c]]", # "accaccacc".
            "2[abc]3[cd]ef", # "abcabccdcdcdef".
        ]
        for c in cases:
            print(c, '=>', self.decodeString(c))
            
            
# Solution().test()