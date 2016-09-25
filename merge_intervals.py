# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


import heapq

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        # [Ideas]
        # 1. use min-heap to save intervals, then pop one-by-one.
        # 2. if poped interval start smaller than current tail, merge. 
        # 3. else, create new interval

        h = [(i.start, i.end) for i in intervals]
        heapq.heapify(h)

        res = []
        tail = -1
        while h:
            istart, iend = heapq.heappop(h)
            print(istart, iend)
            if istart > tail:
                tail = iend
                res.append(Interval(istart, iend))
            else:
                tail = max(tail, iend)
                res[-1].end = tail
        return res

        