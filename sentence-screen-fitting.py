# https://leetcode.com/problems/sentence-screen-fitting/

# Given a rows x cols screen and a sentence represented by a list of words, find how many times the given sentence can be fitted on the screen.

# Note:

# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.
# Example 1:

# Input:
# rows = 2, cols = 8, sentence = ["hello", "world"]

# Output: 
# 1

# Explanation:
# hello---
# world---

# The character '-' signifies an empty space on the screen.
# Example 2:

# Input:
# rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

# Output: 
# 2

# Explanation:
# a-bcd- 
# e-a---
# bcd-e-

# The character '-' signifies an empty space on the screen.
# Example 3:

# Input:
# rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

# Output: 
# 1

# Explanation:
# I-had
# apple
# pie-I
# had--

# The character '-' signifies an empty space on the screen.


class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. just interative through row limit, count the result.
        #    any special problem? no need to worry punctuation.
        # 2. add dynamic programming, key is the start point of sentence
        #------------------------------------------
        # 1. alternatively use row to fit into sentence
        #    => start position + cols, then backward until meet ' '
        
        if not sentence or not rows or not cols: return 0
        
        sent = ' '.join(sentence) + ' '
        lsent = len(sent)
        
        # "abcde abc abcde abc "  # sent
        #  11111111
        #        22222222
        #            33333333
        #                  44444444
        
        
        pos = 0
        for i in range(rows):
            pos += cols
            while pos > 0 and sent[(pos) % lsent] != ' ':
                pos -= 1
            pos += 1
            # print(pos)
        
        return pos // lsent
    
        
        
    def test(self):
        cases = [
            ([], 4, 4),
            (['a', 'b'], 3, 1),
            (['a', 'b'], 3, 2),
            (['a', 'b'], 3, 3),
            (['a', 'b'], 3, 4),
            (["hello", "world"], 2, 4),
            (["hello", "world"], 2, 5),
            (["hello", "world"], 4, 6),
            # (["hello", "world"], 4, 8),
            # (["hello", "world"], 4, 10),
            # (["hello", "world"], 4, 11),
            # (["a", "bcd", "e"], 3, 6),
            # (["I", "had", "apple", "pie"], 4, 5),
            # (['f', 'p', 'a'], 8, 7),
            # (['a'], 100, 100),
        ]
        for sent, rows, cols in cases:
            print(sent, rows, cols, self.wordsTyping(sent, rows, cols))
            
            
# Solution().test()