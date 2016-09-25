# https://leetcode.com/problems/implement-strstr/

# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# 5:38
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (haystack == ""): 
            return 0 if (needle == "") else -1
        if (needle == ""):
            return 0
            
        nlen = len(needle)
        for i in range(len(haystack)):
            if (needle == haystack[i:i+nlen]):
                return i
        return -1
        
#     def unit_test(self):
#         cases = [
#             ["", ""],
#             ["aferwfertsrabc", "abc"],
#             ["aaaab", "aaaaaab"],
#             ["aaaaaab", "aaaab"],
#         ]
#         for haystack, needle in cases:
#             print(haystack, needle, self.strStr(haystack, needle))
        
# Solution().unit_test()