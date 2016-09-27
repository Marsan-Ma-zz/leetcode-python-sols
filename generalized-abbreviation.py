# https://leetcode.com/problems/generalized-abbreviation/

# Write a function to generate the generalized abbreviations of a word.

# Example:
# Given word = "word", return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        
        # [ideas]
        # 1. dfs
        
        
        if not word: return ['']
        
        self.sols = []
        self.dfs("", word)
        return self.sols
    
    
    def dfs(self, abr, rest):
        if not rest:
            self.sols.append(abr)
        else:
            # transform some
            for i in range(1, len(rest)):
                new_abr = abr + "%i%s" % (i, rest[i])
                new_rest = rest[i+1:]
                self.dfs(new_abr, new_rest)
            # keep one
            self.dfs(abr + rest[0], rest[1:])
            # transform all rest
            self.sols.append("%s%i" % (abr, len(rest)))
            
            
    def test(self):
        cases = [
            "",
            "a",
            "abc",
            "word",
        ]
        for c in cases:
            print(c, self.generateAbbreviations(c))
            
            
# Solution().test()
