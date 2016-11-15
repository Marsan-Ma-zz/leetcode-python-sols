# https://leetcode.com/problems/alien-dictionary/

# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# For example,
# Given the following words in dictionary,

# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".

# Note:
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.



from collections import defaultdict

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        # [Ideas]
        # 1. collect directed graph edges, then do topological sort
        
        # build direct graph
        suc, pre = defaultdict(set), defaultdict(set)
        flag = False
        for pair in zip(words, words[1:]):
            if len(pair[1]) < len(pair[0]): flag = True
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
                
        if len(suc) == 0 and flag: return '' # for ['abcde', 'abc'] special case

        # very smart topological sort
        all_chars = set("".join(words))
        free = all_chars - set(pre)
        sol = ''
        while free:
            a = free.pop()
            sol += a
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]:
                    free.add(b)
        if (set(sol) != all_chars):
            sol = ''
        return sol
    
    
    def test(self):
        cases = [
            [],
            ["wrtkj","wrt"],
            ["wrt", "wrf", "er", "ett", "rftt"],
        ]
        for c in cases:
            print(c, self.alienOrder(c))
            
            
Solution().test()
