# https://leetcode.com/problems/isomorphic-strings/

# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character 
# while preserving the order of characters. No two characters may map to 
# the same character but a character may map to itself.

# For example,
# Given "egg", "add", return true.

# Given "foo", "bar", return false.

# Given "paper", "title", return true.

# Note:
# You may assume both s and t have the same length.


# [Ideas]
# 1. use hashmap to scan s: key is char, value is all_appear_occurence
# 2. then valid t by this hashmap


from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        mapper = defaultdict(list)
        for i, c in enumerate(s):
            mapper[c].append(i)

        visited = set()
        for k, vs in mapper.items():
            c = t[vs[0]]
            # check duplicate
            if c in visited: 
                return False
            else:
                visited.add(c)
            # check unify
            for v in vs[1:]:
               if t[v] != c:
                   return False
        return True
