# https://leetcode.com/problems/remove-invalid-parentheses/
# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

# Note: The input string may contain letters other than the parentheses ( and ).

# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        # [Ideas]
        # 1. scan from left to right, cnt += 1 if '(', else -= 1 if ')'
        # 2. now we ensured count('(') <= count(')')
        # 3. then scan from right to left, cnt += 1 if ')', else -= 1 if '('
        # 4. now we ensured count('(') == count(')'), and valid

        # scan left to right
        cnt, res = 0, {s}
        for i, c in enumerate(s):
            if c == '(':
                cnt += 1
            elif (c == ')') and (cnt > 0):
                cnt -= 1
            else:  # (c == ')') and (cnt == 0)
                cuts = [j for j, w in s if (j <= i) and (w == ')')]
                res = {[self.cut_word(t) for t in cuts] for w in res}
                res = {j for k in res for j in k}   # flatten

        return res

    def cut_word(self, word, cut):
        if cut == len(word)-1:
            return word[:cut] + '_'
        else:
            return word[:cut] + '_' + word[cut+1:]


    def test(self):
        cases = [
            "",
            "()())()", #-> ["()()()", "(())()"]
            "(a)())()", #-> ["(a)()()", "(a())()"]
            ")(", #-> [""]
        ]
        for c in cases:


Solution().test()