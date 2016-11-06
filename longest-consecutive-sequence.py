# https://leetcode.com/problems/longest-consecutive-sequence/

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # [Ideas]
        # 1. check only from the min of consecutives
        
        best = 0
        nums = set(nums)
        for n in nums:
            if n-1 in nums:
                continue
            else:
                ns = n
                while ns+1 in nums:
                    ns += 1
                best = max(best, ns-n+1)
        return best
    
    
    def test(self):
        cases = [
            [],
            [100, 4, 200, 1, 3, 2],
            [100, 4, 200, 1, 3, 2, 5],
            [100, 4, 200, 1, 2],
        ]
        for c in cases:
            print(c, self.longestConsecutive(c))
            
# Solution().test()
                
        
        