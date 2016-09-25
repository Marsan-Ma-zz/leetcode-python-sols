# Given a string s and a dictionary of words dict, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

        # [Idea]
        # 1. build a trie with dict
        # 2. recursively check header of string, 
        #    cast rest string to same function.

        if not wordDict:
            return False
        if not s:
            return True

        self.dic = wordDict
        self.memo = [None]*(len(s)+1) # memo handled substring by length
        return self.check_valid(s)


    def check_valid(self, s):
        if self.memo[len(s)] != None: 
            return self.memo[len(s)]
            
        if s == '':
            return True
        else:
            cands = []
            for d in self.dic:
                if (d == s[:len(d)]) and self.check_valid(s[len(d):]):
                    self.memo[len(s)] = True
                    return True
            # print("cands", cands)
            self.memo[len(s)] = False
            return False


    def test(self):
        cases = [
            ("", ['a']),
            ("leetcode", ["leet", "code"]),
            ("thisisgood", ["this", "is"]),
            ("thisisisgood", ["this", "is", "good"]),
            ("thsisgood", ["this", "is", "good"]),
        ]
        for s, d in cases:
            print(s, d, self.wordBreak(s, d))
            
            
Solution().test()