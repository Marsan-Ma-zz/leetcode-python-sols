# https://leetcode.com/problems/regular-expression-matching/

# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        # [Examples]
        # isMatch("aa","a") → false
        # isMatch("aa","aa") → true
        # isMatch("aaa","aa") → false
        # isMatch("aa", "a*") → true
        # isMatch("aa", ".*") → true
        # isMatch("ab", ".*") → true
        # isMatch("aab", "c*a*b") → true
        
        
        # [Ideas]
        # 1. start from both header, '.' is no problem, focus on '*'
        # 2. while meet '*', do DFS to search for valid answer.
        # 3. maybe DP for early stopping duplicated branches
        #------------------------------------------
        # 1. use dynamic programming, boolean table[p][s] as match or not
        # 2. table size is len(p)+1 * len(s)+1 where table[0][0] is empty pairs ('', '')
        
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        table[0][0] = True

        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]
                        
        return table[-1][-1]
        
    # [Accepted Recursive Way, hard to implemented correctly within 1hr]
    # def dfs(self, s, p):
    #     # print("dfs:", s, p)
    #     p1, p2 = 0, 0
    #     key = "%s_%s" % (s, p)
    #     if key in self.dp: return self.dp[key]
    #     while p2 < len(p):
    #         if (p2+1 < len(p)) and (p[p2+1] == '*'):
    #             pre = p[p2]
    #             p2 += 2
    #             while p1 <= len(s):
    #                 # print("p1", p1)
    #                 if pre != '.' and s[p1:p1+1] != pre:
    #                     break
    #                 elif self.dfs(s[p1:], p[p2:]):
    #                     return True
    #                 p1 += 1
    #         elif (p1 < len(s)) and (p[p2] == '.'):
    #             p1, p2 = p1+1, p2+1
    #         elif (len(s[p1:]) == 0) or (s[p1] != p[p2]):
    #             self.dp[key] = False
    #             return False
    #         else: # s[p1] == p[p2]
    #             p1, p2 = p1+1, p2+1
    #     sol = (True if len(s[p1:]) == 0 else False)
    #     self.dp[key] = sol
    #     return self.dp[key]
            
            
    def test(self):
        cases = [
            ("aa","a"),
            ("aa","aa"),
            ("aaa","aa"),
            ("aaa","a*a"),
            ("aa", "a*"),
            ("aa", ".*"),
            ("ab", ".*"),
            ("abcde", ".*"),
            ("abcde", ".*e"),
            ("abcde", ".*de"),
            ("abcde", ".*cde"),
            ("abcde", ".*cfde"),
            ("abcde", ".*def"),
            ("aab", "c*a*b"),
            ("abcde", ".*.*"),
            ("abcde", ".*.*"),
            ("abcde", "...."),
            ("abcde", "....."),
            ("abcde", "..*.*.*.."),
            ("abcde", "..*.*.*........"),
            ("ab", ".*c"),
            ("aaa", "aaaa"),
            ("a", ".*..a*"),
            ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"),
        ]
        for s, p in cases:
            print(s, p, self.isMatch(s, p))
            
            
# Solution().test()
# import re

# print(re.search("a.*.*..", "aaaaabbb").group(0))