# https://leetcode.com/problems/valid-word-abbreviation/

# Given a non-empty string s and an abbreviation abbr, return whether 
# the string matches with the given abbreviation.

# A string such as "word" contains only the following valid abbreviations:

# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", 
# "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Notice that only the above abbreviations are valid abbreviations of the 
# string "word". Any other string is not a valid abbreviation of "word".

# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

# Example 1:
# Given s = "internationalization", abbr = "i12iz4n":

# Return true.
# Example 2:
# Given s = "apple", abbr = "a2e":

# Return false.


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        
        # [Ideas]
        # 1. use 1 pointer, decode abbr and move pointer of word
        
        if not word: return (abbr == '')
            
        ptr = 0
        
        digits = ''
        for c in abbr:
            if c.isdigit():
                digits += c
            elif digits:
                if digits[0] == '0': return False
                ptr += int(digits)
                digits = ''
                if (ptr >= len(word)) or (word[ptr] != c):
                    return False
                else:
                    ptr += 1
            else:
                if (ptr >= len(word)) or (word[ptr] != c):
                    return False
                else:
                    ptr += 1
        # rest digits
        if digits:
            if digits[0] == '0': return False
            ptr += int(digits)
            if ptr != len(word):
                return False
        # print("rest:", ptr, word[ptr:])
        return (word[ptr:] == '')
    
    
    
    def test(self):
        cases = [
            ('', ''),
            ('', 'a'),
            ('a', ''),
            ('word', 'w1rd'),
            ('word', 'w2d'),
            ('word', 'w3'),
            ('word', '4'),
            ('internationalization', 'i18n'),
            ('internationalization', 'i12iz4n'),
            ('apple', 'a2e'),
            ('apple', 'a3e'),
        ]
        for word, abbr in cases:
            print(word, abbr, self.validWordAbbreviation(word, abbr))
            
            
# Solution().test()