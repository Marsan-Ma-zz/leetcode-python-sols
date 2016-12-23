# https://leetcode.com/problems/word-ladder-ii/

# Given two words (beginWord and endWord), and a dictionary's word list, 
# find all shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.




import string
from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """

        # [Ideas]
        # 1. 2-way BFS, use dict[edge_node] = [[paths]] to record candidates
        # 2. this solution exceed memory, could only record node parent 
        #    instead of different paths to save memory
        
        
        idx2word = {i:w for i,w in enumerate(wordlist)}
        word2idx = {w:i for i,w in enumerate(wordlist)}
        
        def neighbors(widx):
            word = idx2word[widx]
            sols = []
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    if c == word[i]: continue
                    new_word = word[:i]+c+word[i+1:]
                    if new_word in word2idx:
                        sols.append(word2idx[new_word])
            return sols
            
        # 2-way BFS
        bidx, eidx = word2idx[beginWord], word2idx[endWord]
        left, right = {bidx: [[bidx]]}, {eidx: [[eidx]]}
        res = []
        while not res:
            # always search from shorter one
            if len(left) > len(right): 
                left, right = right, left
            
            # BFS
            new_left, sols = defaultdict(list), []
            for edge, rows in left.items():
                del left[edge] # save memory
                for nidx in neighbors(edge):
                    if nidx in rows: continue
                    if nidx in right:
                        sols.extend([lrow+rrow[::-1] for lrow in rows for rrow in right[nidx]])
                    else:
                        new_left[nidx].extend([row+[nidx] for row in rows])
            left = new_left
            if not left and not sols: return []  # solution not exists
            
            # solutions found
            if sols:
                for s in sols:
                    if s[0] == eidx: s = s[::-1]
                    res.append([idx2word[i] for i in s])
        return res
                
                