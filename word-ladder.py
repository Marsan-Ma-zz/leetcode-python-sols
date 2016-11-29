# https://leetcode.com/problems/word-ladder/

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        
        # [Ideas]
        # Single source shortest path => (BFS, Dijkstra's, A*)
        # => all edge in same weight, Dijkstra's = BFS
        # => no good estimate distance, A* not guarantee to be good
        # => so, BFS
        # => improve: bi-direction BFS
        
        ans = 1
        grp1, grp2 = {beginWord}, {endWord}
        wordList = wordList - grp1 - grp2
        
        while True:
            # print(grp1, grp2, wordList, ans)
            if (grp1 & grp2):
                return ans
            dics = wordList | grp2
            grp1 = [self.find_neighbors(w, dics) for w in grp1]
            grp1 = set(j for k in grp1 for j in k) # flatten
            wordList -= grp1
            ans += 1
            
            
            if len(grp1) == 0:
                return 0
            
            if len(grp1) > len(grp2):
                grp1, grp2 = grp2, grp1
                
        return 0
    
    
    def find_neighbors(self, w, dic):
        res = []
        # # [find neighbor by checking dictionary]
        # for d in dic:
        #     if self.is_neighbor(w, d):
        #         res.append(d)
        #---------------------------------------------
        # [find neighbor by checking possible mutation]
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(w)):
            for c in alpha:
                mut = w[:i] + c + w[i+1:]
                res.append(mut)
        # print(w, dic, res)
        res = set(res) & dic
        return res
    
                    
    def is_neighbor(self, w1, w2):
        cnt = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                cnt += 1
            if cnt > 1:
                return False
        return (cnt == 1)
            
            
    def test(self):
        cases = [
            ("", "", set([])),
            ("a", "b", set([])),
            ("aa", "kk", set([])),
            ("aa", "kk", set(["ak"])),
            ("hit", "cog", set(["hot","dot","dog","lot","log"])),
            ("hit", "cog", set(["hot","dot","dog","lot","log", "hog"])),
        ]
        for beginWord, endWord, wordList in cases:
            print(beginWord, endWord, self.ladderLength(beginWord, endWord, wordList))
    
                  
# Solution().test()
# print({'a'} - {'b'})