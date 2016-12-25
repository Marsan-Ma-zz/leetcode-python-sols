# https://leetcode.com/problems/non-overlapping-intervals/

# Given a collection of intervals, find the minimum number of intervals you need to remove 
# to make the rest of the intervals non-overlapping.

# Note:
# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
# Example 1:
# Input: [ [1,2], [2,3], [3,4], [1,3] ]

# Output: 1

# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# Example 2:
# Input: [ [1,2], [1,2], [1,2] ]

# Output: 2

# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# Example 3:
# Input: [ [1,2], [2,3] ]

# Output: 0

# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        # [Ideas]
        # 1. sort intervals by startpoint
        # 2. if build overlapped intervals graph 
        #     => remove node with most edges
        #     X. can't guarantee optimum
        # ------------------------------------
        # 3. greedy: always pick interval end first, it occupy 
        #    least space!
        #    => any other choice can't better, at most as better!
        
        right = -float('inf')
        sols = 0
        for n in sorted(intervals, key=lambda v: v.end):
            if n.start < right:
                sols += 1
            else:
                right = max(right, n.end)
        return sols