# https://leetcode.com/problems/valid-sudoku/

# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


# A partially filled sudoku which is valid.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.



class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # [Ideas]
        # 1. valid row, col, X, and each 3x3 grid
        
        
        # rows
        for row in board:
            if not self.valid(row): return False
        
        # cols
        for col in range(9):
            line = [row[col] for row in board]
            # print(line)
            if not self.valid(line): return False
            
        # # X
        # line = [board[i][i] for i in range(9)]
        # # print(line)
        # if not self.valid(line): return False
        # line = [board[i][8-i] for i in range(9)]
        # # print(line)
        # if not self.valid(line): return False
        
        # each 9-grid
        for i in range(3):
            for j in range(3):
                line = []
                for m in range(3):
                    for n in range(3):
                        line.append(board[i*3+m][j*3+n])
                # print(line)
                if not self.valid(line): return False
        return True
    
    
    def valid(self, line):
        line = [n for n in line if n != '.']
        sol = (len(set(line)) == len(line))
        if not sol: print(line)
        return sol
        
    
    
    
    def test(self):
        board = ["........2",
                 "......6..",
                 "..14..8..",
                 ".........",
                 ".........",
                 "....3....",
                 "5.86.....",
                 ".9....4..",
                 "....5...."]
#         board = [
#             ['1','2','3', '.','.','.', '.','.','8'],
#             ['4','5','6', '.','.','.', '.','.','.'],
#             ['7','8','9', '.','.','.', '.','.','.'],
            
#             ['.','.','.', '.','.','.', '.','.','.'],
#             ['.','.','.', '.','4','.', '.','.','.'],
#             ['.','.','.', '.','.','.', '.','.','.'],
            
#             ['.','.','.', '.','.','.', '.','.','.'],
#             ['.','.','.', '.','.','.', '.','.','.'],
#             ['9','.','.', '.','.','.', '.','.','7'],
#         ]
        print(self.isValidSudoku(board))
        
        
# Solution().test()