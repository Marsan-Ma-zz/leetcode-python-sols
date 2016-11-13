# # https://leetcode.com/problems/game-of-life/

# # According to the Wikipedia's article: 
# # "The Game of Life, also known simply as Life, is a cellular automaton 
# # devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
# using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.

# Follow up: 
# Could you solve it in-place? Remember that the board needs to be updated 
# at the same time: You cannot update some cells first and then use their 
# updated values to update other cells.

# In this question, we represent the board using a 2D array. 
# In principle, the board is infinite, which would cause problems when 
# the active area encroaches the border of the array. How would you address these problems?


from collections import defaultdict

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        # How can we store store the middle result without use extra space? encode:
        # living cells nearby | change | new value
        # <2        1->0     2
        # 2,3       1->1     1
        # >3        1->0     2
        # 3         0->1     3

        if not board or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, ele in enumerate(row):
                count = 0
                for a in xrange(max(0, i - 1), min(i + 2, m)):
                    for b in xrange(max(0, j - 1), min(j + 2, n)):
                        if (a, b) != (i, j) and 1 <= board[a][b] <= 2:
                            count += 1
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1

    #     self.board = board
    #     self.row, self.col = len(board), len(board[0])
    #     self.to_live, self.to_death = [], []
        
    #     # collect updates
    #     for i in range(self.row):
    #         for j in range(self.col):
    #             self.judge(i, j)
                
    #     # apply updates
    #     for i,j in self.to_live:
    #         self.board[i][j] = 1
    #     for i,j in self.to_death:
    #         self.board[i][j] = 0
            
    #     # return new_table
                
        
    # def judge(self, i, j):
    #     v = 0
    #     for m in range(-1, 2):
    #         if i+m < 0 or i+m >= self.row: continue
    #         for n in range(-1, 2):
    #             if j+n < 0 or j+n >= self.col: continue
    #             if (m != 0) or (n != 0):
    #                 if self.board[i+m][j+n]: v += 1
                        
    #     if self.board[i][j] and (v not in [2, 3]):
    #         self.to_death.append((i,j))
    #     elif (not self.board[i][j]) and (v == 3):
    #         self.to_live.append((i,j))
    #         