# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

# Given a string, find the length of the longest substring T that 
# contains at most k distinct characters.

# For example, Given s = “eceba” and k = 2,

# T is "ece" which its length is 3.



class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # [Examples]
        # 1. s = “eceba” and k = 2 => "ece" which its length is 3
        
        # [Ideas]
        # 1. we could use hashmap to record latest appearing index of 
        #    certain char
        # 2. do a one-pass traverse, for current position, longest 
        #    substring would be: move backward until meet k+1 different 
        #    char, the length would be k => O(n^2) time complexity
        # 3. how to know length in O(1)?
        #    => know how many character appear while backward track
        #    => use a list to record latest changed char index
        #       thus, backward for k diff char would be:
        #       find k+1 char in list => find position of this char,
        #       then sol = position of this char - 1 => done in O(1)
        #       since just table lookup.
        
        tbl = {}
        queue = []
        sol = 0
        for i, c in enumerate(s):
            # update info
            tbl[c] = i
            if c in queue: queue.remove(c)
            queue.append(c)
            
            # get best answer
            if len(queue) <= k:
                sol = max(sol, i+1)
                # print("cand1:", s[:i+1])
            else:
                c_idx = queue[-k-1]
                c_pos = tbl[c_idx]
                # if i-c_pos > sol: print("cand2:", s[c_pos+1:i+1])
                sol = max(sol, i-c_pos)
                
                
        # exception
        if len(queue) < k:
            sol = max(sol, len(s))
                      
        return sol
                      
                    
    def test(self):
        cases = [
            # ("", 2),
            # ("abbaabba", 3),
            # ("eceba", 2),
            # ("kgheceba", 2),
            # ("kgceheceba", 2),
            # ("kgceheceba", 3),
            # ("kgceheceba", 4),
            # ("kgceheceba", 5),
            ("abcdbcdefghiplokploki", 5),
        ]
        for c, k in cases:
            print(c, self.lengthOfLongestSubstringKDistinct(c, k))
            
            
# Solution().test()
                      