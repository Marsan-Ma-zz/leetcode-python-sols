# https://leetcode.com/problems/remove-duplicate-letters/

# Given a string which contains only lowercase letters, remove duplicate letters 
# so that every letter appear once and only once. You must make sure your result 
# is the smallest in lexicographical order among all possible results.

# Example:
# Given "bcabc"
# Return "abc"

# Given "cbacdcbc"
# Return "acdb"



from collections import defaultdict

class Solution(object):

    # by recursion
    def removeDuplicateLetters(self, s):
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # [Ideas]
        # 1. when we pick the best char with smallest 
        #    lexicographical order: we want to make sure there are other 
        #    chars available behine this.
        #    => build a "chars available to the right" table
        # 2. if leftmost occurence of this char can't fulfill, 
        #    others (right) have no chance.
        #    => build char occurence position table
        #    => pop index smaller than current position before use
        if not s: return ''
        
        # build position info
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)
        
        # build available char to the right info
        avail = [set()] * len(s)
        for i, c in reversed(list(enumerate(s))):
            if i == len(s)-1:
                avail[i] = {c}
            else:
                avail[i] = avail[i+1] | {c}
        # print(pos, avail)
            
        # construct sol
        sol = []
        need = set(pos.keys())
        cur = 0
        while len(sol) < len(avail[0]):
            for c in sorted(need):
                p = [p for p in pos[c] if p >= cur][0]
                if len(need - avail[p] - set([c])) == 0:
                    sol.append(c)
                    cur = p
                    del pos[c]
                    need -= {c}
                    break
        
        return ''.join(sol)
    
    
    def test(self):
        cases = [
            '',
            'a',
            'bcabc',
            'cbacdcbc',
            'cbacdcbccbacdcbccbacdcbc',
            'ecbacdcbccbafcdcbccbacdcbcd',
        ]
        for c in cases:
            print(c, self.removeDuplicateLetters(c))
            
            
# Solution().test()

# print([set()] * 10)