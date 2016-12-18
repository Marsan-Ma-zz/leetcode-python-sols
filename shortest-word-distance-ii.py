# https://leetcode.com/problems/shortest-word-distance-ii/

# This is a follow up of Shortest Word Distance. The only difference is now you are 
# given the list of words and your method will be called repeatedly many times with 
# different parameters. How would you optimize it?

# Design a class which receives a list of words in the constructor, and implements a 
# method that takes two words word1 and word2 and return the shortest distance between 
# these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.



class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.stat = {}
        for i, w in enumerate(words):
            self.stat[w] = self.stat.get(w, []) + [i]
        

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1, idx2 = self.stat[word1], self.stat[word2]
        best, p1, p2 = float('inf'), 0, 0
        while p1 < len(idx1) or p2 < len(idx2):
            id1, id2 = idx1[p1], idx2[p2]
            best = min(best, abs(id1-id2))
            if id1 >= id2 and p2 < len(idx2)-1: 
                p2 += 1
            elif p1 < len(idx1)-1:
                p1 += 1
            elif p2 < len(idx2)-1:
                p2 += 1
            else:
                break
            
        
        return best


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")