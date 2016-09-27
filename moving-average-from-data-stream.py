# https://leetcode.com/problems/moving-average-from-data-stream/

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# For example,
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.len = 0
        self.window = []
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.len == self.size:
            self.window.pop(0)
        else:
            self.len += 1
        self.window.append(val)
        return float(sum(self.window))/self.len


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)