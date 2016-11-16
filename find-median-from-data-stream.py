# https://leetcode.com/problems/find-median-from-data-stream/

# Median is the middle value in an ordered integer list. If the size of 
# the list is even, there is no middle value. So the median is the mean 
# of the two middle value.

# Examples: 
# [2,3,4] , the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# For example:

# add(1)
# add(2)
# findMedian() -> 1.5
# add(3) 
# findMedian() -> 2


from heapq import *

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # max-heap for smaller-half, min-heap for larger-half
        self.hmin, self.hmax = [], []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # if num < max_of_smaller, cast to smaller part
        # if num >= max_of_smaller, cast to larger part
        # if len(smaller) > len(larger), pop smaller to larger
        # else pop larger to smaller
        # 
        # will min_of_larger thus smaller than max_of_smaller?
        
        
        heappush(self.hmin, -heappushpop(self.hmax, num))
        if len(self.hmin) > len(self.hmax):
            heappush(self.hmax, -heappop(self.hmin))
        
        
        
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        size = len(self.hmin) + len(self.hmax)
        if size == 0:
            sol = 0
        elif size % 2 == 0:
            sol = float(self.hmax[0] - self.hmin[0]) / 2
        # size % 2 == 1
        elif len(self.hmax) > len(self.hmin): 
            sol = self.hmax[0]  
        else: 
            sol = -self.hmin[0]
        return float(sol)
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
