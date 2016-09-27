# https://leetcode.com/problems/meeting-rooms/

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        
        1. brute force: check whether intervals[i+1]..intervals[n] schedules envelope intervals[i]
            => time complextity: O(n + n-1 + n-2 ...) = O(n^2)
        2. sort according to start time, see if intervals[i+1].start_time < intervals[i].end_time
            => time complextity: sort for O(nlogn), 1 pass check for O(n)
        3. use space tradeoff for time: hashtable every 5 min to check if collition => time O(n) with space O(n)
        """
        times = sorted([(t.start, t.end) for t in intervals])
        last_s, last_e = -1, -1
        for s, e in times:
            if (s < last_e):
                return False
            last_s, last_e = s, e
        return True
        