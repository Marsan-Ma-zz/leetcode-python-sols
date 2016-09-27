from collections import defaultdict

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        
        self.board = board
        self.row, self.col = len(board), len(board[0])
        self.to_live, self.to_death = [], []
        
        # collect updates
        for i in range(self.row):
            for j in range(self.col):
                self.judge(i, j)
                
        # apply updates
        for i,j in self.to_live:
            self.board[i][j] = 1
        for i,j in self.to_death:
            self.board[i][j] = 0
            
        # return new_table
                
        
    def judge(self, i, j):
        v = 0
        for m in range(-1, 2):
            if i+m < 0 or i+m >= self.row: continue
            for n in range(-1, 2):
                if j+n < 0 or j+n >= self.col: continue
                if (m != 0) or (n != 0):
                    if self.board[i+m][j+n]: v += 1
                        
        if self.board[i][j] and (v not in [2, 3]):
            self.to_death.append((i,j))
        elif (not self.board[i][j]) and (v == 3):
            self.to_live.append((i,j))
            