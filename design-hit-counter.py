# https://leetcode.com/problems/design-hit-counter/

# Design a hit counter which counts the number of hits received in the past 5 minutes.

# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

# It is possible that several hits arrive roughly at the same time.

# Example:
# HitCounter counter = new HitCounter();

# // hit at timestamp 1.
# counter.hit(1);

# // hit at timestamp 2.
# counter.hit(2);

# // hit at timestamp 3.
# counter.hit(3);

# // get hits at timestamp 4, should return 3.
# counter.getHits(4);

# // hit at timestamp 300.
# counter.hit(300);

# // get hits at timestamp 300, should return 4.
# counter.getHits(300);

# // get hits at timestamp 301, should return 3.
# counter.getHits(301); 
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?

import bisect

class HitCounter(object):

    # [Idea]
    # 1. save log in list 'log'
    # 2. each time getHits, find earliest value (index=k) within 5 mins,
    #    then forget: log = log[k:] 
    
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = []
            

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.log.append(timestamp)
        
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        idx = bisect.bisect(self.log, timestamp-300)
        self.log = self.log[idx:]
        return len(self.log)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


# print(bisect.bisect([(0,'a'),(1,'a'),(2,'c'),(3,'b'),(10,'k')], 3))