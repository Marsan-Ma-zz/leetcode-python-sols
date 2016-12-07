# https://leetcode.com/problems/word-pattern/

# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between 
# a letter in pattern and a non-empty word in str.

# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains 
# lowercase letters separated by a single space.


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        mapper = {}
        words = str.split()
        if len(pattern) != len(words): return False
        
        visited = set()
        for i, p in enumerate(pattern):
            if p not in mapper:
                if words[i] in visited: 
                    return False
                mapper[p] = words[i]
                visited.add(words[i])
            elif mapper[p] != words[i]:
                return False
        return True
            