# https://leetcode.com/problems/wildcard-matching/

# Implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false


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
        # isMatch("aa", "*") → true
        # isMatch("aa", "a*") → true
        # isMatch("ab", "?*") → true
        # isMatch("aab", "c*a*b") → false
        
        # [Ideas]
        # 1. ? is no problem, focus on *
        # 2. while *, recursively check all combination until match found
        # 3. use DP table to avoid repeat computation
        # X. too much case, tend to miss
        #----------------------------------------------
        # 1. fully DP
        # 2. dp[si, pi] = first si char in s matching first pi char in p
        # 3. dp[0, 0] = True, dp[si, pi] depends on pi 
        
#         dp = [[False]*(len(p)+1) for _ in range(2)]
#         dp[0][0] = True
#         # print(len(dp), len(dp[0]))
        
#         if len(p) - p.count('*') > len(s): return False
        
#         for pi in range(1, len(p)+1):
#             dp[0][pi] = dp[0][pi-1] and (p[pi-1] == '*')
        
#         for si in range(1, len(s)+1):
#             for pi in range(1, len(p)+1):
#                 cur_s, cur_p = s[si-1], p[pi-1]
#                 if cur_p == '?':
#                     dp[1][pi] = dp[0][pi-1]
#                 elif cur_p != '*':
#                     dp[1][pi] = dp[0][pi-1] and (cur_s == cur_p)
#                 else: # '*'
#                     # dp[1][pi] = any([dp[t][pi-1] for t in range(si+1)])
#                     dp[1][pi] = dp[0][pi-1] or dp[0][pi]
#                     # print([dp[t][pi-1] for t in range(si)])
#                 # print(cur_s, cur_p, dp[si][pi])
        # return dp[-1][-1]
    
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        # print(dp)
        
        for i in p:
            if i != '*':
                # prevent overwrite dp[n-1], thus could use only 1 row dp
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                # '*' will propagate all through
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            # print(dp)
            dp[0] = dp[0] and i == '*'
            # print(dp)
        return dp[-1]
    
        
        # print(dp)
        
    
    def test(self):
        cases = [
            # ("aa","a"),
            # ("aa","aa"),
            # ("aaa","aa"),
            # ("aa", "*"),
            ("aaaa", "a*"),
            # ("ab", "?*"),
            # ("a", "?*"),
            # ("ab", "?*?"),
            # ("ab", "??*"),
            # ("ab", "???*"),
            # ("ab", "??????*"),
            # ("ab", "??*?"),
            # ("aab", "c*a*b"),   
            # ("aab", "*a*b"),   
            # ("aab", "*a*bc"),   ("babbaaababaaababaaabaaaabaaaabbbaabaabaaaaaababbabaabbbabbbaaabaaababbabbabaaaaabaabbbbbaabbaababaaabaaaabbaababbbabaaabababbbbaaabbabababbaaaabbaabaaabbaababbabababbbaaaaaaaabbabbbbaaaabaababbbbbbabbb", 
# "b***abbaaab*b***bb***b**ababa*abb**baa*ab*a*b*b*bbba****a**a***a*b***aa**abb**aa*bbbbaaba****a**bbb*b"),
        ]
        for s, p in cases:
            print(s, p, self.isMatch(s, p))
            
            
Solution().test()
# print(any([True, False]))