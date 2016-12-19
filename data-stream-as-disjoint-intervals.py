# https://leetcode.com/problems/data-stream-as-disjoint-intervals/

# Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize 
# the numbers seen so far as a list of disjoint intervals.

# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then 
# the summary will be:

# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
# Follow up:
# What if there are lots of merges and the number of disjoint intervals are small compared 
# to the data stream's size?





# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import *
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        heappush(self.nums, (val, Interval(val, val)))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        sols = []
        while self.nums:
            v, itv = heappop(self.nums)
            if sols and sols[-1][1].end >= itv.start-1:
                sols[-1][1].end = max(sols[-1][1].end, itv.end)
            else:
                sols.append((v, itv))
        self.nums = sols  # sorted list is natively heapified heap!
        return [itv for _, itv in sols]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()