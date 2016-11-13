# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

# You are given two integer arrays nums1 and nums2 sorted 
# in ascending order and an integer k.

# Define a pair (u,v) which consists of one element from 
# the first array and one element from the second array.

# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

# Example 1:
# Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

# Return: [1,2],[1,4],[1,6]

# The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:
# Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

# Return: [1,1],[1,1]

# The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# Example 3:
# Given nums1 = [1,2], nums2 = [3],  k = 3 

# Return: [1,3],[2,3]

# All possible pairs are returned from the sequence:
# [1,3],[2,3]

import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        # [Ideas]
        # 1. find smallest-k => max-heap with size k,
        #    if new_value < heap_top, replace top with new_value
        # -------------------------------------
        # 2. only 2 sequence => two pointer, 
        #    find smaller delta to move forward
        # X. this doesn't go through all pairs ...
        
        if (not nums1) or (not nums2): return []
        
        h = []
        for n1 in nums1:
            for n2 in nums2:
                if len(h) < k:
                    heapq.heappush(h, (-(n1+n2), [n1, n2]))
                else:
                    if n1+n2 < -h[0][0]:
                        heapq.heapreplace(h, (-(n1+n2), [n1, n2]))
        ans = [pair for val, pair in h]                
        return ans
    
    
    def test(self):
        cases = [
            ([], [], 2),
            ([1,7,11], [2,4,6],3),
            ([1,1,2], [1,2,3], 2),
            ([1,2], [3], 3),
            ([1,1,2],[1,2,3],10),
            ([1,1,2],[1,2,3],2),
        ]
        for n1, n2, k in cases:
            print(self.kSmallestPairs(n1, n2, k))
                 
                  
Solution().test()