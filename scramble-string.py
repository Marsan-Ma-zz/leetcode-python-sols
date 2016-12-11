# https://leetcode.com/problems/scramble-string/

# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

# Below is one possible representation of s1 = "great":

#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.

# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".

# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".

# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.




from collections import Counter
class Solution(object):
    
    dp = {}
    
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        # [Ideas]
        # 1. if len < 4 and chars are the same, valid
        #    => sorted(s1) == sorted(s2)
        # 2. if not, recursive split them
        
        if len(s1) != len(s2) or Counter(s1) != Counter(s2):
            return False
        
        if len(s1) < 4 or (s1 == s2):
            return True
        
        if (s1, s2) in self.dp: return self.dp[(s1, s2)]
        
        for i in range(1, len(s1)):
            c1 = self.isScramble(s1[:i], s2[:i])
            c2 = self.isScramble(s1[i:], s2[i:])
            c3 = self.isScramble(s1[:i], s2[-i:])
            c4 = self.isScramble(s1[i:], s2[:-i])
            if (c1 and c2) or (c3 and c4):
                self.dp[(s1, s2)] = True
                return True
        self.dp[(s1, s2)] = False
        return False
    
        
    def test(self):
        cases = [
            ('', ''),
            ('abc', 'cab'),
            ('great', 'rgtae'),
        ]
        for s1, s2 in cases:
            print(s1, s2, self.isScramble(s1, s2))
            
# Solution().test()