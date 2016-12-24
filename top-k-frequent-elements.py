# https://leetcode.com/problems/top-k-frequent-elements/

# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


from collections import Counter
from heapq import *

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        h = []
        for s,v in Counter(nums).items():
            if len(h) < k:
                heappush(h, (v, s))
            elif v > h[0][0]:
                heapreplace(h, (v, s))
                
        return [s for v,s in h]