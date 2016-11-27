# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


# Given a digit string, return all possible letter combinations 
# that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.



# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution(object):

    mapper = {
      '1': '*',
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz',
      '0': ' '
    }
      
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # [Ideas]
        # 1. recursion, pass possible letter until no rest digits, add to results.
        # 2. possible DP?
        if not digits: return []
        
        return self.rec_combs(digits)
        
        
    def rec_combs(self, digits):
        if len(digits) == 0:
            return ['']
        else:
            cands = self.mapper[digits[0]]
            rests = self.rec_combs(digits[1:])
            results = []
            for c in cands:
                results += [(c + r) for r in rests]
            return results


    def test(self):
        cases = [
            '',
            '0',
            '1',
            '6',
            '12',
            '23',
            '243',
            '2345',
        ]
        for c in cases:
            res = self.letterCombinations(c)
            print(c, res)
            
Solution().test()