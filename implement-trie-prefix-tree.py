# https://leetcode.com/problems/implement-trie-prefix-tree/

# Implement a trie with insert, search, and startsWith methods.

# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_word = False
        self.children = {}
        
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if (word == None) or (len(word) == 0):
            return False
        
        node = self.root
        for c in word:                              # "abc", "abd"
            if c in node.children:    
                node = node.children[c]
            else:
                node.children[c] = TrieNode()
                node = node.children[c]
        node.is_word = True
        return True
                
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if (word == None) or (len(word) == 0):
            return False
        
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.is_word
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if (prefix == None) or (len(prefix) == 0):
            return False
        
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True
        
# #------------------------------------        
# def trie_unit_test():
#     cases = [
#         {
#             "insert": ["abc", "abd", "", None], 
#             "search": ["abcd", "abd", "", None],
#             "startWith": ["abc", "bd"],
#         }
#     ]
#     for case in cases:
#         trie = Trie()
#         for i in case["insert"]:
#             print("insert %s" % i, trie.insert(i))
#         for i in case["search"]:
#             print("search %s" % i, trie.search(i))
#         for i in case["startWith"]:
#             print("startWith %s" % i, trie.startsWith(i))
    
# trie_unit_test()