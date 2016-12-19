# https://leetcode.com/problems/concatenated-words/

# Given a list of words, please write a program that returns all concatenated words 
# in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two 
# shorter words in the given array.

# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
#  "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".


# Note:
# The number of elements of the given array will not exceed 10,000
# The length sum of elements in the given array will not exceed 600,000.
# All the input string will only include lower case letters.
# The returned elements order does not matter.



class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        # [Ideas]
        # 1. use trie with dfs
        
        # build trie
        root = {}
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})
            node['is_word'] = True
            
        # collect sols (use level to filter only comb by one single word)
        def search(word, level):
            node = root
            if not word and level > 1: return True
            for i, c in enumerate(word):
                node = node.get(c)
                if not node: return False
                if node.get('is_word') and search(word[i+1:], level+1):
                    return True
            return False
        
        sols = [w for w in words if search(w, 0)]
        return sols
    
    
# words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# sols = Solution().findAllConcatenatedWordsInADict(words)
# print(sols)
