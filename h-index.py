# https://leetcode.com/problems/h-index/

# Given an array of citations (each citation is a non-negative integer) 
# of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: 
# "A scientist has index h if h of his/her N papers have at least h citations 
# each, and the other N − h papers have no more than h citations each."

# For example, given citations = [3, 0, 6, 1, 5], which means the researcher 
# has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations 
# respectively. Since the researcher has 3 papers with at least 3 citations each 
# and the remaining two with no more than 3 citations each, his h-index is 3.

from collections import Counter

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        
        1. use a hash map to record count of cites in O(n) time complexity => cites = {3:1, 0:1, 6:1, 1:1, 5:1}
        2. check through all keys, find max(i) for cites[i] > i
        """
        if len(citations) == 0: return 0
        
        # (case: [3, 0, 6, 1, 5])
        cites = Counter(citations)
        max_cite = max(cites.keys())

        # find h_idx
        h_idx = 0
        total_cites = 0
        for i in reversed(range(max_cite+1)):         # [i]: 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0
            if i in cites:                           # [total_cites]: 
                total_cites += cites[i]              #      1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 5
            if total_cites >= i:
                h_idx = i
                break
            
        return h_idx
                