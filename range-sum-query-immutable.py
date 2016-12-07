# https://leetcode.com/problems/range-sum-query-immutable/

# Given an integer array nums, find the sum of the elements between 
# indices i and j (i ≤ j), inclusive.

# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3

# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.



class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.tbl = [0]
        s = 0
        for n in nums:
            s += n
            self.tbl.append(s)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tbl[j+1] - self.tbl[i]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)