# https://leetcode.com/problems/insert-interval/

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from bisect import bisect

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        
        # [Ideas]
        # 1. bisect to search for insert point maintaining sorted by start
        # 2. one-pass merge to tail
        
        if not intervals: return [newInterval]
        
        # insert
        k = bisect([(v.start) for v in intervals], newInterval.start)
        intervals = intervals[:k] + [newInterval] + intervals[k:]
        
        # merge
        res = []
        for i in intervals:
            if res and (i.start <= res[-1].end):
                res[-1].end = max(i.end, res[-1].end)
            else:
                res.append(i)
        return res
    