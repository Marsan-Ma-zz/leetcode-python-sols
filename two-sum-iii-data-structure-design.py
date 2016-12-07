# https://leetcode.com/problems/two-sum-iii-data-structure-design/

# Design and implement a TwoSum class. It should support the following operations: add and find.

# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.

# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false


class TwoSum(object):

    def __init__(self):
        self.d = {}
        
    def add(self, n):
        self.d[n] = self.d.get(n, 0) + 1

    def find(self, v):
        d = self.d
        for nbr in d:
            t = v - nbr
            if t in d and d[t] - (t is nbr):
                return True
        return False