# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.


import heapq
from math import log

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        
        1. use a min_heap with length k, heapify initialize k nums
           => replace min if nums[i] > heap[0] for nums[k+1:]
           time complexity O((n-k)*log(k)), space complexity O(k)
        """
        if len(nums) < k: return None
        
        heap = nums[:k]
        heapq.heapify(heap) # min_heap with size k
        for n in nums[k:]:
            if n > heap[0]:
                heapq.heapreplace(heap, n)
        return heap[0]