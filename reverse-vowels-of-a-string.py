# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Given s = "hello", return "holle".

# Example 2:
# Given s = "leetcode", return "leotcede".

# Note:
# The vowels does not include the letter "y".

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        
        vowels = [(i, c) for i, c in enumerate(s) if c in 'aeiouAEIOU']
        rev_vowels = [c for i, c in vowels][::-1]
        
        update = {i: c for (i, _), c in zip(vowels, rev_vowels)}
        
        ans = [update[i] if (i in update) else s[i] for i in range(len(s))]
        ans = ''.join(ans)
        return ans
    
    
    def test(self):
        cases = [
            "",
            "abcde",
            "aeiou",
            "hello",
            "leetcode",
        ]
        for c in cases:
            print(c, self.reverseVowels(c))
            
            
            
        
# Solution().test()