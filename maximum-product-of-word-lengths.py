# https://leetcode.com/problems/maximum-product-of-word-lengths/

# Given a string array words, find the maximum value of 
# length(word[i]) * length(word[j]) where the two words do not share 
# common letters. You may assume that each word will contain only lower 
# case letters. If no such two words exist, return 0.

# Example 1:
# Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# Return 16
# The two words can be "abcw", "xtfn".

# Example 2:
# Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# Return 4
# The two words can be "ab", "cd".

# Example 3:
# Given ["a", "aa", "aaa", "aaaa"]
# Return 0
# No such pair of words.


# use bit filter to check words having same character
class Solution(object):

    # [Ideas]
    # 1. map words with same chars to one same key, 
    #    the value would be maximum length of same category words
    def maxProduct(self, words):
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        # [Ideas]
        # 1. sort by length, then traverse all possibility from largest-2
        # 2. time complexity: O(n**2)
        # 3. improve: double for-loop, break inner if ans smaller than best
        # ---------------------------------
        # 1. it's not possible to solve in O(n) or O(nlog(n)))
        
        if not words: return 0
        
        words = [(w, len(w)) for w in words]
        words = sorted(words, key=lambda v: v[1], reverse=True)
        
        best = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                sol = words[i][1] * words[j][1]
                if sol <= best: break
                    
                # check valid
                valid = True
                for c in words[j][0]:
                    if c in words[i][0]:
                        valid = False
                        break
                if valid:
                    best = max(best, sol)
        return best
        
        
    def test(self):
        cases = [
            [],
            ['a', 'b'],
            ['a', 'b', 'cc', 'ddd', 'eeeee'],
            ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], #16
            ["a", "ab", "abc", "d", "cd", "bcd", "abcd"], #4
            ["a", "aa", "aaa", "aaaa"], #0
        ]
        for c in cases:
            print(c, self.maxProduct(c))
            
            
# Solution().test()
