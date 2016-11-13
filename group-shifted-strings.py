# https://leetcode.com/problems/group-shifted-strings/

# Given a string, we can "shift" each of its letter to its 
# successive letter, for example: "abc" -> "bcd". We can 
# keep "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, 
# group all strings that belong to the same shifting sequence.

# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# A solution is:

# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]


from collections import defaultdict

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        
        # [Ideas]
        # 1. transform string to corresponding 'deltas' between 
        #    consecutive string
        # 2. save them to hashmap, using the 'deltas' as key
        
        
        mapper = defaultdict(list)
        
        for word in strings:
            key = [self.diff(word[i], word[i+1]) 
                   for i in range(len(word)-1)]
            mapper[str(key)].append(word)
                           
        return list(mapper.values())
                           
    def diff(self, c1, c2):
        n1 = ord(c1) - ord('a')
        n2 = ord(c2) - ord('a')
        ans = (26 + (n1-n2)) % 26
        return ans
                
                
    def test(self):
        cases = [
            [],
            ['a', 'c'],
            ['ab', 'cd', 'eg'],
            ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
        ]
        for c in cases:
            print(c, self.groupStrings(c))
                
Solution().test()