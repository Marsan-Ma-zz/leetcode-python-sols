# https://leetcode.com/problems/meeting-rooms-ii/

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.


import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        # [Ideas]
        # 1. might need some special data structure: tree? heap? n-stacks?
        # 2. sort intervals by maybe start-time?
        # 3. check: 
        #      if overlap with last interval => into different group
        #      if non-overlap => into one group
        #      => a min-heap which each node is a group
        #      => the min-heap sorting value is the group ending time
        #      => if new interval begin-time < min in heap, 
        #         append to heap-top group (update the heap-top)
        # 4. it might have multiple suit group to insert, 
        #    append to which one doesn't affect the result, 
        #    since latter-interval-start always larger than current-start
        
        if not intervals: return 0
        
        intervals = sorted([(i.start, i.end) for i in intervals])
        heap = [intervals[0][1]]
        
        for ts, te in intervals[1:]:
            if ts >= heap[0]:
                heapq.heapreplace(heap, te)
            else: # ts < heap[0]
                heapq.heappush(heap, te)
                
        return len(heap)
    
    def test(self):
        cases = [
            [],
            [[0, 30],[5, 10],[15, 20]],
            [[0, 30],[5, 15],[15, 20]],
            [[0, 30],[5, 16],[15, 20]],
        ]
        for c in cases:
            print(c, self.minMeetingRooms(c))
            
    
# Solution().test()