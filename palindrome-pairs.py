# https://leetcode.com/problems/palindrome-pairs/

# Given a list of unique words, find all pairs of distinct indices (i, j) 
# in the given list, so that the concatenation of the two words, 
# i.e. words[i] + words[j] is a palindrome.


# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]

# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]



class Solution(object):
    
    # it's a waste to use Trie when we always compare whole word!!
    # use hashmap instead.
    def palindromePairs(self, words):
        
        d, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
        
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                prefix, postfix = w[:j], w[j:]
                if prefix in d and i != d[prefix] and postfix == postfix[::-1]:
                    res.append([i, d[prefix]])
                if j>0 and postfix in d and i != d[postfix] and prefix == prefix[::-1]:
                    res.append([d[postfix], i])
        return res 

    
#     def palindromePairs(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[List[int]]
#         """
        
#         # [Ideas]
#         # 1. compare 1 word with all the others => use Trie
#         # 2. Trie and word to check in opposite order
#         # 3. while check to trie end or word end, valid whether 
#         #    the rest substring is palindrome
        
#         def is_pal(word):
#             mid = len(word)//2
#             for i in range(mid):
#                 if word[i] != word[-i-1]:
#                     return False
#             return True
        
#         def traverse_trie(node):
#             cands = []
#             def dfs(n, s):
#                 if '' in n and is_pal(s):
#                     cands.append(n[''])
#                 for c in n:
#                     if c != '': dfs(n[c], s+c)
#             for n in node:
#                 if n != '':
#                     dfs(node[n], n)
#             return cands
                
        
#         # build Trie with reversed word
#         root = {}
#         for i, w in enumerate(words):
#             node = root
#             for c in w[::-1]:
#                 node = node.setdefault(c, {})
#             node[''] = i    # is_word = word_index
#         # print(root)
        
        
#         # find palindrome
#         sols = []
#         for i, w in enumerate(words):
#             node = root
#             check = True
#             for j, c in enumerate(w):
#                 if c in node:
#                     node = node[c]
#                     if '' in node and node[''] != i and is_pal(w[j+1:]):
#                         sols.append([i, node['']])
#                 else:
#                     check = False
#                     break
#             if check:
#                 for k in traverse_trie(node):
#                     sols.append([i, k])
        
#         # for FUCKING '' case
#         if '' in words:
#             k = words.index('')
#             for i in range(len(words)):
#                 sols.extend([[i, k], [k, i]])
#         return sols
                        
                    
    def test(self):
        cases = [
            ["a", ''],
            ["a", "ab"],
            ["bat", "tab", "cat"],
            ["abcd", "dcba", "lls", "s", "sssll"],
            ["lls", "sssll"],
        ]
        for c in cases:
            print(c, self.palindromePairs(c))
            
            
Solution().test()