# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# No, this one does NOT need heap.
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        
        Solution: Sort intervals by start. Merge intervals by going down the list
        Runtime: O(nlogn)
        """
        if len(intervals) == 0:
            return intervals
        if len(intervals) == 1:
            return intervals
        
        sorted_intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        merged_intervals = [sorted_intervals[0]]
        
        for idx, interval in enumerate(sorted_intervals):
            if interval.start <= merged_intervals[-1].end:
                merged_intervals[-1].end = max(interval.end, merged_intervals[-1].end)
            else:
                merged_intervals.append(interval)
                
        return merged_intervals

# import heapq

# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: List[Interval]
#         """

#         # [Ideas]
#         # 1. use min-heap to save intervals, then pop one-by-one.
#         # 2. if poped interval start smaller than current tail, merge. 
#         # 3. else, create new interval

#         h = [(i.start, i.end) for i in intervals]
#         heapq.heapify(h)

#         res = []
#         tail = -1
#         while h:
#             istart, iend = heapq.heappop(h)
#             print(istart, iend)
#             if istart > tail:
#                 tail = iend
#                 res.append(Interval(istart, iend))
#             else:
#                 tail = max(tail, iend)
#                 res[-1].end = tail
#         return res

#         