# https://leetcode.com/problems/word-squares/

# Given a set of words (without duplicates), find all word squares 
# you can build from them.

# A sequence of words forms a valid word square if the kth row and 
# column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

# For example, the word sequence ["ball","area","lead","lady"] forms 
# a word square because each word reads the same both horizontally and vertically.

# b a l l
# a r e a
# l e a d
# l a d y
# Note:
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example 1:

# Input:
# ["area","lead","wall","lady","ball"]

# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]

# Explanation:
# The output consists of two word squares. The order of output does 
# not matter (just the order of words in each word square matters).
# Example 2:

# Input:
# ["abat","baba","atan","atal"]

# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]

# Explanation:
# The output consists of two word squares. The order of output does 
# not matter (just the order of words in each word square matters).


from collections import defaultdict

class Solution(object):

    def wordSquares(self, words):
        n = len(words[0])
        fulls = defaultdict(list)
        for word in words:
            for i in range(n):
                fulls[word[:i]].append(word)
        def build(square):
            if len(square) == n:
                squares.append(square)
                return
            for word in fulls[''.join(zip(*square)[len(square)])]:
                build(square + [word])
        squares = []
        for word in words:
            build([word])
        return squares


    # def wordSquares(self, words):
    #     """
    #     :type words: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     self.words = words
    #     self.sols = []
    #     self.dp = defaultdict(list)
    #     for w in words:
    #         for i in range(1, len(w)):
    #             self.dp[w[:i]].append(w)
    #     self.dp[''] = words
    #     self.dfs([])
    #     return self.sols
            
        
    # def dfs(self, chosen):
    #     idx = len(chosen)
    #     # print(chosen)
    #     if chosen and (len(chosen) == len(chosen[0])): 
    #         self.sols.append(chosen)
    #         return
        
    #     prefix = ''.join([c[idx] for c in chosen])
    #     for p in self.dp[prefix]:
    #         self.dfs(chosen + [p])


    # def test(self):
    #     words = [
    #         ["abat","baba","atan","atal"],
    #         # ["area","lead","wall","lady","ball"],
    #     ]
    #     for w in words:
    #         print(self.wordSquares(w))



Solution().test()