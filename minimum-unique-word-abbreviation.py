# https://leetcode.com/problems/minimum-unique-word-abbreviation/

# A string such as "word" contains the following abbreviations:

# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", 
# "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

# Given a target string and a set of strings in a dictionary, find an 
# abbreviation of this target string with the smallest possible length 
# such that it does not conflict with abbreviations of the strings in the dictionary.

# Each number or letter in the abbreviation is considered length = 1. For example, 
# the abbreviation "a32bc" has length = 4.

# Note:
# In the case of multiple answers as shown in the second example below, you may 
# return any one of them.
# Assume length of target string = m, and dictionary size = n. You may assume that 
# m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.

# Examples:
# "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

# "apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include 
# "ap3", "a3e", "2p2", "3le", "3l1").





class Solution(object):
    
    # [Examples]
    # "apple", ["blade"] -> "a4" 
    # (because "5" or "4e" conflicts with "blade")
    # "apple", ["plain", "amber", "blade"] -> "1p3" 
    # (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").

    # [Ideas]
    # 1. remove words from dictionary which have different length with target
    # 2. actually we are finding “how to filter whole dict with 
    #    least char number”
    # 3. use bit mask as “which words in dict have same char in certain
    #    position”, with at most 20 masks, find masks combination which 
    #    bust all dict words
    #    => mask1 & mask2 … & mask3 = 0
    # 4. create mask cost O(n), “and” or mask, then BFS by drop mask 1 by 1
    #    => prune branch if mask result no longer 0
    #    => the path drop most masks would be shortest solution


    # adapted from https://discuss.leetcode.com/topic/61690/python-with-bit-masks
    def minAbbreviation(self, target, dictionary):
        m = len(target)
        # find bits used to diff word from target
        diffs = {sum(2**i for i, c in enumerate(word) if target[i] != c)
                 for word in dictionary if len(word) == m}
        if not diffs:
            return str(m)
    
        # collect candidates separate target from dict
        cands = [i for i in range(2**m) if all(d & i for d in diffs)]
        
        # calculate candidate saving most bits
        best_save, best_cand = 0, None
        for c in cands:
            save = 0
            for i in range(m-1):
                save += ((c >> i) & 3 == 0)
            if save >= best_save: 
                best_save, best_cand = save, c
        if not best_cand: return None
                
        s = ''.join(target[i] if best_cand & 2**i else '#' for i in range(m))
        return re.sub('#+', lambda m: str(len(m.group())), s)
    