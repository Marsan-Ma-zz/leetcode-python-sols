# https://leetcode.com/problems/shortest-word-distance/

# Given a list of words and two words word1 and word2, return the 
# shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2, and word1 and 
# word2 are both in the list.



from collections import defaultdict

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        mem = defaultdict(list)
        for i, w in enumerate(words):
            mem[w].append(i)
            
        line1, line2 = mem[word1], mem[word2]
        p1, p2, best = 0, 0, float('inf')
        while p1 < len(line1) and p2 < len(line2):
            d = abs(line1[p1] - line2[p2])
            best = min(best, d)
            if line1[p1] > line2[p2]:
                p2 += 1
            else:
                p1 += 1
        return best
        
        