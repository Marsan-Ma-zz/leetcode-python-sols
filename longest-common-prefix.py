# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # [Ideas]
        # 1. there is no way to know before check each char,
        #    just implement flow control carefully.
        
        if not strs: return ''
        
        max_n = min([len(s) for s in strs])
        for i in range(max_n):
            c = strs[0][i]
            for s in strs[1:]:
                if s[i] != c:
                    return strs[0][:i]
        return strs[0][:max_n]
    
    
    def test(self):
        cases = [
            [],
            ['abc', 'aba', 'abb'],
            ['abc', 'aba', 'abb', 'avv'],
            ['abc', 'aba', 'abb', 'avv', 'bdd'],
            ['abcde'],
            ['abgde', 'abcde'],
            ['abcdefg', 'abcdefg', 'abcdefg'],
            ['abcdefg', 'abcdefg', 'abcdefgh'],
        ]
        for c in cases:
            print(c, self.longestCommonPrefix(c))
            
# Solution().test()