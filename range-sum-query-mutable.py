# https://leetcode.com/problems/range-sum-query-mutable/

# Given an integer array nums, find the sum of the elements between 
# indices i and j (i ≤ j), inclusive.

# The update(i, val) function modifies nums by updating the element 
# at index i to val.
# Example:
# Given nums = [1, 3, 5]

# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.



class BinaryIndexedTree(object):

    def __init__(self, size):
        self.sums = [0] * (size+1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += val
            i += (i & -i)

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= (i & -i)
        return r


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.bit = BinaryIndexedTree(len(nums))
        for i, n in enumerate(nums):
            self.bit.update(i+1, n)
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.nums[i]
        self.bit.update(i+1, diff)
        self.nums[i] = val
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.bit.sum(j+1) - self.bit.sum(i)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)