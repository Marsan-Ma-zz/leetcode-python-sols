# https://leetcode.com/problems/surrounded-regions/

# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X



class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        # [Ideas]
        # 1. BFS from all edge 'O', collect all "live O"
        # 2. other 'O' not in live is captured.
        # 3. at most visit all table, which is O(m*n)
        
        if not board or not board[0]: return
    
        m, n = len(board), len(board[0])
        live = [(i,j) for i, row in enumerate(board) for j, v in enumerate(row) 
            if v == 'O' and (i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1)
        ]
        while live:
            i, j = live.pop()
            board[i][j] = 'V'
            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    live.append((x,y))
            
        for i,row in enumerate(board):
            for j,v in enumerate(row):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'
        
            