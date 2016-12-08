# https://leetcode.com/problems/word-break-ii/

# Given a string s and a dictionary of words dict, add spaces in s to 
# construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].



class Solution(object):

    # DFS with DP
    def wordBreak(self, s, wordDict):
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = []
                for j in range(i+1, len(s)+1):
                    if s[i:j] in wordDict:
                        for tail in sentences(j):
                            if tail != '': tail = ' ' + tail
                            memo[i].append(s[i:j] + tail)
            return memo[i]
        sol = sentences(0)
        return sol

    # normal order DP
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: Set[str]
#         :rtype: List[str]
#         """
        
#         dp = {-1: ['']}
#         wordDict = [(w, len(w)) for w in wordDict]
        
#         for i, c in enumerate(s):
#             dp[i] = []
#             for w, l in wordDict:
#                 if dp.get(i-l) and s[i-l+1:i+1] == w:
#                     for pw in dp[i-l]:
#                         sol = pw + ' ' + w if pw else w
#                         dp[i].append(sol)
#         # print(dp)
#         return dp[len(s)-1]
    
    def test(self):
        cases = [
            ("", ["cat", "cats", "and", "sand", "dog"]),
            ("", ["cat", "cats", "and", "sand"]),
            ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
            ("catsandcatsanddog", ["cat", "cats", "and", "sand", "dog"]),
("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]),
        ]
        for s, d in cases:
            print(self.wordBreak(s, d))
            
Solution().test()

# print(['' and ' ' + ''])