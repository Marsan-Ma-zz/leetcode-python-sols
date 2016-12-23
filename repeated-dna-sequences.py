# https://leetcode.com/problems/repeated-dna-sequences/

# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify 
# repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur 
# more than once in a DNA molecule.

# For example,

# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].



from collections import defaultdict
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        visit = defaultdict(int)
        for i in range(10, len(s)+1):
            visit[s[i-10:i]] += 1
        return [k for k,v in visit.items() if v > 1]