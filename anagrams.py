# https://leetcode.com/problems/anagrams/

# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        [examples]
            given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
            [
              ["ate", "eat","tea"],
              ["nat","tan"],
              ["bat"]
            ]
        
        [ideas]
            1. use hashmap to profile elements of given strings. 
            2. use sorted string to be hashmap key. 
            3. return inner list must follow the lexicographic order.
            time complexity: O(n*m*log(m)), 
                n : strs 
                m : largest chars of the strings
            O(n) space complexity
        """
        
        # boundary case
        if strs == None: return []
        
        # build hashmap (categorize input)
        table = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in table:
                table[sorted_s].append(s)
            else:
                table[sorted_s] = [s]
                
        # build answer
        return [sorted(vec) for key, vec in table.items()]
    
#     def unit_test(self):
#         cases = [
#             None,
#             [],
#             ['a'],
#             ["eat", "tea", "tan", "ate", "nat", "bat"],
#         ]
#         for case in cases:
#             ans = self.groupAnagrams(case)
#             print(case, ans)
            
# Solution().unit_test()