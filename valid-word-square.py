# https://leetcode.com/problems/valid-word-square/

# Given a sequence of words, check whether it forms a valid word square.

# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

# Note:
# The number of words given is at least 1 and does not exceed 500.
# Word length will be at least 1 and does not exceed 500.
# Each word contains only lowercase English alphabet a-z.
# Example 1:

# Input:
# [
#   "abcd",
#   "bnrt",
#   "crmy",
#   "dtye"
# ]

# Output:
# true

# Explanation:
# The first row and first column both read "abcd".
# The second row and second column both read "bnrt".
# The third row and third column both read "crmy".
# The fourth row and fourth column both read "dtye".

# Therefore, it is a valid word square.
# Example 2:

# Input:
# [
#   "abcd",
#   "bnrt",
#   "crm",
#   "dt"
# ]

# Output:
# true

# Explanation:
# The first row and first column both read "abcd".
# The second row and second column both read "bnrt".
# The third row and third column both read "crm".
# The fourth row and fourth column both read "dt".

# Therefore, it is a valid word square.
# Example 3:

# Input:
# [
#   "ball",
#   "area",
#   "read",
#   "lady"
# ]

# Output:
# false

# Explanation:
# The third row reads "read" while the third column reads "lead".

# Therefore, it is NOT a valid word square.



class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        
        # [Examples]
        # [
        #   "abcd",
        #   "bnrt",
        #   "crm",
        #   "dt"
        # ]
        
        # [Ideas]
        # 1. check if the matrix is symmetry about the lefttop-rightbot
        #    diagonal line
        
        if not words: return True
        
        n = len(words)
        if n != len(words[0]): return False
        
        # fill matrix to square
        for i, row in enumerate(words):
            words[i] = row + ' '*(n-len(row))
        
        # check chars
        for i, row in enumerate(words):
            for j, c in enumerate(row):
                if j < i+1: 
                    continue
                elif c != words[j][i]:
                    return False
        return True
    
    
    def test(self):
        cases = [
            [],
            [
                "ab",
            ],
            [
                "ab",
                "c",
            ],
            [
                "ab",
                "b",
            ],
            [
                "abcd",
                "bnrt",
                "crmy",
                "dtye"
            ],
            [
                "abcd",
                "bnrt",
                "crm",
                "dt"
            ],
            [
                "ball",
                "area",
                "read",
                "lady"
            ],
        ]
        for c in cases:
            print(c, self.validWordSquare(c))
        
Solution().test()