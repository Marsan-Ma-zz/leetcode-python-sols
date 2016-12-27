# https://leetcode.com/problems/palindrome-permutation-ii/

# Given a string s, return all the palindromic permutations (without duplicates) of it. 
# Return an empty list if no palindromic permutation could be form.

# For example:

# Given s = "aabb", return ["abba", "baab"].

# Given s = "abc", return [].

# Hint:

# If a palindromic permutation exists, we just need to generate the first half of the string.
# To generate all distinct permutations of a (half of) string, use a similar approach from: 
# Permutations II or Next Permutation.



from collections import Counter

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        # [Ideas]
        # 1. collect half-palindrome items
        # 2. permutation use half-palindrome items
        #    => how to avoid duplicate? like in "permutations-ii" and "combination-sum-ii"
        #    => "sort" + "if i > 0 and nums[i] == nums[i-1]"
        
        if not s: return []
        
        # collect half-side items
        stat = Counter(s)
        single = None
        chars = []
        for k,v in stat.items():
            if v % 2 == 1:
                if single: return []
                single = k
            chars.extend([k]*(v//2))
        chars = ''.join(chars)  # because string append by += cost O(n) for each!!
            
        # DFS get sols
        self.sols = []
        def dfs(chars, items):
            if not chars:
                self.sols.append(items)
            else:
                for i, c in enumerate(chars):
                    if i > 0 and c == chars[i-1]:
                        continue
                    dfs(chars[:i] + chars[i+1:], items+[c])
            
        dfs(chars, [])
        
        # generate sols
        if single:
            self.sols = ["".join(s+[single]+s[::-1]) for s in self.sols]
        else:
            self.sols = ["".join(s+s[::-1]) for s in self.sols]
        return self.sols
        