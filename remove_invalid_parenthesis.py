# https://leetcode.com/problems/remove-invalid-parentheses/

# Remove the minimum number of invalid parentheses in order to make 
# the input string valid. Return all possible results.

# Note: The input string may contain letters other than the parentheses ( and ).

# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]



class Solution(object):

    # BFS and use eval to check
    def removeInvalidParentheses(self, s):
        level = {s}
        while True:
            valid = []
            for s in level:
                try:
                    eval('0,' + filter('()'.count, s).replace(')', '),'))
                    valid.append(s)
                except:
                    pass
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}


    # another way
    def removeInvalidParentheses(self, s):
        def isvalid(s):
            s = filter('()'.count, s)
            while '()' in s:
                s = s.replace('()', '')
            return not s
        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}


    # def removeInvalidParentheses(self, s):
    #     """
    #     :type s: str
    #     :rtype: List[str]
    #     """
        
    #     # [Examples]
    #     # "()())()" -> ["()()()", "(())()"]
    #     # "(a)())()" -> ["(a)()()", "(a())()"]
    #     # ")(" -> [""]

        
    #     # [Ideas]
    #     # 1. recusive (slower) or analytic ways (danger while time limited)
    #     # 2. try remove 1 char at a time, see if "more valid". (BFS?)
    #     # 3. pre-process to remove special cases can't be valid
    #     # X. then pre-calculate minimum step count till valid
    #     # 5. use helper function "valid" and "bfs"
    #     # 6. O(n!) time complexity
    #     # 7. maybe DP to trim branches
    #     #---------------------------
    #     # 1. if we could know '(' or ')' to remove
    #     # 2. case: '((()))))()((((()' use stack to check max valid pairs
        
        
    #     if not s: return ['']
        
    #     sols = []
    #     s = self.trimmer(s)
    #     # print("start:", s)
        
    #     # bfs
    #     queue = [s]
    #     processed = [s]
    #     while queue:
    #         t = queue.pop(0)
    #         if sols and (len(t) < len(sols[0])):
    #             continue
    #         elif self.valid(t):
    #             sols.append(t)
    #         else:
    #             cnt_l, cnt_r = t.count('('), t.count(')')
    #             target = '(' if cnt_l > cnt_r else ')'
    #             for i in range(len(t)):
    #                 if t[i] == target:
    #                     nt = t[:i] + t[i+1:]
    #                     if nt not in processed: 
    #                         queue.append(nt)
    #                         processed.append(nt)
    #     if not sols: sols = ['']
    #     return sols
        
        
    # def trimmer(self, s):
    #     i, j = 0, len(s)-1
    #     while i < len(s) and s[i] == ')':
    #         i += 1
    #     while j > 0 and s[j] == '(':
    #         j -= 1
    #     return s[i:j+1]
        
        
    # def valid(self, s):
    #     cnt = 0
    #     for c in s:
    #         if c == '(':
    #             cnt += 1
    #         elif c == ')':
    #             cnt -= 1
    #         if cnt < 0:
    #             return False
    #     if cnt == 0:
    #         return True
        
        
    def test(self):
        cases = [
            None,
            ")",
            "(",
            "))",
            "()())()",
            "(a)())()",
            ")(",    
            "))))(((",
            "()()()()()()()()()()()",
            "()()()()()()())()()()()",
            "()()(a)()()(b)()()(c)()()",
            "(())))))()(()()x()(",
        ]
        for c in cases:
            print(c, self.removeInvalidParentheses(c))
        
        
# Solution().test()