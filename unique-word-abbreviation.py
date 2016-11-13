# https://leetcode.com/problems/unique-word-abbreviation/

# An abbreviation of a word follows the form <first letter><number><last letter>. 
# Below are some examples of word abbreviations:

# a) it                      --> it    (no abbreviation)

#      1
# b) d|o|g                   --> d1g

#               1    1  1
#      1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n

#               1
#      1---5----0
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation 
# is unique in the dictionary. A word's abbreviation is unique if no other word 
# from the dictionary has the same abbreviation.

# Example: 
# Given dictionary = [ "deer", "door", "cake", "card" ]

# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true


from collections import defaultdict

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dict = defaultdict(set)
        for d in dictionary:
            key = self.word2key(d)
            self.dict[key] |= {d}
        

    def word2key(self, word):
        l = len(word)
        if (l <= 2):
            key = word  
        else: 
            key = "%s%i%s" % (word[0], len(word)-2, word[-1])
        return key
        
        
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        key = self.word2key(word)
        pool = self.dict[key]
        unique = (len(pool - {word}) == 0)
        # if len(self.dict) < 10:
        #     print(self.dict, unique)
        return unique
