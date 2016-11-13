# https://leetcode.com/problems/word-search/

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# For example,
# Given board =

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        # [Ideas]
        # 1. [DFS] find the first char, 
        #     then recursively check valid next path.
        # 2. maybe record index and fail try, 
        #     to prevent try same route again (dynamic programming)

        if not word: return True
        if not board: return False

        self.board = board
        self.x_max, self.y_max = len(board), len(board[0])
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if (self.board[i][j] == word[0]): 
                    if (len(word) == 1) or self.dfs(word[1:], (i, j), [(i, j)]):
                        return True
        return False


    def dfs(self, word, pos, visited):
        x, y = pos
        cands = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        # print("cands", cands)
        cands = [(x, y) for x, y in cands if x>=0 and y>=0 and x<self.x_max and y<self.y_max and (x, y) not in visited]
        # print("cands", cands)
        for x, y in cands:
            if (self.board[x][y] == word[0]):
                if (len(word) == 1) or self.dfs(word[1:], (x, y), visited + [(x, y)]):
                    return True
        return False


    def test(self):
        board = [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E'],
        ]
        words = [
            "",
            "AB",
            "AS",
            "ASAS",
            "ASASASAS",
            "AE",
            "ABCCED",
            "ABCKCED",
            "SEE",
            "ABCB",
        ]
        for w in words:
            print(w, self.exist(board, w))


Solution().test()