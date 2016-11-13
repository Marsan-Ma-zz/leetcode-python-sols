# https://leetcode.com/problems/add-and-search-word-data-structure-design/

# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string 
# containing only letters a-z or .. A . means it can represent any one letter.

# For example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.is_word = True
        

    def search_helper(self, word, node):
        for i, w in enumerate(word):
            if w == '.':
                for c, child in node.children.items():
                    if self.search_helper(word[i+1:], child):
                        return True
                return False
            else:
                if w not in node.children:
                    return False
                node = node.children[w]
        return node.is_word

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.search_helper(word, self.root)
        
#     def unit_test(self):
#         cases = [
#             [[], ['aaa']],
#             [['aaa', 'bbb'], ['aaa']],
#             [['aa', 'bbb'], ['aaa', 'bbbbb']],
#             [['bad', 'dad', 'mad'], ['pad', 'bad', '.ad', 'b..']],
#         ]
#         for ins, sea in cases:
#             wd = WordDictionary()
#             for i in ins:
#                 wd.addWord(i)
#             for s in sea:
#                 print(wd.search(s))
                

# WordDictionary().unit_test()                