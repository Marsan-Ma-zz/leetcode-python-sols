# https://leetcode.com/problems/russian-doll-envelopes/

# You have a number of envelopes with widths and heights given as a pair of 
# integers (w, h). One envelope can fit into another if and only if both the 
# width and height of one envelope is greater than the width and height of 
# the other envelope.

# What is the maximum number of envelopes can you Russian doll? (put one inside other)



from bisect import bisect_left

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
        # [Ideas]
        # 1. sort by (width, -height), then traverse this new series
        #    in height since width is already ascending.
        # 2. it becomes "longest increasing subsequence" problem:
        #    => doing something like insertion sort, but:
        #    => instead of insertion, do "replace"
        #    => use binary search to make searching log(n) per time.
        #
        # [10, inf, inf, inf, inf, inf, inf, inf, inf] 
        # [9, inf, inf, inf, inf, inf, inf, inf, inf] 
        # [2, inf, inf, inf, inf, inf, inf, inf, inf] 
        # [2, 5, inf, inf, inf, inf, inf, inf, inf] 
        # [2, 3, inf, inf, inf, inf, inf, inf, inf] 
        # [2, 3, 7, inf, inf, inf, inf, inf, inf] 
        # [2, 3, 7, 101, inf, inf, inf, inf, inf] 
        # [2, 3, 7, 18, inf, inf, inf, inf, inf] 

        envelopes = sorted(envelopes, key=lambda v: (v[0], -v[1]))
        # print(envelopes)
        
        nums = [float('inf')]*len(envelopes)
        for w, h in envelopes:
            pos = bisect_left(nums, h)
            nums[pos] = h
            # print(nums)
            
        return bisect_left(nums, float('inf'))
        

    def test(self):
        cases = [
            [],
            [[5,4],[6,4],[6,7],[2,3]],
        ]
        for c in cases:
            print(c, self.maxEnvelopes(c))
            
            
# Solution().test()
        