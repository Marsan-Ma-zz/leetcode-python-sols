# https://leetcode.com/problems/word-search-ii/

# Given a 2D board and a list of words from the dictionary, 
# find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once in a word.

# For example,
# Given words = ["oath","pea","eat","rain"] and board =

# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].



class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        # 1. use complex number system to 2D => 1D hash
        # 2. [1j**i for i in range(4)] cover 4 direction
        # 3. prevent grid been reuse, hijack before dfs branch and 
        #    recover after done.
        # 4. use True with DFS to save time.
        
        # initial words trie
        root = {}
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})
            node[''] = True
        # print("trie_root:", root)
            
        # initial board hashmap
        m, n = len(board), len(board[0])
        tbl = {}
        for i in range(m):
            for j in range(n):
                tbl[i+j*1j] = board[i][j]
        # print("tbl:", tbl)
        
        # dfs
        sols = []
        def dfs(z, word, node):
            if node.pop('', None):  # prevent duplicate
                sols.append(word)
                
            c = tbl.get(z)
            if c in node:
                tbl[z] = None    # prevent grid been reuse
                for i in range(4):
                    dfs(z + 1j**i, word+c, node[c])
                tbl[z] = c       # add-back grid
                    
        for z, c in tbl.items():
            dfs(z, '', root)
                
        return sols
    
    
    def test(self):
        cases = [
            # (["aa"], ["aaa"]),
            (["oaan","etae","ihkr","iflv"], ["oath","pea","eat","rain"]),
        ]
        for tbl, words in cases:
            print(self.findWords(tbl, words))
            
            
Solution().test()